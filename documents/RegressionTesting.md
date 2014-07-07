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

* https://docs.python.org/2/library/test.html


### Integration testing

[Integration testing](https://en.wikipedia.org/wiki/Integration_testing) consists in writting tests
that will check all your module works together.


### Continuous integration dashboards

To confirm that the update done to your code are not broking other platform or verion of python,
the test suite can automatically be run on build bot each time a update is pushed to your
repository. Then, the corresponding could be published to a dashboard.

## Hands On

Run through the *04-RegressionTesting.ipynb* notebook in the repository. You will be able to
adapt the example to work with your images. Save the updated notebook to disk.
