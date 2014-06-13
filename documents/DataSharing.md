# Data Sharing

Now that we have acquired several images in the mobile device, it is time to
move these images to an online platform where they can be cataloged, linked to,
and downloaded.

Here we are going to perform this in two steps:

* Export images from the mobile device
* Upload images to a data sharing web site

## Exporting images

There are many options for exporting images, depending on the type of mobile
device that you are using. Here we will explore a few. They are not necessarily
optimal for regular scientific work, but they will take us end-to-end through
this exercise.

### Google+

If you are using an Android device, this might be the most straight-forward method to use.

* Share the image as a post in G+
* Install in your computer the Google command line tool:
  * [https://code.google.com/p/googlecl]
* To get the list of all your albums
  * Use the command:  google picasa list-albums > myalbums.txt
* To get the list of all your pictures
  * Use the command: google picasa list > mypictures.txt
  * Identify the URL of the pictures that you posted


### Twitter

* Tweet the image using the hashtags
  * #reproducibleresearch
  * #scipy
  * #openscience

### Email

* Using the Sharing options, email the image to yourself.
* You may want to use your Gmail account for this purpuose.


## Sharing images

Now that you have brought the images to a hard disk, you can upload them to both of your data sharing accounts.

### Figshare

* Login in your Figshare account [http://figshare.com/account/my_data]
* Create a new project, titled: Reproducible Research Training
* Upload images to this project
* For a given image take note of its identifier:
  * For example: [http://figshare.com/articles/Tardigrades_Image_01/1050597]
  * Will have the identifier: 1050597
* Use the identifier in the following way to get the article metadata:
  * http://api.figshare.com/v1/articles/1050597
  * This will return a JSON structure such as

  {"count": 1, "items": [{"article_id": 1050597, "title": "Tardigrades Image 01", "figshare_url": "http://figshare.com/articles/Tardigrades_Image_01/1050597", "views": 1, "downloads": 0, "shares": 0, "doi": "http://dx.doi.org/10.6084/m9.figshare.1050597", "publisher_doi": "", "publisher_citation": "", "master_publisher_id": 0, "defined_type": "media", "status": "Public", "version": 1, "published_date": "18:07, Jun 13, 2014", "description": "<p>Image of tardigrades acquired with a mobile device and drop of water lens.</p>", "description_nohtml": "Image of tardigrades acquired with a mobile device and drop of water lens.", "total_size": "57.47 MB", "owner": {"id": 97454, "full_name": "Luis Ibanez"}, "authors": [{"first_name": "Luis", "last_name": "Ibanez", "id": 97454, "full_name": "Luis Ibanez"}], "tags": [{"id": 98329, "name": "tardigrades"}], "categories": [{"id": 12, "name": "Cell Biology"}], "files": [{"thumb": "http://previews.figshare.com/1526486/250_1526486.png", "download_url": "http://files.figshare.com/1526486/VID_20140331_135241.mp4", "name": "VID_20140331_135241.mp4", "id": 1526486, "mime_type": "video/mp4", "size": "57.47 MB"}], "links": []}]}

* Look for the "download_url" tag.
* Now we can refer to to actual file by using the "download_url" as
  * http://files.figshare.com/1526486/VID_20140331_135241.mp4


### MIDAS

* Login in your MIDAS account
* Join the community Reproducible Research [?]
* Create a folder with your name
* Upload the images to this folder
* Share the link to the folder with your peers

