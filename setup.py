from setuptools import setup

setup(name='djangogeo',
      version='1.0',
      description='OpenShift DjangoGeo',
      author='Ale',
      author_email='dev@trincatornidor.com',
      url='http://www.python.org/sigs/distutils-sig/',
      install_requires=['Django>=1.8,<1.9'],
      dependency_links=['https://pypi.python.org/simple/django'],
)

