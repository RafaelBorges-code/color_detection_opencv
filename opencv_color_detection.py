#Rafael Borges (inspirado no código de Murtaza
import cv2
import numpy as np


def empty(a):
    pass


cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 300, 300)
cv2.createTrackbar("Hue Min", "TrackBars", 81, 179,
                   empty)  # nome da barra, Nome da tela onde a barra vai ficar, minvalue, maxvalue, função a ser chamada sempre que o valor mudar
cv2.createTrackbar("Hue Max", "TrackBars", 108, 179, empty)
cv2.createTrackbar("Sat Min", "TrackBars", 18, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBars", 180, 255, empty)
cv2.createTrackbar("Val Min", "TrackBars", 111, 255, empty)
cv2.createTrackbar("Val Max", "TrackBars", 217, 255, empty)

while True:
    img = cv2.imread("eu.png")
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")  # what trackbar from what window
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    img_results = cv2.bitwise_and(img, img,
                                  mask=mask)  # imagem de destino, imagem que sera aplicada a mascara, e a mascara

    cv2.imshow("eu", img)
    cv2.imshow("eu em outra cor", imgHSV)
    cv2.imshow("mask", mask)
    cv2.imshow("Result mask", img_results)

    cv2.waitKey(1)
