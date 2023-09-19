import cv2

path = "/home/jhonatas/Downloads/campo_aberto.mp4"
video_capture = cv2.VideoCapture(path) 
ret, back_frame = video_capture.read()

if ret:
    import random
    back_frame = cv2.cvtColor(back_frame,cv2.COLOR_BGR2GRAY)
    histograma = cv2.calcHist([back_frame], [0], None, [256], [0, 256])
    beta = random.randint(50,127)
    limiar = 255/2 + beta
    