# Check the position of mice and if they are in a ROI
#  Make ROI selection ✔
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

def draw_roi(frame):
    if("rois" in project_data.keys()):
        for index,roi in enumerate(rois):
            top_left = (roi["x"], roi["y"])
            bottom_right = (roi["x"]+roi["w"], roi["y"]+roi["h"])
            mark_color = (128, 244, 66)
            cv.rectangle(frame, top_left, bottom_right,mark_color,2)
            cv.putText(frame,f'Counter: {rois_counter[index]}', (top_left[0], bottom_right[1]), cv.FONT_HERSHEY_COMPLEX,1, (255,255,255))
            
        return frame
    else:
        print("Error: The project data don't have a ROI list")
        exit()

def select_threshold(static_frame):
    threshold = thresholding()
    gray_frame = cv.cvtColor(static_frame, cv.COLOR_BGR2GRAY)
    s = cv.threshold(gray_frame, threshold, 255, cv.THRESH_BINARY)[1]
    cv.imshow("qualquer coisa", s)
    
    key = cv.waitKey(0)
    
    if key == 27 or key == ord('q'):
        cv.destroyAllWindows()
        return threshold
    elif key == ord('c'):
        return select_threshold(static_frame)

        


if __name__ == "__main__":
    args = parser_args()
    project_data = open_data()
    rois = project_data["rois"]
    rois_counter = [ 0 for _ in range(len(rois)) ]
    capture = open_capture()
    ret, bg_frame = capture.read()
    threshold = select_threshold(bg_frame)
    print(threshold)
    frameWidth = int(capture.get(3))
    frameHeight = int(capture.get(4))
    window_name = 'Preview Window'
    make_window(window_name=window_name,ratio=cv.WINDOW_KEEPRATIO,width=frameWidth,height=frameHeight)
    frameIndex = 0
    previous_pos = (0, 0)
    current_pos = (0, 0)
    num_frames = int(capture.get(cv.CAP_PROP_FRAME_COUNT))
    pbar = tqdm(total=num_frames)

    while(capture.isOpened()):
        ret,frame = capture.read()
        if not ret:
            print("Error: Couldn't open frame %d" % (frameIndex))
            exit()
        
        gray_frame = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        filtered_frame = cv.threshold(gray_frame, threshold, 255, cv.THRESH_BINARY)[1]
        contours, _ = cv.findContours(filtered_frame, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
        cv.drawContours(frame, contours, -1, (0, 255, 0), 3)

        frame = draw_roi(frame)
        cv.imshow(window_name, frame)
        pbar.update(1)
        frameIndex+=1

        if cv.waitKey(30) & 0xFF == ord('q'):
            break