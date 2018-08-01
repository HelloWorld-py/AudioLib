from setuptools import setup

setup(name='pysounds',
      version='1.0',
      description='A high level sounds api for python',
      url='https://github.com/HelloWorld-py/PySounds',
      author='Jacob Tsekrekos',
      author_email='jdtsekrekos@live.com',
      install_requires=['pyaudio'],
      packages=['pysounds', 'pysounds/pyaudio'])
