from setuptools import setup, find_packages

setup(
    name="gsoc25_py_jderobot",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "numpy==1.21.5",       
        "matplotlib==3.5.1",    
    ],
    author="Muhtasim Redwan",
)