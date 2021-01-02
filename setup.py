from setuptools import find_packages, setup
setup(
    name='stairs_lib',
    packages=find_packages(include=['stairs_lib']),
    version='0.1.0',
    description='ws2812B library for stairs',
    author='Me',
    license='MIT',
    install_requires=['numpy'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)