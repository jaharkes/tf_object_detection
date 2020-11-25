import os
import setuptools

from protoc_compile import build
build()

file_dir = os.path.dirname(os.path.realpath(__file__))
with open(os.path.join(file_dir, "README.md")) as f:
    long_description = f.read()

install_requires = [
    "setuptools>=41.0.0",  # tensorboard requirements
    "contextlib2",
    "Cython",
    "lxml",
    "matplotlib",
    "Pillow",
    "protobuf",
    "protoc-wheel-0",
    # replacement for pycocotools, as the published pypi package fails on cython and numpy dependencies
    "pycocotools-fix",
]

extras_require = {
    'tf': ['tensorflow<2.0'],
    'tf-gpu': ['tensorflow-gpu<2.0'],
}

setuptools.setup(
    name='tf_object_detection',
    version='0.0.3',
    author='Junjue Wang',
    author_email='junjuew@cs.cmu.edu',
    description='A Thin Wrapper around Tensorflow Object Detection API for Easy Installation and Use',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/junjuew/tf_object_detection',
    packages=setuptools.find_packages(
        where="tensorflow_models/research",
        include=["object_detection", "object_detection.*"],
    )
    + setuptools.find_packages(where="tensorflow_models/research/slim"),
    package_dir={
        '': 'tensorflow_models/research/slim',  # tf slim dependencies
        'object_detection': 'tensorflow_models/research/object_detection'},
    license='Apache License 2.0',
    install_requires=install_requires,
    extras_require=extras_require,
    python_requires='>=3.6, <4.0',  # matplotlib >3.1 requires python >=3.6
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
    ]
)
