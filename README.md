# Chapter 0

## [use ssh connection to github](https://help.github.com/articles/connecting-to-github-with-ssh/)
```sh
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
# start the ssh-agent in the background
eval $(ssh-agent -s)
ssh-add ~/.ssh/id_rsa
```
If still need to input the username and password:
from [SF](https://segmentfault.com/q/1010000000599327)
```sh
git remote remove origin
git remote add origin git@github.com:Username/Your_Repo_Name.git
git branch --set-upstream-to=origin/master master
```

## vim open and edit more than one file
```sh
# from terminal
vim file1 file2 file3 ...

# from vim
:o filename

# show many files
:split
:vsplit

# handle different files
ctrl + 6 # next file
:bn # next
:bp # last 

ctrl + w + up/down/left/right
ctrl + w + j/k/h/l # same as last one
ctrl + ww # next

```


# Chapter 1

## why python?
Life is short, use python!

## py2 or py3
BOTH. IT'S NOT SO HARD TO WRITE CODE BOTH WORK UNDER THE VERSION 2 AND 3. 


# Chapter 2

## small tools

### http server
```sh
python -m SimpleHTTPServer # for python 2
python -m http.server # for python 3
```

### string2json
`json style string | python -m json.tool`

### check the validity of third party package 
`python -c "import paramiko"`

## pip

### change pip source
for linux
```sh
cd ~ && mkdir .pip
vim pip.conf
# content
# [global]
# index-url = https://pypi.douban.com/simple/
```
for windows
```sh
# path is %APPDATA as pip\pip.ini
# content is same to before
```

### download package and deploy locally
```sh
# new method, the old '--download' way will be deprecated in the future
pip download package_name --trusted-host mirrors.aliyun.com
```

### pipenv
> Pipenv is a dependency manager for Python projects. 

Use `pip` to install Pipenv:
```sh
pip install --user pipenv

# installing packages for your project
cd myproject
pipenv install requests
``` 


## python Editor
vim of course   
some plugs:
1. snipmate
2. syntastic
3. jedi-vim
```sh
pip install jedi
```

interactive ways:
1. ipython   
```sh
  # magic method: start with %  
  %lsmagic # show all the magic method
```
2. notebook 
```sh 
  jupyter notebook --no-browser --ip=0.0.0.0 --allow-root
```

## python debug tools
pdb and ipdb   
usage:
```sh
python -m pdb test_pdb.py
```

or 

```python
# filename: test.py
improt pdb

# some codes
pdb.set_trace()
# some codes
```
save and exit. than `python test.py` and it will start debug at breakpoint

## python coding standard

### for check: pycodestyle(pep8)

install:   
```sh
pip install pycodestyle
``` 

usage:   
```
pycodestyle *.py
```

optional arguments:
```
--first: show check information
--show-source --show-pep8: with the informal parts print
```

### for modify: autopep8
install:
```sh 
pip install autopep8
```

usage:
```sh 
autopep8 *.py # print the modification without change the original file
```

optional:
```sh
--in-place: equals `-i` modify in the original file
```

## python workplace management

### pyenv: manage different kinds of python interpretation
install(from github):   
TODO:    

usage:
```sh
pyenv --help # show help information
pyenv install --list # show available versions
pyenv install -v version_num(eg.3.6.0, 2.7.13) # install specific version of python
pyenv versions # show current installed python versions
pyenv global version_num # activate specific python version
pyenv uninstall version_num # uninstall specific version of python 
```

### virtualenv: manage different workplace of python
TODO:   

---
# Chapter 3

## pertain command line python features

### sys
```
sys.argv: the arguments list
sys.stdin: standard input stream
sys.stdout: standard ouput stream
sys.stderr: standard error stream
```
### fileinput
fileinput.input(): input from a specific file

### getpass
```
getpass.getuser(): get username
getpass.getpass(): get password
```

## parse config files
```python
import configparser


cf = configparser.configparser(allow_no_value=True)
cf.read("my.cnf")
...
```

## parse command line arguments
```python
from __future__ import print_function
import argparse


def _argparse():
    parser = argparse.ArgumentParser(description="This is a description")
    parser.add_argument('--host', action='store',
                        dest='server', default='localhost', help='connect to host')
    parser.add_argument('-t', action='store_true',
                        default=False, dest='boolean_switch', help='Set a switch to true')
    return parser.parse_args()


def main():
    parser = _argparse()
    print(parser)
    print('host =', parser.server)
    print('boolean_switch =', parser.boolean_switch)


if __name__ == '__main__':
    main()
```

## use click to parse command line argument
```python
import click


@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='your name',
              help='The person to greet.')
def hello(count, name):
    '''Simple program that greets NAME for a total of COUNT times.'''
    for x in range(count):
        click.echo('Hello {}!'.format(name))


if __name__ == '__main__':
    hello()
```
