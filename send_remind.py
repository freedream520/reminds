# -*- coding:utf-8 -*-
from __future__ import unicode_literals
import click
from mailer import send_email

@click.command()
@click.argument('to')
@click.argument('text')
@click.argument('id')
def main(to, text, id):
    send_email(to, 'Date Remind', text)

if __name__ == '__main__':
    main()
