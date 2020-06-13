from setuptools import find_packages, setup

setup(
    name="flask_mico",
    version="0.1.1",
    description="flask mico",
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
            'startporject=flask_mico.cli:create_project'
        ]
    }
)
