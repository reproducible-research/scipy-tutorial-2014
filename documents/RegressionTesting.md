# Regression Testing

## Overview

In the [DataProcessing](DataProcessing.md) section, we experimented and created some
awesome code to download, display, process and extract features from the _Saltritus_ 
image.

### Unit tests

To ensure that improvement made to our code or even updates in the computing environment
are not changing the expected results of each one of your modules, we will see how to
write basic [unit tests](https://en.wikipedia.org/wiki/Unit_testing#Benefits).

More details:

* [https://docs.python.org/2/library/test.html](https://docs.python.org/2/library/test.html)


### Integration testing

[Integration testing](https://en.wikipedia.org/wiki/Integration_testing) consists in writting tests
that will check all your modules can work together.


### Continuous integration dashboards

To confirm that your commits are not causing failure on other platform or when executed using
different version of python, the test suite can automatically be run on a _build bot_ each time
an update is pushed to your repository.

The [Travis CI](https://travis-ci.org/) platform provides a very convenient solution to trigger a build/test cycle each
time a change is pushed on your GitHub repository.

For example: [https://travis-ci.org/girder/girder](https://travis-ci.org/girder/girder)


Then, the associated results could be published on a dashboard.

For example:

* [http://open.cdash.org/index.php?project=CPython](http://open.cdash.org/index.php?project=CPython)
* [http://my.cdash.org/index.php?project=girder](http://my.cdash.org/index.php?project=girder)

## Hands On

Run through the *04-RegressionTesting.ipynb* notebook in the repository. You will be able to
adapt the example to work with your images. Save the updated notebook to disk.
