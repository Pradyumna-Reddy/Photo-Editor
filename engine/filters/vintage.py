from PIL import Image, ImageEnhance
import numpy as np

def vinatage_filter(image,intensity = 1.0):

    #1) covert to RBG:
    img = image.convert("RGB")

    #2) reducing the contrast ad brightness for fade look
    img = ImageEnhance.Contrast(img).enhance(0.85*intensity + 0.5)
    img = ImageEnhance.Brightness(img).enhance(0.5*intensity + 0.5)


    #3) converting to numoy array
    arr = np.array(img, dtype = np.float32)

    #4)applying the warm tone
    arr[:, :, 0] *= 0.8*intensity #RED
    arr[:, :, 1] *= 0.9 * intensity #GREEN
    arr[:, :, 2] *= 1.3 #slight reduce in blue 

    #5)Optional vignette (dark edges)
    rows, cols, _ = arr.shape
    y, x = np.ogrid[:rows, :cols]
    center_y, center_x = rows / 2, cols / 2
    distance = np.sqrt((x - center_x)**2 + (y - center_y)**2)
    max_distance = np.sqrt(center_x**2 + center_y**2)
    vignette_mask = 1 - (distance / max_distance) * 0.8 * intensity
    vignette_mask = np.clip(vignette_mask, 0.3, 1.0)
    arr *= vignette_mask[:, :, np.newaxis]
    
    #6) clip and convert back

    arr= np.clip(arr, 0, 255).astype(np.uint8)
    new_img = Image.fromarray(arr)

    return new_img