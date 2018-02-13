#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""""""""""""""""""""""""""""""""""""""""""""""
"      Filename: click_test2.py
"
"        Author: xss - callmexss@126.com
"   Description: ---
"        Create: 2018-02-14 01:36:18
"""""""""""""""""""""""""""""""""""""""""""""""
import click
import codecs


@click.command()
@click.option('--password', prompt=True, hide_input=True,
              confirmation_prompt=True)
def encrypt(password):
    click.echo('Encrypting password to {}'.format(
        codecs.encode(password, 'rot13')))


if __name__ == '__main__':
    encrypt()
