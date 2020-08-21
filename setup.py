# coding: utf-8

"""
    MELI Markeplace SDK
    This is the official Python SDK for the MercadoLibre Marketplace platform.  # noqa: E501
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "meli"
VERSION = "3.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.25.6", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="MELI Markeplace SDK",
    author="Mercado Libre",
    author_email="",
    url="",
    keywords=["Mercado Libre", "API", "MELI Markeplace SDK"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""\
    This is the official Python SDK for the MercadoLibre Marketplace platform.  # noqa: E501
    """
)
