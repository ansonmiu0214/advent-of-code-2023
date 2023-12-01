# _Multilingual_ Advent of Code 2023

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![C++](https://img.shields.io/badge/c++-%2300599C.svg?style=for-the-badge&logo=c%2B%2B&logoColor=white)

[**_Advent of Code_**](https://adventofcode.com/2023)
is a great opportunity to brush up on existing languages
and learn some new ones!

<p align="center">
<a href="#usage">Usage</a>
-
<a href="#directory-structure">Directory Structure</a>
-
<a href="#extending-language-support">Extending Language Support</a>
</p>

## Usage

```bash
$ ./run.sh
usage: ./run.sh LANGUAGE DAY PART INPUT_TYPE

arguments:
  LANGUAGE     the programming language
  DAY          the day of a problem, day{01..25}
  PART         the part of a problem, part{1,2}
  INPUT_TYPE   type of input file
```

```bash
$ ./dev.sh
usage: ./dev.sh LANGUAGE

arguments:
  LANGUAGE     the programming language
```

### Examples

Run the **Python** solution for **part 1** of **day 2**'s problem, using the **sample-1.in** input:

```bash
$ ./run.sh python day02 part1 sample-1
```

Open a development container for working on **C++** solutions:

```bash
$ ./dev.sh cpp
```

## Directory structure

| File / Directory         | Description                                 |
| ------------------------ | ------------------------------------------- |
| `data/dayXX/sample-1.in` | Sample input for part 1 of `dayXX`          |
| `data/dayXX/sample-2.in` | Sample input for part 2 of `dayXX`          |
| `data/dayXX/test.in`     | Test input for `dayXX`                      |
| `drivers/LANG`           | Build context and solution for `LANG`       |
| `dev.sh`                 | Multilingual development container launcher |
| `run.sh`                 | Multilingual solution dispatcher            |

## Extending language support

```bash
# 1.
# Create a driver subdirectory for the new language.
$ mkdir drivers/golang

# 2.
# Implement a Dockerfile with a base image for the new language,
# and sets '/workarea' as the WORKDIR.
$ cat drivers/golang/Dockerfile

# 3.
# Create an executable 'run.sh' file that expects to be invoked with
# './run.sh day{01..25} part{1..2} sample|test'.
$ cat drivers/golang/run.sh
```
