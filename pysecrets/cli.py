import os
import subprocess
from tempfile import NamedTemporaryFile

import click

import pysecrets


@click.group()
def cli():
    pass


@cli.command(help="Symmetric encryption of plaintext input file to ciphertext output file")
@click.argument('input', type=click.File())
@click.argument('output', type=click.File('w'))
@click.option('--key', help="An encryption key")
def write(input, output, key):
    key = _resolve_key(key)

    try:
        ciphertext = pysecrets.encrypt(input.read(), key)
    except pysecrets.SecretsException as ex:
        click.echo(ex, err=True)
        return

    output.write(ciphertext)


@cli.command(help="Symmetric decryption of ciphertext input file to plaintext output file")
@click.argument('input', type=click.File())
@click.argument('output', type=click.File('w'))
@click.option('--key', help="An encryption key")
def read(input, output, key):
    key = _resolve_key(key)

    try:
        plaintext = pysecrets.decrypt(input.read(), key)
    except pysecrets.SecretsException as ex:
        click.echo(ex, err=True)
        return

    output.write(plaintext)


@cli.command(help="Decrypts the given file and opens its contents in a temporary file for editing. "
             + "Once saved, the updated contents are reencrypted back to the orignal file.")
@click.argument('path', type=click.Path())
@click.option('--key', help="An encryption key")
def edit(path, key):
    key = _resolve_key(key)
    with NamedTemporaryFile() as tmpfile:
        try:
            if os.path.isfile(path):
                with open(path) as f:
                    ciphertext = f.read()
                    plaintext = pysecrets.decrypt(ciphertext, key)
                    tmpfile.write(plaintext.encode('utf-8'))
                    tmpfile.flush()

            editor = os.getenv('EDITOR', 'vim')
            subprocess.call([editor, tmpfile.name])
            tmpfile.seek(0)
            plaintext = tmpfile.read().decode('utf-8')
            ciphertext = pysecrets.encrypt(plaintext, key)

            with open(path, 'w') as f:
                f.write(ciphertext)
        except pysecrets.SecretsException as ex:
            click.echo(ex, err=True)


@cli.command(help="Generates a cryptographically strong key and writes it to the given output path")
@click.argument('output', type=click.File('w'))
def genkey(output):
    key = pysecrets.genkey()

    if os.path.isfile(output.name):
        click.echo(
            "Key already exists at {}. Will not overwrite existing key.".format(output.name))
        return

    output.write(key)

    click.echo('Key has been written to {}'.format(output.name))


def _resolve_key(key):
    key = pysecrets.resolve_key(key)

    if key is None:
        key = click.prompt(text='Key', hide_input=True)

    return key


if __name__ == '__main__':
    cli()
