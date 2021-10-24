#!/usr/bin/env python3
import os
import sys
import jinja2
import click


@click.command()
@click.argument('args', nargs=-1)
@click.option('--input_file', type=click.File('r'), default=sys.stdin)
@click.option('--output_file', type=click.File('w'), default=sys.stdout)
def render(args, input_file, output_file):
    """
    Construct Template object from env var
    Render to output file
    """
    env = jinja2.Environment()
    with input_file:
        template = env.from_string(input_file.read())

    content = template.render({
        'env': os.environ,
        **dict(arg.split('=', 1) for arg in args),
    })

    with output_file:
        output_file.write(content)


if __name__ == '__main__':
    render(auto_envvar_prefix='JINJA')
