from setuptools import setup

setup(
    name='mirror',
    version='0.1.0',
    packages=['mirror'],
    entry_points={
        'console_scripts': [
            'mirror = mirror.__main__:main'
        ]
    }
)