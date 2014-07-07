# -*- coding: utf-8 -*-

import urllib
import json

class ImageDownloader(object):

    figshare_id = None
    image_name = None

    def __init__(self):
      pass

    def set_figshare_id(self,figshare_id):
      self.figshare_id = figshare_id

    def set_image_name(self,image_name):
      self.image_name = image_name

    def download(self):
      figshare_url = "http://api.figshare.com/v1/articles/%s" % self.figshare_id
      f = urllib.urlopen(figshare_url)
      info = json.load(f)
      image_url = info['items'][0]['files'][0]['download_url']
      urllib.urlretrieve(image_url, self.image_name)

