'''
def resize(src, scale=0.5):
    width = int(src.shape[1] * scale)
    height = int(src.shape[0] * scale)

    dsize = (width, height)
    output = cv2.resize(src, dsize)


def canny_processing(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    return edge

def pencil_sketch(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    for row in range(len(edges)):
        for col in range(len(edges[row])):
            if edges[row][col] == 255:
                edges[row][col]  = 0
            elif edges[row][col] == 0:
                edges[row][col]  = 255

    return edges        


def compression():
    ''' file compression
    order than images
    '''
    return         

#light
def image_to_sketch(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_invert = cv2.bitwise_not(gray)
    img_smoothing = cv2.GaussianBlur(img_invert, (21, 21), sigmaX =0, sigmaY = 0)
    doodge = cv2.divide(gray, 255 - img_smoothing, scale = 256)
    return doodge

#dark
def image_to_sketch2(rgb):
    gray = np.dot(rgb[..., :3],[0.299, 0.587, 0.114])
    diff = 255 - gray
    smoothing = scipy.ndimage.filters.gaussian_filter(diff, sigma=10)
    result = smoothing * 255/(255 - gray)
    result[result > 255] = 255
    result[gray == 255] = 255
    return result.astype('uint8')    

#composite
def img_to_sketch(img):
    img1 = image_to_sketch2(img)
    img2 = image_to_sketch(img)
    composite_img = (img1/2) + (img2/2)
    return composite_img 
    '''