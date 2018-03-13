#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from jinja2 import Template
from whaaaaat import style_from_dict, Token, prompt

from derrick.core.command import Command
from derrick.core.common import *
from derrick.core.derrick import Derrick
from derrick.core.exceptions import RiggingCompileException, ParamsShortageException
from derrick.core.logger import Logger
from derrick.core.models import RiggingDetectInfo
from derrick.core.recorder import ApplicationRecorder


class Init(Command):
    """
    Init command is the most important command in Derrick.
    It will first detect application's platform to judge
    if the registered rigging can handle the application.

    When there is a rigging that can handle the application,
    It's compile function will execute.The compile command
    will return a dict,It contains the template_name and template_content mapping.
    Then Init command will load the template and render the template
    with template_content and flush the rendered template to WORKSPACE.

    If there is more than one rigging that match the application
    Derrick will prompt a choice select window. You can choose one
    rigging to execute.
    """

    def execute(self, context):
        # TODO add application recorder to record the application platform and other things.

        rigging_manager = Derrick().get_rigging_manager()
        all_rigging = rigging_manager.all()

        detected = False
        handled_rigging = []
        for rigging_name in all_rigging:
            rigging = all_rigging.get(rigging_name)
            try:
                handled, platform = rigging.detect(context)
                if handled is True:
                    detected = True
                    handled_rigging.append({"rigging_name": rigging_name, "rigging": rigging, "platform": platform})
            except Exception as e:
                Logger.error("Failed to detect your application's platform with rigging(%s),because of %s"
                             % (rigging_name, e))

        if detected is True:
            if len(handled_rigging) > 1:
                # TODO when more than one rigging can handle your application.
                Logger.warn("More than one rigging can handle the application.")
                rigging_dict = Init.choose_rigging(handled_rigging)
                if rigging_dict is None:
                    Logger.error("The Rigging you chosen maybe broken.")
                    return
            else:
                rigging_dict = handled_rigging[0]

            rigging = rigging_dict.get("rigging")

            try:
                results = rigging.compile(context)
                Logger.debug("The platform is %s,the rigging used is %s"
                             % (rigging_dict.get("platform"), rigging_dict.get("rigging_name")))
                Logger.debug("The results is %s" % results)
            except Exception as e:
                Logger.error("Failed to compile your application.because of %s" % e)
                return

            if type(results) is dict:
                try:
                    template_dir = rigging.get_template_dir()
                    dest_dir = context.get(WORKSPACE_ENV)
                    Logger.debug("Ready to render templates and template_dir:%s,dest_dir:%s,compile_dict:%s" % (
                        template_dir, dest_dir, results))
                    Init.render_templates(templates_dir=template_dir, dest_dir=dest_dir, compile_dict=results)
                    Logger.info("Derrick detect your platform is %s and compile successfully."
                                % rigging_dict.get("platform"))
                except Exception as e:
                    Logger.error("Failed to render template with rigging(%s),because of %s"
                                 % (rigging.get_name(), e))
                try:
                    if results.get("Meta") is not None:
                        image_with_tag = results.get("Meta").get("image_with_tag")
                    rdi = RiggingDetectInfo(rigging_dict.get("rigging_name"), rigging_dict.get("platform"),
                                            image_with_tag)
                    ApplicationRecorder().record(rdi)
                except Exception as e:
                    Logger.debug("Failed to record detected information.because of %s" % e)
            else:
                raise RiggingCompileException("compile results is not a dict.")
        else:
            Logger.warn(
                "Failed to detect your application's platform."
                "Maybe you can upgrade Derrick to get more platforms supported.")
            return

    def get_help_desc(self):
        return "derrick init [--debug]"

    @staticmethod
    def choose_rigging(rigging=None):
        choices = []
        for c_rigging in rigging:
            rigging_name = c_rigging.get("rigging_name")
            platform = c_rigging.get("platform")
            choices.append("[R] %-15s [P] %-s" % (rigging_name, platform))

        questions = [
            {
                'type': 'list',
                'name': 'rigging_choice',
                'message': 'Which rigging would you like to choose?',
                'choices': choices
            }
        ]
        style = style_from_dict({
            Token.Selected: '#00FFFF bold',
        })
        answers = prompt(questions, style=style)
        choice = answers.get('rigging_choice')

        for c_rigging in rigging:
            rigging_name = c_rigging.get("rigging_name")
            platform = c_rigging.get("platform")
            if choice == "[R] %-15s [P] %-s" % (rigging_name, platform):
                return c_rigging
        return None

    # TODO Maybe you can alse define your custom template render using ExtensionPoints
    # Render all templates to dest workspace
    @staticmethod
    def render_templates(templates_dir=None, dest_dir=None, compile_dict=None):
        if templates_dir is None or dest_dir is None or compile_dict is None:
            raise ParamsShortageException("compile templates need some more params")
        all_success = True
        for template_name in os.listdir(templates_dir):
            template_path = os.path.join(templates_dir, template_name)
            try:
                Init.render_template(template_path, dest_dir, compile_dict.get(template_name))
            except Exception as e:
                all_success = False
                Logger.debug("template_path:%s,dest_dir:%s,content:%s"
                             % (template_path, dest_dir, compile_dict.get(template_name)))
                Logger.debug("Failed to compile template(%s),because of %s" % (template_name, e))

        return all_success

    # Render single file to workspace
    @staticmethod
    def render_template(template_path, dest_dir, content):
        template_file = os.path.basename(template_path)

        with open(template_path) as f:
            template_content = f.read()
            # If template is Jinja2 template then render the template or just move the template
            if template_file.endswith(".j2"):
                dest_file_name = template_file[:-3]
                template = Template(template_content)
                converted_content = template.render(content)
            else:
                dest_file_name = template_file
                converted_content = template_content

        dest_file_path = os.path.join(dest_dir, dest_file_name)

        with open(dest_file_path, "w") as dest_file:
            dest_file.write(converted_content)
