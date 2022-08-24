from setuptools import setup, find_packages

long_description = 'Random Typing - most commonly used with timeit. Read the documentation at https://github.com/nayakrujul/typing-tools/'

setup(
  name = 'random-typing',
  version = '0.1',
  license='Apache',
  description = 'Random Typing',
  author = 'Rujul Nayak',
  author_email = 'rujulnayak@outlook.com',
  url = 'https://github.com/nayakrujul/typing-tools',
  download_url = 'https://github.com/nayakrujul/typing-tools/archive/refs/tags/v_01.tar.gz',
  keywords = ['random', 'typing', 'tools'],
  install_requires=[
      ],
  classifiers=[
    'Development Status :: 3 - Alpha', 
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
  long_description=long_description,
  long_description_content_type='text/x-rst',
  packages = find_packages()
)
