from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="flask_mico",
    version="0.2.3",
    include_package_data=True,
    description="flask mico",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="@buzz",
    url="https://github.com/YE-Kits/flask_mico",
    platforms=["all"],
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
    install_requires=[
        'flask',
        'cerberus'
    ],
    entry_points={
        'console_scripts': [
            'startproject=flask_mico.cli:create_project'
        ]
    }
)
