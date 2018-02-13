#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""""""""""""""""""""""""""""""""""""""""""""""
"      Filename: click_test.py
"
"        Author: xss - callmexss@126.com
"   Description: A test for click 
"        Create: 2018-02-14 00:42:20
"""""""""""""""""""""""""""""""""""""""""""""""
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
