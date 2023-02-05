from setuptools import setup, find_packages

VERSION = '0.1.0'

DEPENDENCIES = [
    'fire==0.1.3',
    'flask-restful==0.3.7',
    'requests==2.21.0',
    'Babel==2.6.0',
    'boto3==1.9.246',
    'python-dotenv==0.18.0',
    'xlrd==1.2.0',
    'ipython==7.25.0',
    'numpy==1.21.1',
    'seaborn==0.11.1',
    'matplotlib==3.4.2',
    'scikit-learn==0.24.2',
    'Cython==0.29.24'
]

config = {
    'name': 'ids',
    'url': '',
    'version': VERSION,
    'packages': find_packages(exclude=['test*']),
    'entry_points': {
        'console_scripts': [
            'ids = ids.api:cli'
        ],
    },
    'install_requires': DEPENDENCIES,
}

setup(**config)
