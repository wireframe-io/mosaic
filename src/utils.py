import os
from PIL import Image


def get_photos(source):
    """Return a list of photos from the source directory."""
    photos = []
    for file in os.listdir(source):
        if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
            photos.append(os.path.join(source, file))

    return photos


def get_photo_dimensions(photo):
    """Return the dimensions of the photo."""
    return Image.open(photo).size
