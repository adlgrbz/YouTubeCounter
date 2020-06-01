from os import path
from setuptools import setup
from yscounter import gui


here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="yscounter",
    version=gui.__version__,
    packages=["yscounter"],
    description="YouTube Subscriber Counter with Arduino and Python (Without API key)",
    long_description=long_description,
    url=gui.__source__,
    author=gui.__author__,
    author_email=gui.__contact__,
    platforms=["Linux"],
    classifiers=[
        "Operating System :: POSIX",
        "Environment :: Console",
        "Intended Audience :: End Users/Desktop",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
    keywords="youtube",
    install_requires=["asyncio", "aiohttp", "pyserial", "beautifulsoup4"],
    extras_require={":python_version == '2.7'": ["ino"]},
    package_data={"yscounter": ["data/*.*"], "yscounter": ["src/*.*"]},
    data_files=[
        ("share/icons", ["yscounter/data/icon.png"]),
        ("share/applications", ["yscounter.desktop"]),
    ],
    entry_points={"gui_scripts": ["yscounter = yscounter"]},
)
