from setuptools import find_packages, setup

setup(
    name="luneth_engine",
    version="1.0.0",
    packages=find_packages(),
    python_requires=">=3.12",
    description="A lightweight pure Python game engine",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Ido-Badash/luneth_engine",
    author="Ido Badash",
    author_email="idoba12012011@gmail.com",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
