from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as file:
    long_des = file.read()

setup(
    name='sentinelsys',
    version='1.1',
    packages=find_packages(),
    install_requires=[
        'psutil',
        'matplotlib'
    ],
    package_data={"sentinelsys": ["*.py"]},
    description='Simple System Resource Monitor with Real-time Visualization',
    long_description=long_des,
    long_description_content_type="text/markdown",
    author="Arya Wiratama",
    author_email="aryawiratama2401@gmail.com",
    python_requires='>=3.10',
)