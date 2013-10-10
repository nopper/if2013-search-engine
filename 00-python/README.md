# Requirements

Download and install [pyenv](https://github.com/yyuu/pyenv) a simple
Python Version Management script that let's you manage multiple
concurrent versions of python.

You should also install the
[pyenv-virtualenv](https://github.com/yyuu/pyenv-virtualenv) plugin that
let's you have control of virtual environments directly from the `pyenv`
script.

# Simple setup

You need to install the latest python `2.7.x` version which at the
current time is `2.7.5`.

    $ pyenv install 2.7.5
    ....

    $ pyenv version 2.7.5
    $ pyenv versions
      system
    * 2.7.5 (set by /Users/nopper/.pyenv/version)

After the installation you need to setup a virtual environment for your
demo:

    $ pyenv virtualenv 2.7.5 demo-2.7.5
    ...
    $ pyenv versions
      system
    * 2.7.5 (set by /Users/nopper/.pyenv/version)
      demo-2.7.5

To use your new virtual environment:

    $ pyenv shell demo-2.7.5
