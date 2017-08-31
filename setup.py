from setuptools import setup, find_packages

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
    ],
    entry_points='''
        [console_scripts]
        derrick=derrick.main:main
    ''',
    packages=find_packages()
)
