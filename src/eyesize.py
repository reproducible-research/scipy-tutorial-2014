# -*- coding: utf-8 -*-

import SimpleITK as sitk
import numpy as np
import imagedownloader
import json

class EyeSize(object):

    seed_point = None
    input_image = None

    def __init__(self):
      pass

    def set_seed_point(self,seed_point):
      self.seed_point = seed_point

    def set_image(self,input_image):
      self.input_image = input_image

    def estimate(self):
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

