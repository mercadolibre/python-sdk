from meli import __version__ as PACKAGE_VERSION
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='MELI-PYTHON-SDK',
    version=PACKAGE_VERSION,
    author='Mercadolibre',
    url='https://github.com/mercadolibre/python-sdk',
    packages=['meli'],
    include_package_data=True,
    description="MercadoLibre's Python SDK.",
    install_requires=[
        "requests>=2.0"
    ],
    test_suite='test',
)
