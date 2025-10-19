from PIL import Image
from .filters import brightness
from engine.filters.sunny import sunny_filter
from engine.filters.vintage import vinatage_filter


class ImageProcessor:
    def __init__(self, image_path=None, image=None):
        if image:
            self.image = image.convert('RGB')
        elif image_path:
            self.image = Image.open(image_path).convert('RGB')
        else:
            raise ValueError('image_path or image is required')

        self.filters = {
            'brightness': brightness.apply,
            'sunny_filter': sunny_filter,
            'vinatage_filter': vinatage_filter,
        }

    def apply(self, filter_name, **kwargs):
        if filter_name not in self.filters:
            raise ValueError(f'filter_name must be one of {self.filters.keys()}')
        self.image = self.filters[filter_name](self.image, **kwargs)

    def save(self, path = 'output.jpg'):
        self.image.save(path)