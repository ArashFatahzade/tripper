import re
from os.path import join, dirname
from setuptools import setup, find_packages


# reading package version (same way the sqlalchemy does)
with open(join(dirname(__file__), 'tripper', '__init__.py')) as v_file:
    package_version = re.\
        compile(r".*__version__ = '(.*?)'", re.S).\
        match(v_file.read()).\
        group(1)


dependencies = [
    'restfulpy',
    'sqlalchemy_media',

    #Crawling
    'requests',

    # Testing
    'bddrest',

    # Serving
    'gunicorn'
]


setup(
    name="tripper",
    version=package_version,
    author="Arash Fatahzade",
    author_email="arash.fattahzade@carrene.com",
    description="Tripper backend",
    url='https://github.com/ArashFatahzade/tripper.git',
    install_requires=dependencies,
    packages=find_packages(),
    test_suite="tests",
    entry_points={
        'console_scripts': [
            'tripper = tripper:tripper.cli_main'
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Customer Service',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development',
    ],
)
