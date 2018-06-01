from vcmder.version import __version__
from setuptools import setup

setup(name='vcmder',
      version=__version__,
      description='Hashicorp Vault Mass Admin Tool.',
      url='http://github.com/Pashbee/vcmder',
      author='Pashbee',
      license='MIT',
      packages=['vcmder'],
      install_requires=['click', 'boto3', 'moto', 'progressbar2', 'pytest'],
      scripts=['bin/vcmder'],
      zip_safe=False)

