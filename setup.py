from setuptools import setup, find_packages

VERSION = '1.1' 
DESCRIPTION = 'A simple Python library to get information about Steam games using their webpage'
LONG_DESCRIPTION = 'A simple Python library to get information about Steam games using their webpage to check for attributes'

# Setting up
setup(
    name="pythonpyd", 
    version=VERSION,
    author="Sean-e",
    author_email="<seane410@gmail.com>",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    py_modules=['steamwebtools'],  # Include pythonryd.py directly as a module
    install_requires=[],  # Add any additional packages that need to be installed along with your package. Eg: 'requests'
    keywords=['python', 'api'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
