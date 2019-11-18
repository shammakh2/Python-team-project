from PIL import Image
from PIL import ImageFilter
import os
import argparse

def create_thumbnails(args):
    """Convert images to JPEG thumbnails and appropriately name them"""
    size = 300, 300
    files = os.listdir(r'C:\Users\b9035266\PycharmProjects\practical-3\specification-2\images')
    counter = 0
    for f in files:
        fn, fext = os.path.splitext(f)
        im = Image.open(os.path.join(r'C:\Users\b9035266\PycharmProjects\practical-3\specification-2\images', f))

        if fext != '.jpg':
            im = im.convert('RGB')

        im.thumbnail(size)
        im.save(r'C:\Users\b9035266\PycharmProjects\practical-3\specification-2\thumbnails\thumbnail{0}.thumbnail'
                   .format(counter), "JPEG")
        counter += 1

def gaussian_blur(args):
    """Apply the gaussian blur filter to the specified images"""
    thumbnails = os.listdir(r'C:\Users\b9035266\PycharmProjects\practical-3\specification-2\thumbnails')
    counter = 0
    for f in thumbnails:
        fn, fext = os.path.splitext(f)
        thumb = Image.open(os.path.join(r'C:\Users\b9035266\PycharmProjects\practical-3\specification-2\thumbnails', f))
        thumb = thumb.filter(ImageFilter.GaussianBlur(radius = 10))

        thumb.save(r'C:\Users\b9035266\PycharmProjects\practical-3\specification-2\thumbnails\thumbnail{0}.thumbnail'
                   .format(counter), "JPEG")
        counter += 1


def color_conversion(args):
    """Take pixels of {color} and convert them to another {color}"""
    thumbnails = os.listdir(r'C:\Users\b9035266\PycharmProjects\practical-3\specification-2\thumbnails')

    colors = {
        "red": (255, 0, 0),
        "green": (0, 255, 0),
        "blue": (0, 0, 255),
        "black": (0, 0, 0),
        "white": (255, 255, 255)
    }
    counter = 0
    for f in thumbnails:
        fn, fext = os.path.splitext(f)
        thumb = Image.open(os.path.join(r'C:\Users\b9035266\PycharmProjects\practical-3\specification-2\thumbnails', f))

        pixels = thumb.load()  # create the pixel map

        for i in range(thumb.size[0]):  # for every pixel:
            for j in range(thumb.size[1]):
                if pixels[i, j] == colors[args.colora]:
                    pixels[i, j] = colors[args.colorb]

        thumb.save(r'C:\Users\b9035266\PycharmProjects\practical-3\specification-2\thumbnails\thumbnail{0}.thumbnail'
                   .format(counter), "JPEG")
        counter += 1

def run():
    """Adding the needed parsers/subparsers"""
    parser = argparse.ArgumentParser(prog="img_manip")
    subparsers = parser.add_subparsers(help="Sub Command Help")

    subparsers.add_parser("thumbnails", help='Creates the thumbnails').set_defaults(func=create_thumbnails)

    conversion = subparsers.add_parser("color_conversion", help='converts pixels from Color A to Color B')
    conversion.set_defaults(func=color_conversion)
    conversion.add_argument('-colora', dest='colora', action='store', required=True, help='color to convert from')
    conversion.add_argument('-colorb', dest='colorb', action='store', required=True, help='color to convert to')

    parser.add_argument("-loca", help="Location of images to be modified", required=False)                      #CHANGE FROM FALSE TO TRUE WHEN DONE
    parser.add_argument("-locb", help="Location of where to store the modified images", required=False)         #CHANGE FROM FALSE TO TRUE WHEN DONE

    args = parser.parse_args()
    args.func(args)

run()
