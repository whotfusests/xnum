from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="xnum",
    version="4.0",
    author="whotfusests",
    description="Encryption module for Python with /x64/ like encrypt lines and complete gibberish encryption.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/whotfusests/xnum",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[],
    extras_require={
        'dev': [
            'pytest>=6.0',
            'twine>=3.0',
        ],
    },
)