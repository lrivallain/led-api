from distutils.core import setup
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='led_api',
    version='1.0.0',
    author="Ludovic Rivallain",
    author_email='ludovic.rivallain+ledapi -> gmail.com',
    packages=setuptools.find_packages(),
    description=
    "A simple API to remote control some LEDs through a GPIO module.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        "flask-restplus",  # API provider
        "gpiozero",        # GPIO interface
        "RPi.GPIO",        # GPIO interface
        "coloredlogs",     # fancy logs
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'led-api=led_api.__main__:main'
        ],
    })
