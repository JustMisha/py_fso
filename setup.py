from setuptools import setup

setup(
    name='py_fso',
    version='1.0.8',
    description='The Python package for working with dirs and files',
    long_description=open('docs/README.rst', 'r').read(),
    long_description_content_type="text/x-rst",
    url='https://github.com/JustMisha/py_fso',
    author='Mikhail Trusov',
    author_email='admin@superprogrammist.ru',
    license='MIT',
    packages=['py_fso'],
    package_dir={'': 'src'},
    install_requires=[],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: System :: Filesystems',
        'Topic :: Utilities',
    ],
)