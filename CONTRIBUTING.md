pysharedutils
=============

Contribution
------------

## Bugfixes and New Features
Before starting to tackle a bugfix or add a new feature, look for existing [issues](https://github.com/joeljames/py-shared-utils/issues) or create one a specific issue or feature request. This way you can avoid working on something that has already been addressed or is being worked on.

## Style Guide
pysharedutils aims to follow [PEP8](https://www.python.org/dev/peps/pep-0008/) including 4 space indents. When possible we try to stick to 79 character line limits.

## General Guidelines
* If possible avoid breaking backward changes.
* Write inline documentation for new classes and methods.
* Write tests and make sure they pass.
* Add improvements and bug fixes to docs/changelog.rst

## Workflow
Fork py-shared-utils on Github
``` bash
$ git clone https://github.com/joeljames/py-shared-utils.git
$ cd py-shared-utils
```
Install development requirements. It is highly recommended that you use a [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/), and activate the virtualenv before installing the requirements.
``` bash
$ pip install -r requirements.txt
```
Run tests with coverage.
``` bash
$ make unit_test
```
Run test Using Tox (Runs the tests in different supported python interpreter):
``` bash
$ tox
```

Run Lint:
``` bash
$ make lint
```

Create a new local branch to submit a pull request.
``` bash
$ git checkout -b name-of-feature
```

Commit your changes
``` bash
$ git commit -m "Detailed commit message"
$ git push origin name-of-feature
```

Submit a pull request. Before submitting a pull request, make sure pull request add the functionality, it is tested and docs are updated.
