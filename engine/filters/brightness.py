from PIL import ImageEnhance


def apply(image, factor=1.0):
    """
    Adjust brightness of an image.
    :param image: PIL.Image.Image
    :param factor: > 1 brighter, < 1 darker
    :return: PIL.Image.Image
    """
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(factor)