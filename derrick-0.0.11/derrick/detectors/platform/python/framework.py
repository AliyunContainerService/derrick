from derrick.core.common import *
from derrick.core.detector import Detector

DJANGO_ENTRY = "manage.py"
PLAIN_ENTRY = "app.py"


class PythonFrameworkDetector(Detector):
    def execute(self, *args, **kwargs):
        commands_args = []
        detected_files = []
        workspace = get_workspace()
        for file_name in os.listdir(workspace):
            if file_name.endswith(".py") and PythonFrameworkDetector.python_setup_skip(file_name):
                detected_files.append(file_name)

        if len(detected_files) != 0:
            if DJANGO_ENTRY in detected_files:
                commands_args.append(DJANGO_ENTRY)
                commands_args.append("runserver")
                commands_args.append("0.0.0.0:8000")
            else:
                commands_args.append(detected_files[0])

        return {"commands_args": commands_args}

    @staticmethod
    def python_setup_skip(file_name):
        if file_name.find("setup") == -1:
            return True
        return False
