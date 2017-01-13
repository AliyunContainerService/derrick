from setuptools import setup

setup(
    name='derrick',
    version='0.0.1',
    py_modules=['derrick'],
    include_package_data=True,
    install_requires=[
        'jinja2',
        'docopt',
        'inquirer',
        'pychalk',
        'simplejson',
    ],
    entry_points='''
        [console_scripts]
        derrick=derrick.derrick:main
    ''',
    packages=['derrick', 'derrick.convertor',
              'derrick.cmd', 'derrick.utils', 'derrick.buildpacks',
              'derrick.conf', 'derrick.deployer', 'derrick.utils', ]
)
