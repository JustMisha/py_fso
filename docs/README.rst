
The main function of this small package is to process the contents of a
folder with a single function: ``folder.process()`` (pun intended
:-), without going into the details of iterating over files and folders.

It's strange that python doesn't have such a built-in function, but
maybe someone (maybe even myself) will write an extension to ``c``
someday.

So, if, for example, you need to find all files with a too long full
name, you just need to write the following script:

::

   from argparse import ArgumentParser
   from py_fso import folder

   MAX_FILEPATH_LENGTH = 260

   def print_if_file_has_length_too_more_chars(fileEntry) :
       filePath = fileEntry.path
       fileLength = len(filePath)
       if fileLength > MAX_FILEPATH_LENGTH:
           print("File " + filePath + " has  length " + str(fileLength) + " chars")

   parser = ArgumentParser(description='Scan a directory and its subdirectories and search for files with path lengths greater than ' + str(MAX_FILEPATH_LENGTH) + ' characters.')
   parser.add_argument("directory", help="scan this directory with its subdirectories", metavar="DIR")
   parser.add_argument("-m", "--max_filepath_length", help="max filepath's length")
   args = parser.parse_args()
   if args.max_filepath_length:
       MAX_FILEPATH_LENGTH = int(args.max_filepath_length)

   folder.process(init_dir = args.directory, proc_file_function = print_if_file_has_length_too_more_chars, process_dirs = False, proc_dir_function = '', go_into_subdirs = True)

Just one call to folder.process() will replace all the details of traversing the contents of the folder, allowing you to focus on the main action of the script.

I use this package all the time in my work, installing it globally so that it's available to all scripts. It's very convenient.

Getting Started
---------------

Prerequisites
~~~~~~~~~~~~~

-  `python <https://www.python.org/>`__ (version >=3+, version 2+ dosn't
   check)


Installing
~~~~~~~~~~

::

    # Just install the package globally (recommended)
    # so you can use in all your scripts and projects:
    $ python -m pip install py_fso

Using
~~~~~~~~~~

::

    # then you can use it in your scripts
    from py_fso import folder
    from py_fso import textfile

Versioning
----------

Using `SemVer <http://semver.org/>`__ for versioning.

Authors
-------

-  **Mikhail Trusov** -
   `py_fso <https://github.com/JustMisha/py_fso>`__

License
-------

This project is licensed under the MIT License - see the `LICENSE.md <https://github.com/JustMisha/py_fso/blob/main/LICENSE.md>`__ file for details