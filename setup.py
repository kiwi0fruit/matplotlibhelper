from setuptools import setup, find_packages
import io
import os
import versioneer

here = os.path.abspath(os.path.dirname(__file__))
with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='matplotlibhelper',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),

    description='Matplotlib Helper is my custom helper to tune Matplotlib experience in Atom/Hydrogen and Pandoctools/Knitty.',
    long_description=long_description,
    long_description_content_type="text/markdown",

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
        'Programming Language :: Python :: 3.6',
    ],

    # keywords='sample setuptools development',
    packages=find_packages(exclude=['docs', 'tests']),
    python_requires='>=3.6',
    install_requires=['numpy', 'pandas', 'ipython',
                      'sugartex>=0.1.16', 'matplotlib'],

    include_package_data=True,
    package_data={
        'matplotlibhelper': ['fonts/*'],
    },
)
