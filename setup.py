from setuptools import setup, find_packages

setup(
    name='compiler',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'setuptools',
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
)
