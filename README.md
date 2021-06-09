<!--
SPDX-FileCopyrightText: 2020-2021 Carnegie Mellon University

SPDX-License-Identifier: Apache-2.0
-->

# tf_object_detection

This is a thin wrapper around the [Tensorflow Object Detection API] for easy
installation and use. The original [installation procedure] contains multiple
manual steps that make dependency management difficult. This repository creates
a pip package that automate the installation so that you can install the API
with a single pip install.

[Tensorflow Object Detection API]:
    https://github.com/tensorflow/models/tree/v1.13.0/research/object_detection
[installation procedure]:
    https://github.com/tensorflow/models/blob/v1.13.0/research/object_detection/g3doc/installation.md


## Installation

```
pip install tf-object-detection[tf]
```

Or for tensorflow with GPU support,

```
pip install tf-object-detection[tf-gpu]
```


## Usage

All the scripts from tensorflow object detection APIs work out-of-box.
You can find an example usages from the API's [model_main.py].

```
import object_detection
```

[model_main.py]:
    https://github.com/tensorflow/models/blob/v1.13.0/research/object_detection/model_main.py


## Build from repository

```bash
#
# install [poetry](https://python-poetry.org)
#
# Download and setup all required dependencies required for tensorflow object
# detection library to work correctly.
#
$ poetry install
```

To rebuild the sdist and wheels, there are 2 issues to work around.

  - Poetry does not handle combining modules from different locations, which is
    what we are trying to do with the modules in the `tensorflow_models`
    subproject.  This is fixed by the following patch which hopefully will get
    merged in poetry-core,
        https://github.com/python-poetry/poetry-core/pull/108

  - The build depends on the protobuf compiler which is installed with the
    protoc-wheel-0 dev-dependency. However this means that `poetry build` has
    to run from within the development virtualenv that was set up with
    `poetry install`. So build will only work if run as `poetry run poetry build`.


## What's in here

* `pyproject.toml`: The project configuration.
* `protoc_compile.py`: Helper script to compile protocol buffer wrappers.
* `tensorflow_models`: A git submodule pointing to the version of tensorflow object detection this thin wrapper is for.
