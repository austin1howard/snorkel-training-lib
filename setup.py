import os
import re

import setuptools

directory = os.path.dirname(os.path.abspath(__file__))

# Extract long_description
path = os.path.join(directory, 'README.md')
with open(path) as read_file:
    long_description = read_file.read()

setuptools.setup(
    name='snorkel-training-lib',
    version='v0.7.0-beta',
    url='https://github.com/HazyResearch/snorkel/tree/master/tutorials/workshop/lib',
    description='Training libs from snorkel examples',
    long_description_content_type='text/markdown',
    long_description=long_description,
    license='Apache License 2.0',
    packages=setuptools.find_packages(),
    include_package_data=True,
)
