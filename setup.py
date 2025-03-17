from setuptools import setup, find_packages

setup(
    name='sentinelsys',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'psutil',
        'matplotlib'
    ],
    package_data={"sentinelsys": ["*.py"]},
    description='Simple System Resource Monitor with Real-time Visualization',
    author="Arya Wiratama",
    author_email="aryawiratama2401@gmail.com",
    url="https://github.com/AryaWiratama26/sentinelsys",
    python_requires='>=3.10',

)