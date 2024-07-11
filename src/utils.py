import os
from PIL import Image
from pathlib import Path
from pillow_heif import register_heif_opener

register_heif_opener()


def get_photos(source):
    """Return a list of photos from the source directory."""
    photos = []
    for file in os.listdir(source):
        if (
            file.endswith(".jpg")
            or file.endswith(".jpeg")
            or file.endswith(".png")
            or file.endswith(".heic")
        ):
            photos.append(os.path.join(source, file))
        elif file.endswith(".mov"):
            # TODO: Write a function to extract the first frame of the video
            pass

    return photos


def get_photo_dimensions(photo):
    """Return the dimensions of the photo."""
    return Image.open(photo).size


def separate_vertical_and_horizontal_photos(photos):
    vertical_photos = []
    horizontal_photos = []

    for photo_path in photos:
        size = get_photo_dimensions(photo_path)
        photo = {
            "full_path": photo_path,
            "filename": Path(photo_path).name,
            "x": size[0],
            "y": size[1],
        }

        if size[0] > size[1]:
            horizontal_photos.append(photo)
        else:
            vertical_photos.append(photo)

    return [horizontal_photos, vertical_photos]


def separate_photos_into_prints(photos, number_of_photos_in_print):
    """Return a list of prints, each print is a list of photos."""
    prints = []
    photos_in_print = []

    for photo in photos:
        if len(photos_in_print) == number_of_photos_in_print:
            prints.append(photos_in_print)
            photos_in_print = []

        photos_in_print.append(photo)

    if len(photos_in_print) > 0:
        prints.append(photos_in_print)

    return prints


def resize_photo(photo, size):
    """Resize the photo to the given size."""
    image = Image.open(photo["full_path"])
    image = image.resize(size, Image.ANTIALIAS)
    image.save("/Users/mattkoskela/Desktop/prints/" + photo["filename"])
