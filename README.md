[![ru](docs/ru.svg)](docs/README.ru.md)
# Py_FSO (python file system object)

The main function of this package &mdash; is to process the contents of a folder with a single function: 
`` folder.process()'' (pun intended :-), without going into the details of iterating over files and folders.  

It's strange that python doesn't have such a built-in function, but maybe someone (maybe even myself) will write an extension to ``c`` someday.

So, if, for example, you need to find all files with a too long full name, you just need to write the following script:

```
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

```
Just one call to folder.process() will replace all the details of traversing the contents of the folder, allowing you to focus on the main action of the script.

The package also includes several useful functions for working with text files.

I use this package all the time in my work, installing it globally so that it's available to all scripts. It's very convenient.

## Getting Started

### Prerequisites

* [python](https://www.python.org/) (version  >=3+, version 2+ dosn't check)
* [pip](https://pypi.org/project/pip/) (version 16+)
* [Git](https://git-scm.com).

### Installing

```
# Clone the repository:
$ git clone https://github.com/JustMisha/py_fso.git myproject

# go to the project folder:
# cd myproject

# Install the package globally in development mode:
$ python -m pip install -e .

```

## Running the tests

```
# Go to the subfolder with the tests
$ cd test

# Run the tests
$ python -m unittest discover -v

# If you want to define the test coverage

# install coverage
$ python -m pip install coverage

$ python -m coverage run -m unittest discover -v
$ python -m coverage report html

# To see the coverage report simply open htmlcov/index.html
```

It's also possible to make the tests run before each commit (pre-commit hook). To do it, add parameter in your .git/config file core section
```
    hooksPath = .githooks
``` 
Or adjust your pre-commit according to the attached file in the .githooks folder.

## Contributing

Please send your suggestions, comments, and pull requests.

## Versioning

We use [SemVer](http://semver.org/) for versioning.

## Authors

* **Mikhail Trusov** - *py_fso* - [py_fso](https://github.com/JustMisha/py_fso)

See also the list of [contributors](https://github.com/JustMisha/py_fso/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

