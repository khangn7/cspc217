
# https://note.nkmk.me/en/python-opencv-imread-imwrite/

# https://www.geeksforgeeks.org/numpy-ndarray/


# import cv2

# image = cv2.imread("images/mike2.jpg")
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # plt.imshow(gray, cmap="gray")
# # plt.show()
# # blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# # wide = cv2.Canny(blurred, 50, 200)

# # perform the canny edge detector to detect image edges

# inp = 1
# while inp:
#     inp = int(input("cont: "))
#     edges = cv2.Canny(gray, threshold1=int(input("1: ")), threshold2=int(input("2: ")))

#     cv2.imshow("asdf", edges)

#     cv2.waitKey(0)

# cv2.destroyAllWindows()

import cv2

# ndarray, this one 3 dimensions
im = cv2.imread('images/mikeBW.png')

# im.shape is tuple with len() of each dimension

# ndarray.shape is as if 
# def get_shape(ndarray):

#     if type(ndarray[0]) == "array":

#         return [len(ndarray)].concat(get_shape[0])

#     else:
#         return []

# tuple (height, width, )
shape = im.shape

# in pixels
width = shape[1]
height = shape[0]

# to get BGR list for pixel at position x, y
def getPixel(x, y):
    return im[y][x]

# 

# content = "asdf"
# with open("in/mike.txt", "w") as file:
#     file.write(content)