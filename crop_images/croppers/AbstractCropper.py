from abc import ABC, abstractmethod
from typing import Tuple

from PIL.Image import Image as ImageType


class AbstractCropper(ABC):
    @abstractmethod
    def crop(self, image: ImageType, relation: Tuple) -> ImageType:
        pass
