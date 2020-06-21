from setuptools import setup, find_packages

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()

VERSION = '0.0.1'

setup(
    name="mkdocs-edupress-theme",
    version=VERSION,
    url='https://github.com/kubilus1/mkdocs-edupress-theme',
    license='GPL',
    description='Edupress theme for mkdocs',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Matt Kubilus',
    author_email='mattkubilus@gmail.com',
    install_requires=[
        'mkdocs>=0.17',
        'mkdocs-paginate-plugin>=0.0.4',
        'mkdocs-datesort-plugin>=0.0.2'
    ],
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        'mkdocs.themes': [
            'edupress = edupress',
        ],
    },
    zip_safe=False
)
