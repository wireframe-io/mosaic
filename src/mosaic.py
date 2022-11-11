#!/usr/bin/env python3

import click
import utils
from pathlib import Path


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

    for photo in photos:
        size = utils.get_photo_dimensions(photo)
        filename = Path(photo).name
        click.echo(f"{filename} - {size}")


if __name__ == "__main__":
    run()
