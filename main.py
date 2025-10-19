from engine.core import ImageProcessor

processor = ImageProcessor(image_path="test.jpg")
#processor.apply("brightness", factor=1.8)
processor.apply("vinatage_filter",intensity = 1)
processor.save("output.jpg")
