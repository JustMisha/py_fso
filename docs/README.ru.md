[![en](en.svg)](../README.md)
# Py_FSO (python file system object)

Главная функция этого пакета &mdash; это обработка содержимого папки с помощью одной функции: ``` folder.process() ``` (получился каламбур :-), без погружения в детали итерации по файлам и папкам.  

Странно, что в python нет такой встроенной функции, но может кто-нибудь (может даже я сам) когда-нибудь напишет расширение на ```c```.

Итак, если, например, нужно найти все файлы со слишком длинным полным именем, вам достаточно написать следующий скирпт:

```
#!/usr/bin/python
# -*- coding: utf-8 -*-
""" Print  all files in /home/init/directory which have length more than MAX_FILEPATH_LENGTH """

from argparse import ArgumentParser
from py_fso import folder

MAX_FILEPATH_LENGTH = 260

def print_if_file_has_length_too_more_chars(fileEntry) :
    filePath = fileEntry.path
    fileLength = len(filePath)
    if fileLength > MAX_FILEPATH_LENGTH:
        print("Файл " + filePath + " has  length " + str(fileLength) + " chars")

parser = ArgumentParser(description='Scan a directory and its subdirectories and search for files with path lengths greater than ' + str(MAX_FILEPATH_LENGTH) + ' characters.')
parser.add_argument("directory", help="scan this directory with its subdirectories", metavar="DIR")
parser.add_argument("-m", "--max_filepath_length", help="max filepath's length")
args = parser.parse_args()
if args.max_filepath_length:
    MAX_FILEPATH_LENGTH = int(args.max_filepath_length)

folder.process(init_dir = args.directory, proc_file_function = print_if_file_has_length_too_more_chars, process_dirs = False, proc_dir_function = '', go_into_subdirs = True)

```

Только один вызов функции folder.process() заменит все детали обхода содержимого папки, позволив вам сосредоточится на главном действии скрипта.

Также пакет включает несколько полезных функций для работы с текстовыми файлами.

Я в своей работе использую этот пакет постоянно, установив его глобально, чтобы он был доступен для всех скриптов. Очень удобно.

## Локальное развертывание

### Предварительные условия

Для работы вам нужен:

* [python](https://www.python.org/) (version  >=3+, version 2+ dosn't check)
* [pip](https://pypi.org/project/pip/) (version 16+)
* [Git](https://git-scm.com).


### Установка

```
# Клонируем репозитарий:
$ git clone https://github.com/JustMisha/py_fso.git myproject

# Переходим в папку проекта:
$ cd myproject

# Устанавлимваем пакет глобально в режиме разработки:
$ python -m pip install -e .

```

## Тестирование

```
# Переходим в подпапку с тестами
$ cd test

# Запускаем тесты
$ python -m unittest discover -v

# Если нужно определить тестовое покрытие

# устанавливаем пакет coverage
$ python -m pip install coverage

$ python -m coverage run -m unittest discover -v
$ python -m coverage report html

# Чтобы посмотреть отчет о покрытии достаточно открыть htmlcov/index.html
```

Также можно подключить выполнение тестов перед кажым коммитом (pre-commit hook). Для этого в локальный файл конфигурации git в раздел core добавьте параметр в конфигурационный файл репозитория (.git/config) в секцию  core:
```
    hooksPath = .githooks
``` 
или откорректируйте свой pre-commit в соответствии с прилагаемым файлом в папке .githooks.


## Участие

Пожалуйста, присылайте свои предложения, замечания и pull requests.

## Версии

Для обозначения версий используется [SemVer](http://semver.org/).

## Автор

* **Михаил Трусов** - *py_fso* - [py_fso](https://github.com/JustMisha/py_fso)

См. также [участники](https://github.com/JustMisha/py_fso/contributors).

## Лицензия

Данный пакет лицензируется на условиях MIT Лицензии - смотри подробности [LICENSE.md](../LICENSE.md).

