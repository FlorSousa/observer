# Check the position of mice and if they are in a ROI
#  Make ROI selection
#  Count the time that each mouse has spent in each ROI.
#  Calculate the mouse's speed.
#  Save the mice's data in a log file

import cv2 as cv
from utils.utils import *

def open_data():
    import json
    try:
        return open(args.project_path)
    except:
        print("erro1")
        exit()
    
def open_capture():
    try:
        return cv.VideoCapture(project_data.video_path)
    except:
        print("erro2")
        exit()
    

if __name__ == "__main__":
    args = parser_args()
    project_data = open_data()
    capture = open_capture()
    