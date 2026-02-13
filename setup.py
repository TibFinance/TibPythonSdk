from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='tib-finance',
    version='2.0.0',
    url="https://github.com/TibFinance/TibPythonSdk",
    author="TIB Finance",
    author_email="support@tib.finance",
    description="Python SDK for the TIB Finance payment processing API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    packages=find_packages(),
    install_requires=['pycryptodome', 'requests'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
)
