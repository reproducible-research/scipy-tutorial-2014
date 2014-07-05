# Agenda

[TOC]


## 8:00 am First Session

### Getting Started

* Get acquainted and verify preparations (5 min) - Matt
    * Say *Hi!* to the instructors
    * Introduce yourself to the person sitting next to you, they will be your
  partner
    * Recall successfully completing the [preparation](Preparation.md) tasks

### Introduction

* History of scientific societies and publications (10 min) - Luis
    * [Reproducible Research](http://reproducible-research.github.io/Reproducible-Research-Part-I/)
    * [Leeuwenhoek](http://en.wikipedia.org/wiki/Antonie_van_Leeuwenhoek) was The Man!
    * [The Invisible College](http://en.wikipedia.org/wiki/Invisible_College)
    * [Nullius in Verba](https://royalsociety.org/about-us/history/)

### Data Acquisition

* [Image Acquisition](DataAcquisition.md) (25 min) - Matt

* Replication of the early microscope experiments by Antonie Leeuwenhoek
    * Cell camera phone microscope
    * With drop of interesting water
    * *Hands on:* each pair acquires images

### Data Sharing

[Data Sharing](DataSharing.md) - (20 min) - Luis

* Image gathering, storage, and sharing (10 min)
    * Figshare (www.figshare.com)
    * MIDAS (www.midasplatform.com)
    * Girder (http://girder.readthedocs.org/en/latest)
    * *Hands on:* Upload the images
* Download data via RESTful API (10 min)
    * REST download via Python standard library
    * Checksum verification
    * *Hands on:* Download the data via HTTP


## 9:00 am Second Session

### Reproducible Computational Environment

[Computational Environment](ComputationalEnvironment.md) (20min) - Aashish

* Reproducible computational environment
    * Docker
    * Package versioning
    * Virtual Machines
    * Cloud services
* *Hands on:*
    * Create a Docker image and container
    * Run our tutorial package verification script
    * Upload your Docker image to DockerHub

### Revision Control

Revision Control with Git (20min) - Steve

* Software versioning, collaboration, and citation
    * Keeping track of changes
    * Unique hashes
    * DOI
* *Hands on:*
    * Create a branch
    * Make a commit
    * Push the branch
    * [Create a citable version](https://guides.github.com/activities/citable-code/)

### Developing Reproducible Scripts and Code

[IPython Notebook, Scripts, and SimpleITK](DataProcessing.md) (20min) - Matt

* Reproducible code development
    * IPython Notebook to combine notes, code, and results
    * Avoid duplication with re-usable modules
* *Hands on:*
    * Run analysis on new data
    * Generate histogram for the data


## 10:00 am Break (15min)


## 10:15 am Third Session

### Regression Testing

Regression Testing (30min) - Jc

* Quality code development with regression tests
    * Testing code hypothesis: the scientific method applied to development
    * Unit testing
    * Integration test
    * Continuous integration dashboards
* *Hands on:*
    * Run the test suite
    * Add coverage for another method to the unit tests

### Literate Programming

Literate Programming with Dexy (30min) - Ana

* Article generation
* RST to HTML, etc
* GitHub replication and sharing
* *Hands on:* run dexy to generate a PDF document


## 11:15 am Fourth Session

### Open Science Publication

Submitting an article to a Reproducible Journal (20 min) - Luis

* Open Science Publication
    * Open Access
    * Publishes article, data, and code
* *Hands on:*
    * Submit Article to the Insight Journal
    * Point to github fork, for source code

### Replicate or Perish !

Attempt to replicate articles (40 min)

* Group assignment
* Replication attempt
* Sharing observations

