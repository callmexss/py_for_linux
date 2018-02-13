#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""""""""""""""""""""""""""""""""""""""""""""""
"      Filename: click_test1.py
"
"        Author: xss - callmexss@126.com
"   Description: ---
"        Create: 2018-02-14 01:29:44
"""""""""""""""""""""""""""""""""""""""""""""""
import click


@click.command()
@click.option('--pos', nargs=2, type=float)
def findme(pos):
    # click.echo('{} / {}'.format(pos[0], pos[1]))
    click.echo('{} / {}'.format(*pos))


if __name__ == '__main__':
    findme()
