# Data Sharing

## Introduction

### Data Items as Papers

In the new environment of modern scientific publishing, data items are finally
getting the equivalent status of papers. We can today publish a dataset and get
a Digital Object Identifier
[DOI](http://en.wikipedia.org/wiki/Digital_object_identifier) reference to it,
making it citable.

For example

    Ortega, Ana; Behdadfar, Sareh; Li, Lin; Zenteno, Omar (2014):
    Tralitus Saltator. figshare.
    (http://dx.doi.org/10.6084/m9.figshare.1066744)

### Career Rewards

Now that data items are citable, data sharing activities can be accounted as
part of the career reward system for researchers. Thus recognizing the valuable
contributions that data sharers make to their respective fields and communities.

In this new environment, data items no longer need to be sequestered until a
traditional article is published. Instead, data can be shared immediately after
acquisition for the benefit of the larger scientific community.

### Data Sharing Sites

Many data sharing sites are available.

Here are a few examples, that are focused on certain communities

* Figshare (htt://www.figshare.com)
* MIDAS (http://www.midasplatform.com)
* Girder (http://girder.readthedocs.org/en/latest)

You may find additional specific data sharing sites for your specific field.

## Hands-On

Now that we have acquired several images in the mobile device, it is time to
move these images to an online platform where they can be cataloged, linked to,
and downloaded.

Here we are going to perform this in three steps:

* Export images from the mobile device
* Upload images to a data sharing web site
* Download images via REST API

## Exporting images

There are many options for exporting images from your mobile device (phone or
tablet). They depend on the type of mobile device that you are using. Here we
will explore a few. They are not necessarily optimal for regular scientific
work, but they will take us end-to-end through this exercise.

### Email

* From your mobile device:
  * Using the Sharing options, email the image to yourself.
  * You may want to use your Gmail account for this purpuose.
* From your laptop:
  * Open the email
  * Download the attached image


### Google+

If you are using an Android device, this might be the most straight-forward
method to use.

* From your mobile device: Share the image as a post in G+.
* From your laptop: Visit the G+ post and download the image.


### Twitter

* From your mobile: Tweet the image using the hashtags
  * #reproducibleresearch
  * #scipy2014
  * #openscience
* From your laptop: Visit the twitter page and
  * Click on the image
  * Right click on it to get the URL of the image
  * Download the image in to your local laptop filesystem


## Sharing images

Now that you have brought the images to a hard disk, you can upload them to
your data sharing account. Here we focus on using Figshare, but keep in mind
that other data sharing sites are also available.


### Publishing

* This step is equivalent to serious publishing
* Please use real descriptions and informative tags
* Since this image is going to receive a real DOI identifier, just like a published paper

### Figshare

* Login to your [Figshare account](http://figshare.com/account/my_data)
* Click on the [Upload](http://figshare.com/account/upload) link at the top of the page
* Go to the [My Data](http://figshare.com/account/my_data) link at the top of the page and find your new uploaded image in the list
* On the Status column, click on the "DRAFT" button
  * Select a title for the image (use a serious and descriptive title)
  * Select a Category, from the dropdown menu
    * In our case, we could use "Biological Techniques"
  * Enter a serious description in the "Description" field.
  * Click on the "Public" button, on the bottom right, to make the image publicly available
  * Save the changes
  * Click on the "Publish" link, no the bottom right.
  * Answer the confirmation by clicking on the "Yes, publish" button
  * Click on "Preview" the article
* For a given image take note of its identifier:
  * For example: [http://figshare.com/articles/Tardigrades_Image_01/1050595]
  * Will have the identifier: 1050595
* Use the identifier in the following way to get the article metadata:
  * http://api.figshare.com/v1/articles/1050595
  * This will return a JSON structure such as

    {"count": 1, "items": [{"article_id": 1050595, "title": "Image 002", "figshare_url": "http://figshare.com/articles/Image_002/1050595", "views": 1, "downloads": 0, "shares": 0, "doi": "http://dx.doi.org/10.6084/m9.figshare.1050595", "publisher_doi": "", "publisher_citation": "", "master_publisher_id": 0, "defined_type": "figure", "status": "Public", "version": 1, "published_date": "23:09, Jun 14, 2014", "description": "<p>Image of Tardigrade acquired with a cell phone water drop microscope</p>", "description_nohtml": "Image of Tardigrade acquired with a cell phone water drop microscope", "total_size": "85.10 KB", "owner": {"id": 97454, "full_name": "Luis Ibanez"}, "authors": [{"first_name": "Luis", "last_name": "Ibanez", "id": 97454, "full_name": "Luis Ibanez"}], "tags": [{"id": 247678, "name": "diy microscopy"}, {"id": 98329, "name": "tardigrades"}], "categories": [{"id": 12, "name": "Cell Biology"}, {"id": 8, "name": "Microbiology"}], "files": [{"thumb": "http://previews.figshare.com/1526484/250_1526484.jpg", "download_url": "http://files.figshare.com/1526484/IMG_20140331_131717.jpeg", "name": "IMG_20140331_131717.jpeg", "id": 1526484, "mime_type": "image/jpeg", "size": "87 KB"}], "links": []}]}

* Look for the "download_url" tag.
* Now we can refer to to actual file by using the "download_url" as
  * http://files.figshare.com/1526484/IMG_20140331_131717.jpeg
  * Put the "download_url" of your image in a browser and verify that the image is downloaded
  * Breath, Smile !

More on the Figshare API at [http://api.figshare.com/docs/]

