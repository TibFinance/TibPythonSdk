from setuptools import setup, find_packages

with open("README-BETA.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='tib-finance',
    version='3.1.0b2',
    url="https://github.com/TibFinance/TibPythonSdk",
    author="TIB Finance",
    author_email="support@tib.finance",
    description="Beta of the Python SDK for the TIB Finance payment processing API, for the sandbox only",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    packages=find_packages(),
    python_requires='>=3.8',
    install_requires=['pycryptodome', 'requests'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
)
