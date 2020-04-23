from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="get-comics",
    version="0.1.0",
    author="Loris M",
    author_email="",
    description="A comicbook scrapper",
    long_description="",
    long_description_content_type="text/markdown",
    url="",
    packages=find_packages(),
    #below line makes sure the library.txt file is downloaded as well
    package_data = {
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt'],
    },
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points = {
        'console_scripts': [
            'get-comics = get_comics.__main__:main'
        ]
    },
    python_requires='>=3.6'
)
