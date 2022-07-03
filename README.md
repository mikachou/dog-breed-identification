# Overview

The purpose of this program is to predict the breed of a dog from a picture entered as argument

# Requirements

Python-3.7.13

The following install procedure requires `pyenv` and its plugin `pyenv-virtualenv`
* pyenv : https://github.com/pyenv/pyenv
* pyenv-virtualenv : https://github.com/pyenv/pyenv-virtualenv

# Install

1. Clone the repository

```
$ git clone https://github.com/mikachou/dog-breed-identification
```

Then enter in folder

```
$ cd dog-breed-identification
```

2. Install right python version :

```
$ pyenv local $(cat .python-version)
```

You may check that you have installed the right python version
```
$ python -V
Python 3.7.13
```

Create a virtualenv for this project

```
$ pyenv virtualenv dogs-cli
```

Enter in virtualenv

```
$ pyenv shell dogs-cli
```

3. Install required packages

```
$ pip install -r requirements.txt
```

# How to use

Call the script with `python` command and pass an image filepath as argument.

You may use examples left in `imgs/` directory.

For example :

```
$ python app.py imgs/beethoven.jpg
```

Final result should be :
```
Saint Bernard | score = 0.99720997
```