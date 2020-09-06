from setuptools import find_packages, setup

setup(
    name='notes',
    version='1.0.0',
    packages=['notes'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
    python_requires='>=3.6',
)