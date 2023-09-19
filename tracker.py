# Check the position of mice and if they are in a ROI
#  Make ROI selection
#  Count the time that each mouse has spent in each ROI.
#  Calculate the mouse's speed.
#  Save the mice's data in a log file

import cv2 as cv
from tqdm import tqdm
from utils.utils import *
from utils.parser import *


def open_data():
    import json
    try:
        return json.load(open(args.project_path))
    except:
        print("Error: couldn't open project data")
        exit()
    
def open_capture():
    try:
        capture = cv.VideoCapture(project_data["video_path"])
        if not capture.isOpened():
            print("Error: couldn't open video")
            exit()    
        return capture
    except Exception as e:
        print(f"Error: {str(e)}")
        exit()

def thresholding():
    import random
    beta = random.randint(50, round(255/2))
    return (255/2) + beta

if __name__ == "__main__":
    args = parser_args()
    project_data = open_data()
    capture = open_capture()
    frameWidth = int(capture.get(3))
    frameHeight = int(capture.get(4))
    window_name = 'Preview Window'
    make_window(window_name=window_name,ratio=cv.WINDOW_KEEPRATIO,width=frameWidth,height=frameHeight)
    frameIndex = 0
    previous_pos = (0, 0)
    current_pos = (0, 0)
    num_frames = int(capture.get(cv.CAP_PROP_FRAME_COUNT))
    pbar = tqdm(total=num_frames)