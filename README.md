# tf-object-detection

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
pip install http://coda.cs.cmu.edu/~jaharkes/tf-object-detection-0.1.0.tar.gz[tf]
```

Or for tensorflow with GPU support,

```
pip install http://coda.cs.cmu.edu/~jaharkes/tf-object-detection-0.1.0.tar.gz[tf-gpu]
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
# Download and install all required dependencies required for the tensorflow
# object detection library to work correctly.
#
$ poetry install
```

To rebuild both sdist and wheels there is one issue. poetry-core 1.0.0 does not
handle combining modules from different locations, which is what we are trying
to do with the modules in the `tensorflow_models` subproject.  This is fixed by
[this patch](https://github.com/python-poetry/poetry-core/pull/108).


## What's in here

* `pyproject.toml`: The project configuration.
* `protoc_compile.py`: Helper script to compile protocol buffer wrappers.
* `tensorflow_models`: A git submodule pointing to the version of tensorflow object detection this thin wrapper is for.
