lockbox: User-friendly CLI over cryptography.io's Fernet symmetric cipher
=====================================================

.. image:: https://img.shields.io/badge/python-2.6%202.7%203.3%203.4%203.5%203.6-blue.svg
    :target: https://pypi.python.org/pypi/lockbox

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target: https://pypi.python.org/pypi/lockbox

---------------

.. image:: https://s3.amazonaws.com/johnwheeler/lockbox.gif

**lockbox** provides a command line interface over cryptography.io's `Fernet symmetric cipher <https://cryptography.io/en/latest/fernet/>`_.
Fernet guarantees that a message encrypted using it cannot be manipulated or read without the key. lockbox was inspired by the Ruby-based
`sekrets <https://github.com/ahoward/sekrets>`_ project, but they use different ciphers.

Installation
------------
``pip install lockbox``

Command line interface
----------------------

The ``write`` command
/////////////////////

.. code::

    Usage: lockbox lock [OPTIONS] INPUT OUTPUT

        Symmetric encryption of plaintext input file to ciphertext output file

    Options:
      --key TEXT  An encryption key
      --help      Show this message and exit.


The ``read`` command
////////////////////

.. code::

    Usage: lockbox unlock [OPTIONS] INPUT OUTPUT

      Symmetric decryption of ciphertext input file to plaintext output file

    Options:
      --key TEXT  An encryption key
      --help      Show this message and exit.


The ``edit`` command
////////////////////

.. code::

    Usage: lockbox edit [OPTIONS] PATH

      Decrypts the given file and opens its contents in a temporary file for
      editing. Once saved, the updated contents are reencrypted back to the
      orignal file.

    Options:
      --key TEXT  An encryption key
      --help      Show this message and exit.


The ``genkey`` command
//////////////////////

.. code::

    Usage: lockbox genkey [OPTIONS] OUTPUT

      Generates a cryptographically strong key and writes it to the given output
      path

    Options:
      --help  Show this message and exit.


Key resolution
--------------

With **lockbox**, you can pass an encryption key as a command line option ``--key`` or store the key in a ``.lockbox.key`` file.
The key should be `cryptographically strong <https://en.wikipedia.org/wiki/Password_strength#Guidelines_for_strong_passwords>`_. The command
line interface also has a command to generate such a key.

For all operations, lockbox uses the following algorithm to search for a key:

- A key passed via the ``--key`` option is always preferred.
- Otherwise the code looks for a companion key file named ``.lockbox.key`` in the the current working directory.
- If that is not found lockbox looks for the key in the environment under the environment variable ``LOCKBOX_KEY``
- Next the global key file is searched for. The path of this file is ``~/.lockbox.key``
- Finally, if no keys have been specified or found, the user is prompted to input the key. Prompt only occurs if the user is attached to a tty.
- You should **never** commit keyfiles. Add them to to your ``.gitignore`` or similar.
