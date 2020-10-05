import argparse

from crop_images.croppers import crop_images
from crop_images.io import save_images_as_original_tree, search_images_paths

parser = argparse.ArgumentParser(description='Crop images')

parser.add_argument('images_path', help='path of images')
parser.add_argument('destination_path', help='destination path of images')

args = parser.parse_args()

images_paths = search_images_paths(args.images_path)
cropped_images = crop_images(images_paths)
save_images_as_original_tree(images_paths, cropped_images, args.destination_path)
