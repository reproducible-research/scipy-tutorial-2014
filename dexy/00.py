# -*- coding: utf-8 -*-
import SimpleITK as sitk
import json
import sys

import eyesize
import imagedownloader

downloader = imagedownloader.ImageDownloader()
estimator = eyesize.EyeSize()

image_name = "TralitusSaltrator.jpg"

downloader.set_figshare_id("1066744")
downloader.set_image_name(image_name)
downloader.download()

input_image = sitk.ReadImage(image_name)

### "segmented"
estimator.set_image(input_image)
estimator.set_seed_point([204,400])
eyes_segmented,radius_estimate = estimator.estimate()

### "overlay"
magnitude_image = sitk.VectorMagnitude(input_image)
image_overlay = sitk.LabelOverlay(magnitude_image, eyes_segmented)
sitk.WriteImage(image_overlay,'SegmentedEyeOverlay.png')


### "save-results"
results = {}
results['radius'] = float(radius_estimate)

with open('image-analysis.json', 'wb') as myfile:
    json.dump(results, myfile)
