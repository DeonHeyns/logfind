try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description':
        'The logfind tool is designed to find all the log files that have at least one instance of some text',
    'author': 'Deon Heyns',
    'url': 'https://github.com/DeonHeyns/logfind',
    'download_url': 'https://github.com/DeonHeyns/logfind',
    'author_email': 'deon@deonheyns.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['logfind'],
    'scripts': [],
    'name': 'logfind',
    'entry_points': {
        'console_scripts': [
            'logfind = logfind.__main__:main',
        ]
    }
}

setup(**config)
