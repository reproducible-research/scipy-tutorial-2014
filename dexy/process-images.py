import SimpleITK as sitk
import urllib

source = "http://54.221.241.247:8080/api/v1/file/539c7a298d72b60edb223eca/download/IMG_20140331_131725.jpeg"
destination = "tardigrade.jpg"

urllib.urlretrieve(source, destination)
image = sitk.ReadImage(destination)

### "image-size"
print image.GetSize()
