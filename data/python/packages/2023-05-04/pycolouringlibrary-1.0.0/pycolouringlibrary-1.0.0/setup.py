from setuptools import setup, find_packages

VERSION = '1.0.0'
DESCRIPTION = "Colors for Python"
LONG_DESCRIPTION = "Colors for Python"

# Setting up
setup(
    name="pycolouringlibrary",
    version=VERSION,
    author="Bluescreen",
    author_email="nick.faltermeier@gmx.de",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python'],
    classifiers=[
        "Operating System :: Microsoft :: Windows",
    ]
)