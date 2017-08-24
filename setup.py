from setuptools import setup

setup(
    name='derrick',
    version='1.0.0',
    py_modules=['derrick'],
    include_package_data=True,
    install_requires=[
        'jinja2',
        'docopt',
        'inquirer',
        'pychalk',
        'simplejson',
        'requests',
    ],
    entry_points='''
        [console_scripts]
        derrick=derrick.main:main
    ''',
    packages=['derrick', 'derrick.core', 'derrick.commands', 'derrick.utils', ]
)
