#!/usr/bin/env python3

import shutil
import click
import utils
from pathlib import Path
from PIL import Image


@click.command()
@click.option(
    "--size",
    prompt="Size of final images",
    help="Size of the final images.",
    default="4x6",
    type=click.Choice(["4x6", "5x7"]),
)
@click.option(
    "--source",
    prompt="Source directory",
    default="~/Downloads/photos",
    help="Source directory.",
)
@click.option(
    "--destination",
    prompt="Destination directory",
    default="~/Downloads/print",
    help="Destination for final photos.",
)
def run(size, source, destination):
    """Simple program that greets NAME for a total of COUNT times."""

    home = str(Path.home())
    source = source.replace("~", home)

    click.echo("")
    click.echo(f"Size of the final images: {size}")
    click.echo(f"Source directory for photos: {source}")

    photos = utils.get_photos(source)
    click.echo(f"Found {len(photos)} photos")

    photos.sort()

    [
        horizontal_photos,
        vertical_photos,
    ] = utils.separate_vertical_and_horizontal_photos(photos)

    click.echo("")
    click.echo("Vertical photos: {}".format(len(vertical_photos)))
    click.echo("Horizontal photos: {}".format(len(horizontal_photos)))

    click.echo("")

    vertical_prints = utils.separate_photos_into_prints(vertical_photos, 8)
    click.echo("Vertical prints: {}".format(len(vertical_prints)))
    # click.echo(vertical_prints)

    horizontal_prints = utils.separate_photos_into_prints(horizontal_photos, 4)
    click.echo("Horizontal prints: {}".format(len(horizontal_prints)))
    # click.echo(horizontal_prints)

    click.echo("")

    shutil.rmtree("/Users/mattkoskela/Desktop/prints")
    Path("/Users/mattkoskela/Desktop/prints").mkdir(parents=True, exist_ok=True)

    height_inches = 4
    width_inches = 6
    dpi = 300

    w = int(width_inches * dpi)
    h = int(height_inches * dpi)

    print_number = 1
    for print in vertical_prints:
        click.echo("Processing print {}".format(print_number))
        img = Image.new("RGB", (w, h), color="white")
        i = 0
        for photo in print:
            new_x_size = int(photo["x"] * (height_inches / 2 * dpi) / photo["y"])
            new_y_size = int(photo["y"] * new_x_size / photo["x"])

            pic = Image.open(photo["full_path"])
            pic = pic.resize((new_x_size, new_y_size), Image.LANCZOS)

            x = 0
            y = 0
            if i == 1 or i == 5:
                x = int(width_inches * dpi / 4 * 1)
            elif i == 2 or i == 6:
                x = int(width_inches * dpi / 4 * 2)
            elif i == 3 or i == 7:
                x = int(width_inches * dpi / 4 * 3)
            if i > 3:
                y = int(height_inches / 2 * dpi)

            img.paste(pic, (x, y))
            i += 1

        img.save("/Users/mattkoskela/Desktop/prints/photo_{}.jpg".format(print_number))
        print_number += 1

    for print in horizontal_prints:
        click.echo("Processing print {}".format(print_number))
        img = Image.new("RGB", (w, h), color="white")
        i = 0
        for photo in print:
            new_x_size = int(photo["x"] * (height_inches / 2 * dpi) / photo["y"])
            new_y_size = int(photo["y"] * new_x_size / photo["x"])

            pic = Image.open(photo["full_path"])
            pic = pic.resize((new_x_size, new_y_size), Image.LANCZOS)

            x = 0
            y = 0
            if i == 1 or i == 3:
                x = int(width_inches * dpi / 2 * 1)
            if i > 1:
                y = int(height_inches / 2 * dpi)

            img.paste(pic, (x, y))
            i += 1

        img.save("/Users/mattkoskela/Desktop/prints/photo_{}.jpg".format(print_number))
        print_number += 1


if __name__ == "__main__":
    run()
