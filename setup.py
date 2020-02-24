from setuptools import setup, find_packages

setup(
    name='python-derrick',
    version='0.1.1',
    description="An automation tool to help you dockerize App in seconds",
    keywords='Docker dockerize automation dockerfile docker-compose Jenkinsfile DevOps',
    author="ringtail",
    author_email="zhongwei.lzw@alibaba-inc.com",
    url="https://github.com/alibaba/derrick",
    py_modules=['derrick'],
    include_package_data=True,
    install_requires=[
        'whaaaaat==0.5.2',
        'docopt==0.6.2',
        'pychalk==1.1.0',
        'Jinja2==2.10',
        'chardet==3.0.4',
        'simplejson==3.13.2',
    ],
    entry_points='''
        [console_scripts]
        derrick=derrick.derrick:main
    ''',
    packages=find_packages()
)
