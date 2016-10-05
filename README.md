# Python tool selection

Will determine which Python version to use to invoke a given tool,
depending on the contents of a ``runtime.txt`` file.

The main reason is to be able to quickly switch between Python 2 and 3
flake8 in editors.


## Usage

Clone the repo somewhere, symlink ``pytoolselect.py`` somewhere in
your path.

Example:

    git clone https://github.com/rshk/pytoolselect ~/Projects/pytoolselect

    # If you haven't already, put this in your shell configuration
    PATH="${HOME}/bin:${PATH}"

    mkdir -p ~/bin
    ln -s ~/Projects/pytoolselect/pytoolselect.py ~/bin/flake8

Then, in your project root, specify the runtime you want to use:

    echo python-2.7 > runtime.txt

or

    echo python-3.5 > runtime.txt

(If no ``runtime.txt`` is found at filesystem boundary, then will
default using python3).

Of course, you can create symlinks for all the tools you want.


## Caveats

- Only works for tools that can be invoked via ``python -m <name>``
  (for now..)

- Only supports switching based on Python major version (do we need
  more granularity?)

- The ``runtime.txt`` thing is quite Heroku-specific, might be worth
  to allow configuring it some way in the future.. (git config maybe?)
