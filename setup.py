from setuptools import setup, find_packages

setup(
    name = "eazyAI",
    version = '1.1.6',
    packages = find_packages(),
    author = 'Puneet Dhankar , Naman Jain',
    author_email = "puneetd2005@gmail.com",
    description = 'A one function go library for Ski-Kit learn and TensorFlow AI/ML models build-in.',
    url = 'https://github.com/Self-nasu/eazyAI',
    install_requires=[
        'numpy',
        'pandas',
        'matplotlib',
        'tensorflow',
    ],
)