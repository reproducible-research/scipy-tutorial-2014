# -*- coding: utf-8 -*-

import SimpleITK as sitk
import numpy as np
import urllib
import json

class EyeSize(object):

    figshare_id = None
    image_name = None
    seed_point = None
    input_image = None

    def __init__(self):
      pass

    def set_figshare_id(self,figshare_id):
      self.figshare_id = figshare_id

    def set_image_name(self,image_name):
      self.image_name = image_name

    def set_seed_point(self,seed_point):
      self.seed_point = seed_point

    def get_image(self):
      figshare_url = "http://api.figshare.com/v1/articles/%s" % self.figshare_id
      f = urllib.urlopen(figshare_url)
      info = json.load(f)
      image_url = info['items'][0]['files'][0]['download_url']
      urllib.urlretrieve(image_url, self.image_name)
      self.input_image = sitk.ReadImage(self.image_name)

    def estimate(self):
      self.get_image()
      color_region_growing = sitk.VectorConfidenceConnectedImageFilter()
      color_region_growing.SetNumberOfIterations(4)
      color_region_growing.SetMultiplier(5.3)
      color_region_growing.SetInitialNeighborhoodRadius(2)
      color_region_growing.SetReplaceValue(255)
      color_region_growing.AddSeed(self.seed_point)
      eyes_segmented = color_region_growing.Execute(self.input_image)
      distance_filter = sitk.SignedMaurerDistanceMapImageFilter()
      distance_filter.SetInsideIsPositive(True)
      distance_map = distance_filter.Execute(eyes_segmented)
      radius_estimate = np.amax(sitk.GetArrayFromImage(distance_map))
      return radius_estimate


