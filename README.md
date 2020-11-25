# tf_object_detection [![PyPI version][pypi-image]][pypi] [![Build Status][travis-image]][travis]

[travis-image]: https://travis-ci.org/junjuew/tf_object_detection.svg?branch=master
[travis]: http://travis-ci.org/junjuew/tf_object_detection

[pypi-image]: https://badge.fury.io/py/tf-object-detection.svg
[pypi]: https://pypi.org/project/tf-object-detection/

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


## What's in here

* [setup.py](setup.py): The python packaging script.

```bash
# Download and setup all required dependencies required for tensorflow object 
# detection libarary to work correctly.
$ python setup.py install
```

* `protoc_compile.py`: Helper script to compile protocol buffer wrappers.
* `tensorflow_models`: A git submodule pointing to the version of tensorflow object detection this thin wrapper is for.
