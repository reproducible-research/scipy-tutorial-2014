# -*- coding: utf-8 -*-
import SimpleITK as sitk
import json
import numpy as np
import urllib

def figshare_info(fig_id):
    figshare_url = "http://api.figshare.com/v1/articles/%s" % fig_id
    f = urllib.urlopen(figshare_url)
    return json.load(f)

info = figshare_info("1066744")
image_url = info['items'][0]['files'][0]['download_url']

image_file = "TralitusSaltrator.jpg"
urllib.urlretrieve(image_url, image_file)

image = sitk.ReadImage(image_file)


mimage = sitk.VectorMagnitude(image)
assert mimage.GetNumberOfComponentsPerPixel() == 1

otsu = sitk.OtsuThresholdImageFilter()
bimage = otsu.Execute(mimage)
sitk.WriteImage(bimage,'OtsuThreshold.png')


### "segmented"
color_region_growing = sitk.VectorConfidenceConnectedImageFilter()
color_region_growing.SetNumberOfIterations(4)
color_region_growing.SetMultiplier(5.3)
color_region_growing.SetInitialNeighborhoodRadius(2)
color_region_growing.SetReplaceValue(255)
color_region_growing.AddSeed([204,400])
eyes_segmented = color_region_growing.Execute(image);
image_overlay = sitk.LabelOverlay(mimage, eyes_segmented)
sitk.WriteImage(image_overlay,'SegmentedEyeOverlay.png')


### "radius"
distance_filter = sitk.SignedMaurerDistanceMapImageFilter()
distance_filter.SetInsideIsPositive(True)
distance_map = distance_filter.Execute(eyes_segmented)
radius_estimate = np.amax(sitk.GetArrayFromImage(distance_map))

### "save-results"
results = {}
results['radius'] = float(radius_estimate)

with open('image-analysis.json', 'wb') as myfile:
    json.dump(results, myfile)
