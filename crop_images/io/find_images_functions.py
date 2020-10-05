import os
from typing import List

DEFAUL_EXCLUDE_FILES_EXTENSIONS: List[str] = [
    ".ipynb", ".pdf", ".pptx", ".ppt", ".py", ".md", ".git"]


def search_images_paths(path: str, exclude_files_extensions: List[str] = DEFAUL_EXCLUDE_FILES_EXTENSIONS) -> List[str]:
    images: List[str] = []
    for base_path, _, files in os.walk(path):
        for file in files:
            _, file_extension = os.path.splitext(file)
            if not file.startswith(".") and not file_extension in exclude_files_extensions:
                images.append(os.path.join(base_path, file))
    return images
