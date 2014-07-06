# Data Processing

Now that we have data in online sharing sites, we can start processing it. 
When processing, we want to keep the following best practices in mind:

* Avoid duplication of code: maximize re-use
* Keep track of the full state with version identifiers
* Make sure all analysis is tested
* Data, code, and documentation are coupled

The latter three topics are covered in further detail in the upcoming
sessions on revision control, regression testing, and literate programming.


## IPython Notebook

[![IPython Notebook](https://avatars1.githubusercontent.com/u/230453?s=140)](http://ipython.org/)

This is one of the best existing resources for reproducible research practices.

* Learn it !
* Love it !

When it becomes desireable to re-use code outside of the notebook, it is helpful
to incrementally refactor by creating classes or functions. These classes or functions
can be stored in python modules, and imported into the Notebook.

![No Copy Paste](http://www.madhavighare.com/wp-content/uploads/2010/09/Don_t-Copy-Paste-150x150.jpg)

There are few helpful functions for this type of rapid development. In Python 2,
the [reload]() built-in, and in Python 3,
[imp.reload](https://docs.python.org/3.0/library/imp.html#imp.reload) which
forces the interpreter to reload modules whose cached version is used by `import`
statements. Instead of manually calling these functions, there is also an
[autoreload](http://ipython.org/ipython-doc/dev/config/extensions/autoreload.html)
IPython magic,

<pre><code>
%load_ext autoreload
%autoreload 2
</code></pre>

## Hands On

Run through the *03-DataProcessing.ipynb* notebook in the repository. At the end of the notebook,
there is a simple exercise on code re-use. Explore analysis on your images or images of
nearby groups. Save the updated notebook to disk.
