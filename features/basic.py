import cv2

def resize():
    src = cv2.imread('', cv2.IMREAD_UNCHANGED)
    scale = 0.5

    width = int(src.shape[1] * scale)
    height = int(src.shape[0] * scale)

    dsize = (width, height)
    output = cv2.resize(src, dsize)def canny_processing():


def canny_processing():
    image_array = np.asarray(bytearray(url.read()), dtype=np.uint8)
    img_opencv = cv2.imdecode(image_array, -1)
    gray = cv2.cvtColor(img_opencv, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)
    retval, buffer = cv2.imencode('.jpg', edges)
    response = make_response(buffer.tobytes())
    response.headers['Content-Type'] = 'image/jpeg'
    # Return the response:
    return response

def cropping():
    return 


def compression():
    ''' file compression
    order than images
    '''
    return         

def imageToSketch():
    return 