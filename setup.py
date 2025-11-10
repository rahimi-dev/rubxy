from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="rubxy",
    author="Amirali Rahimi",
    author_email="amiralirahimi769@gmail.com",
    version="0.1.7",
    description="A Python library for interacting with the Rubika bot API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=("tests", )),
    include_package_data=True,
    python_requires=">=3.8",
    install_requires=["aiohttp"],
    license="GPL-3.0-or-later",
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    keywords=[
        "rubika",
        "rubxy",
        "bot",
        "robot"
    ],
)