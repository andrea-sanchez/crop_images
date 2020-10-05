from typing import List, Tuple

from PIL import Image
from PIL.Image import Image as ImageType

from .AbstractCropper import AbstractCropper
from .CropperType import CropperType
from .CenteredCropper import CenteredCropper


def centered_crop_images(images_paths: List[str], relation: Tuple = (4, 6)) -> List[ImageType]:
    return crop_images(images_paths, relation, cropper_factory(CropperType.CENTERED_CROPPER))


def cropper_factory(cropper_type: CropperType) -> AbstractCropper:
    if cropper_type == CropperType.CENTERED_CROPPER:
        return CenteredCropper()
    else:
        raise NotImplementedError("Not a valid cropper")


def crop_images(images_paths: List[str], relation: Tuple = (4, 6), cropper: AbstractCropper = CenteredCropper()) -> List[ImageType]:
    return [cropper.crop(Image.open(file), relation) for file in images_paths]
