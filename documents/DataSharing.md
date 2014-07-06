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

* Login to your [Figshare account](http://figshare.com/account/my_data)
* Create a new project, titled: Reproducible Research Training
* Upload images to this project
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

More on the Figshare API at [http://api.figshare.com/docs/]


### Girder

* Login in your Girder account
* Create a folder called 'ReproducibleResearch'
* Upload the images to this folder
* Share the link to the folder with your peers
* Downloading a file through the API
  * Look at the Item, for example [http://54.221.241.247:8080/#item/539c7a298d72b60edb223ec9]
  * The last number in the URL is the Item ID: 539c7a298d72b60edb223ec9
  * The page will show you the file name as: IMG_20140331_131725.jpeg
  * We can combine the two in a URL of the form:
  * http://54.221.241.247:8080/api/v1/file/ItemID/download/FileName
  * For example
    * http://54.221.241.247:8080/api/v1/file/539c7a298d72b60edb223eca/download/IMG_20140331_131725.jpeg

More on the Girder API at [http://54.221.241.247:8080/api/v1]
More on the Girder Documentation [http://girder.readthedocs.org]
