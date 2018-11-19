from setuptools import setup, find_packages

setup(
    name='python-derrick',
    version='0.0.23',
    description="An automation tool to help you dockerize App in seconds",
    keywords='Docker dockerize automation dockerfile docker-compose Jenkinsfile DevOps',
    author="ringtail",
    author_email="zhongwei.lzw@alibaba-inc.com",
    url="https://github.com/alibaba/derrick",
    py_modules=['derrick'],
    include_package_data=True,
    install_requires=[
        'jinja2>=2.9',
        'docopt>=0.6.2',
        'whaaaaat>=0.5.2',
        'pychalk==1.1.0',
        'simplejson>=3.11.1',
        'setuptools-git==1.2',
        'idna>=2.6',
        'MarkupSafe>=1.0',
        'nose>=1.3',
        'requests==2.20.0',
        'requests-toolbelt==0.8.0',
        'pkginfo>=1.4.1',
        'prompt-toolkit==1.0.15',
        'Pygments>=2.2.0',
        'six>=1.11.0',
        'tqdm>=4.9.12',
        'wcwidth>=0.1.7',
        'chardet==3.0.4',
    ],
    entry_points='''
        [console_scripts]
        derrick=derrick.derrick:main
    ''',
    packages=find_packages()
)
