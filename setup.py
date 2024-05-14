from setuptools import setup, find_packages

setup(
    name = "easyAI",
    version = '0.1',
    packages = find_packages(),
    author = 'Puneet Dhankar',
    author_email = "puneetd2005@gmail.com",
    description = 'A one function go library for Ski-Kit learn and TensorFlow AI/ML models build-in.',
    url = 'https://github.com/self-Puneet/easyAI',
    install_requires=[
        'numpy',
        'pandas',
        'matplotlib' 
    ],
)