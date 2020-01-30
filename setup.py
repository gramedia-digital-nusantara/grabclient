from os.path import dirname, join, abspath
from setuptools import setup, find_packages

ROOT_DIR = dirname(abspath(__file__))

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['requests']

setup_requirements = []

test_requirements = ['behave']

setup(
    author="Heri Priyatno",
    author_email='heri.priyatno@staff.gramedia.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    description="Python library to consume GRABExpress API",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='grabclient',
    name='grabclient',
    packages=find_packages(where='src'),
    package_dir={'grabclient': join('src', 'grabclient')},
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    version='1.0.0',
    zip_safe=False,
)
