import cv2 as cv
import numpy as np
from os import mkdir
from math import atan2, cos, sin, sqrt, pi


def drawAxis(frame,area):
    if area["m00"]:
          px = int(area["m10"]/area["m00"])
          py = int(area["m01"]/area["m00"])
          cv.line(frame,(px,py), (px+10,py),(0,0,255),2)
'''
def drawAxis(img, p_, q_, colour, scale):
    p = list(p_)
    q = list(q_)

    angle = atan2(p[1] - q[1], p[0] - q[0])  # angle in radians
    hypotenuse = sqrt((p[1] - q[1]) * (p[1] - q[1]) + (p[0] - q[0]) * (p[0] - q[0]))

    # Here we lengthen the arrow by a factor of scale
    q[0] = p[0] - scale * hypotenuse * cos(angle)
    q[1] = p[1] - scale * hypotenuse * sin(angle)
    cv.line(img, (int(p[0]), int(p[1])), (int(q[0]), int(q[1])), colour, 2, cv.LINE_AA)

    # create the arrow hooks
    p[0] = q[0] + 9 * cos(angle + pi / 4)
    p[1] = q[1] + 9 * sin(angle + pi / 4)
    cv.line(img, (int(p[0]), int(p[1])), (int(q[0]), int(q[1])), colour, 2, cv.LINE_AA)

    p[0] = q[0] + 9 * cos(angle - pi / 4)
    p[1] = q[1] + 9 * sin(angle - pi / 4)
    cv.line(img, (int(p[0]), int(p[1])), (int(q[0]), int(q[1])), colour, 2, cv.LINE_AA)

def getOrientation(pts, img, draw):
    # Construct a buffer used by the pca analysis
    sz = len(pts)
    data_pts = np.empty((sz, 2), dtype=np.float64)

    for i in range(data_pts.shape[0]):
        data_pts[i, 0] = pts[i, 0, 0]
        data_pts[i, 1] = pts[i, 0, 1]

    # Perform PCA analysis
    mean = np.empty((0))
    mean, eigenvectors, eigenvalues = cv.PCACompute2(data_pts, mean)

    # Store the center of the object
    center = (int(mean[0, 0]), int(mean[0, 1]))

    # Draw the principal components
    cv.circle(img, center, 3, (42, 89, 247), -1)
    p1 = (
        center[0] + 0.02 * eigenvectors[0, 0] * eigenvalues[0, 0],
        center[1] + 0.02 * eigenvectors[0, 1] * eigenvalues[0, 0]
    )
    p2 = (
        center[0] - 0.02 * eigenvectors[1,0] * eigenvalues[1,0],
        center[1] - 0.02 * eigenvectors[1,1] * eigenvalues[1,0]
    )

    if(draw):
        drawAxis(img, center, p1, (91, 249, 77), 2)
        drawAxis(img, center, p2, (190, 192, 91), 2)

    # orientation in radians
    angle = atan2(eigenvectors[0, 1], eigenvectors[0, 0])

    return {"center":center,"angle":angle}
'''

def save_video(filename,frameWidth,frameHeight,frame_rate, encode=cv.VideoWriter_fourcc('M', 'J', 'P', 'G')):
        try:
            cv.VideoWriter(filename,encode,frame_rate, (frameWidth, frameHeight))
            return True
        except:
             return False
        
def make_folder(path,folder):
    if (not path.exists(folder)):
            mkdir(folder)

def write_file(file_path,text,mode="w"):
    with open(file_path, mode) as log_file:
            log_file.write(f'{text}')

def make_window(window_name,ratio,width,height):
    cv.namedWindow(window_name,ratio)
    cv.resizeWindow(window_name,width,height)

def apply_morphological_filter(actual_frame,background_frame,lower_white,upper_white):
        sub_frame = cv.absdiff(actual_frame, background_frame)

        filtered_frame = cv.inRange(sub_frame, lower_white, upper_white)

        # Kernel for morphological operation opening
        kernel3 = cv.getStructuringElement(
            cv.MORPH_ELLIPSE,
            (3, 3),
            (-1, -1)
        )

        kernel20 = cv.getStructuringElement(
            cv.MORPH_ELLIPSE,
            (20, 20),
            (-1, -1)
        )

        # Morphological opening
        return cv.dilate(cv.erode(filtered_frame, kernel3), kernel20)