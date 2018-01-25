"""
A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages


setup(
    name='crqasoap',
    version='1.0.0',
    description='Chrome River QA Tools',
    long_description='Libraries with functionality needed to test soap apis at Chrome River.',
    url='https://github.com/Chrome-River/qa-soap-automation',
    author='Chrome River QA Team',
    license='Copyright @ ChromeRiver Technologies',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: Other/Proprietary License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='mercury controller development test',

    # Packages can be specified manually here if the project is simple.
    # Or use find_packages().
    # packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    # py_modules=['core'],
    packages=find_packages(),

    # Non Python files
    package_data={'': [
        'crqasoap/listener/*',
        'crqasoap/log/*',
        'crqasoap/master/*',
        'crqasoap/nodes/*',
        'crqasoap/properties/*',
        'crqasoap/requestxml/*',
        'crqasoap/service/*',
        'crqasoap/xmlparser/*'
    ]},
    include_package_data=True,

    # Dependencies.
    # These will be installed by pip when the project is installed.
    # For an analysis of "install_requires" vs pip's requirements files see:
    # https://packaging.python.org/en/latest/requirements.html

    # install_requires=['json'],
)
