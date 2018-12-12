from setuptools import setup, find_packages

import os
import versioneer

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='matplotlibhelper',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),

    description='Matplotlib Helper is my custom helper to tune Matplotlib experience.',
    long_description=long_description,

    url='https://github.com/kiwi0fruit/matplotlibhelper',

    author='Peter Zagubisalo',
    author_email='peter.zagubisalo@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],

    # keywords='sample setuptools development',
    packages=find_packages(exclude=['docs', 'tests']),

    install_requires=['numpy', 'pandas', 'ipython',
                      'sugartex>=0.1.10', 'matplotlib'],

    include_package_data=True,
    package_data={
        'matplotlibhelper': ['fonts/*'],
    },
)
