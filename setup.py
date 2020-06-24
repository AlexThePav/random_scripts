import scripts.main
import scripts.watch_downloads
from setuptools import setup, find_packages

INSTALL_REQUIRES = ['watchdog']

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="var_scripts",
    version="0.0.0",
    author="Alexandru Pavilcu",
    author_email="alexandrupavilcu@gmail.com",
    description="Small collection of scripts",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=INSTALL_REQUIRES,
    entry_points = {
        'console_scripts': ['watchdownloads=scripts.watch_downloads:run_watch_downloads'],
    }
)