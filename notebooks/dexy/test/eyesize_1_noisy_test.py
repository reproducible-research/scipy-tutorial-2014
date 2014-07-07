import sys

sys.path.append('..')

import eyesize
import imagedownloader
import SimpleITK as sitk

def eyesize_noisy_test():

  downloader = imagedownloader.ImageDownloader()
  estimator = eyesize.EyeSize()

  image_name = "TralitusSaltrator.jpg"

  downloader.set_figshare_id("1066744")
  downloader.set_image_name(image_name)
  downloader.download()

  input_image = sitk.ReadImage(image_name)

  estimator.set_image(input_image)
  estimator.set_seed_point([204,400])

  eyes_segmented,radius_estimate = estimator.estimate()

  sitk.WriteImage(eyes_segmented,'SegmentedEye.png')

  expected_value = 85
  assert radius_estimate == expected_value, \
    "Problem with estimating radius: current: %s, expected: %s" % (radius_estimate, expected_value)
