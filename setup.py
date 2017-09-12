from setuptools import setup, find_packages

setup(
    name='derrick',
    version='1.0.1',
    py_modules=['derrick'],
    include_package_data=True,
    install_requires=[
        'jinja2',
        'docopt',
        'whaaaaat',
        'pychalk',
        'simplejson',
        'setuptools-git'
    ],
    entry_points='''
        [console_scripts]
        derrick=derrick.main:main
    ''',
    packages=find_packages()
)
