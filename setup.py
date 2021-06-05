from setuptools import setup
from setuptools import find_packages

setup(name='fasttext-langdetect',
      version='1.0.0',
      description='Language identification with fasttext',
      keywords=['fasttext', 'langdetect', 'language detection',
                'language identification'],
      long_description=open("README.md", "r", encoding='utf-8').read(),
      long_description_content_type="text/markdown",
      url='https://github.com/zafercavdar/fasttext-langdetect.git',
      download_url='https://github.com/zafercavdar/fasttext-langdetect/archive/refs/tags/v1.0.0.tar.gz',
      author='Zafer Cavdar',
      author_email='zafercavdar@yahoo.com',
      install_requires=['fasttext >= 0.9.1'],
      license='MIT',
      packages=find_packages(),
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'Topic :: Software Development :: Build Tools',
          'License :: MIT License',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
      ])
