
from setuptools import setup,find_packages

setup(
  project_name = 'AQI prediction',
  version = '0.0.1',
  author = 'shivam',
  author_email = 'shivam4806@gmail.com',
  package_dir = {'':'src'},
  packages = find_packages(where = 'src'),
  install_requires = [
    'pandas',
    'numpy',
    'matplotlib',
    'seaborn',
    'scikit-learn'
  ]

) 
