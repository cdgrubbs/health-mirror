from setuptools import setup

setup(
    name='mirror',
    version='0.1.0',
    packages=['mirror'],
    entry_points={
        'console_scripts': [
            'mirror = mirror.__main__:main'
        ]
    },
    install_requires=[
        'pyqt5==5.14.1',
        'SpeechRecognition==3.8.1',
        'PyAudio==0.2.11',
        'requests==2.23.0',
    ],
)