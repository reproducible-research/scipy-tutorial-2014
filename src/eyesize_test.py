import eyesize
import imagedownloader
import SimpleITK as sitk

def eye_test():

  downloader = imagedownloader.ImageDownloader()
  estimator = eyesize.EyeSize()

  image_name = "TralitusSaltrator.jpg"

  downloader.set_figshare_id("1066744")
  downloader.set_image_name(image_name)
  downloader.download()

  input_image = sitk.ReadImage(image_name)

  estimator.set_image(input_image)
  estimator.set_seed_point([204,400])
  radius_estimate = estimator.estimate()

  return radius_estimate == 8.5 

