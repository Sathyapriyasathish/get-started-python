"""
Hello World app for running Python apps on Bluemix
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='python-hello-world-flask',
    version='1.0.0',
    description='Hello World app for running Python apps on Bluemix',
    long_description=long_description,
    url='https://github.com/IBM-Bluemix/python-hello-world-flask',
    license='Apache-2.0'
)
import random

number = random.randint(1, 9)

guess = 0

count = 0



while guess != number and guess != "exit":

    guess = input("What's your guess?")



    if guess == "exit":

        break



    guess = int(guess)

    count += 1



    if guess < number:

        print("Too low!")

    elif guess > number:

        print("Too high!")

    else:

        print("You got it!")

        print("And it only took you", count, "tries!")
 
