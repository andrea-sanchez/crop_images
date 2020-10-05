from typing import Tuple
from .AbstractCropper import AbstractCropper

from PIL.Image import Image as ImageType


class CenteredCropper(AbstractCropper):
    def crop(self, image: ImageType, relation: Tuple) -> ImageType:
        width, height = image.size
        new_height = height * relation[0] / relation[1]
        origen_y = (height - new_height) / 2
        extremo_y = new_height + origen_y
        box = (0, origen_y, width, extremo_y)
        return image.crop(box)
