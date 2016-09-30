try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project', # Describe the project here
    'author': 'Douglas Melvin',
    'url': 'github.com/duggym122/<repo_path>', # Add the repository path here
    'download_url': 'https://github.com/duggym122/<repo_path>/archive/<version>.zip', # Add the repository path and version name here
    'version': '0.0.1',
    'install_requires': ['nose','coveralls','coverage~=4.2'], # Add additional requirements here AND in requirements.txt
    'packages': ['NAME'], # Add package names here
    'scripts': [],
    'name': 'python-project-skeleton' # Add project name here
}

setup(**config)