from PIL import Image
import numpy as np
def sunny_filter(image,intensity):
    #convert to new rgb image
    img = image.convert("RGB")
    #set my sunny filter
    new_R = intensity * 1.2 
    new_G = intensity * 1.1
    new_B = intensity * 0.8
    #coverting to numpy array
    arr = np.array(img, dtype=np.float32)
    
    #applying my sunny filter to the arrays
    arr[:,:,0] = arr[:,:,0] * new_R
    arr[:,:,1] = arr[:,:,1] * new_G
    arr[:,:,2] = arr[:,:,2] * new_B
    #reducing the intensity if they go outof range
    arr = np.clip(arr,0,255)
    #converting back into single 8 bit digit
    arr = arr.astype(np.uint8)
    #converting that array into new changed image
    new_img = Image.fromarray(arr)
    
    return new_img