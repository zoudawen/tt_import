# from distutils.core import setup
from setuptools import setup, find_packages
import fun
import unittest


setup(name=covertutils.__name__,
      version="1.0"
      description='test',
      url="https://github.com/zoudawen/tt_import/",
      author="dzou",
      author_email="dz@gmail.com",
      license='MIT',
      packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
	  )