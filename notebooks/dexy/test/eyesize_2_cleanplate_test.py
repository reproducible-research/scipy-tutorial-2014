import os
import shutil
import sys

sys.path.append('..')

import eyesize
import imagedownloader
import SimpleITK as sitk

def eyesize_cleanplate_test():

  downloader = imagedownloader.ImageDownloader()
  estimator = eyesize.EyeSize()

  image_name = "TralitusSaltrator.jpg"

  inputs_dir = os.path.join(os.getcwd(), "inputs")
  outputs_dir = os.path.join(os.getcwd(), "outputs")
  
  image_path = os.path.join(inputs_dir, image_name)
  
  # Clear inputs folder
  if os.path.isdir(inputs_dir):
    shutil.rmtree(inputs_dir)
  os.mkdir(inputs_dir)
  
  # Clear outputs folder
  if os.path.isdir(outputs_dir):
    shutil.rmtree(outputs_dir)
  os.mkdir(outputs_dir)

  downloader.set_figshare_id("1066744")
  downloader.set_image_name(image_path)
  downloader.download()

  input_image = sitk.ReadImage(image_path)

  estimator.set_image(input_image)
  estimator.set_seed_point([204,400])

  eyes_segmented,radius_estimate = estimator.estimate()

  sitk.WriteImage(eyes_segmented,'SegmentedEye.png')

  expected_value = 85
  assert radius_estimate == expected_value, \
    "Problem with estimating radius: current: %s, expected: %s" % (radius_estimate, expected_value)
