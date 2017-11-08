from setuptools import setup, find_packages

setup(
    name='python-derrick',
    version='0.0.12',
    description="An automation tool to help you dockerize App in seconds",
    keywords='Docker dockerize automation dockerfile docker-compose Jenkinsfile DevOps',
    author="ringtail",
    author_email="zhongwei.lzw@alibaba-inc.com",
    url="https://github.com/alibaba/derrick",
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
        derrick=derrick.derrick:main
    ''',
    packages=find_packages()
)
