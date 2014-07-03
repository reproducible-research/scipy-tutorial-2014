import json
import eyesize

estimator = eyesize.EyeSize()

estimator.set_figshare_id("1066744")
estimator.set_image_name("TralitusSaltrator.jpg")
estimator.set_seed_point([204,400])
radius_estimate = estimator.estimate()

### "save-results"
results = {}
results['radius'] = float(radius_estimate)

with open('image-analysis.json', 'wb') as myfile:
    json.dump(results, myfile)
