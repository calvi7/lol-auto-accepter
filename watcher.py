import numpy as np
import cv2 as cv

import time
import mss
import os

import pydirectinput


class Watcher:
    def __init__(self) -> None:
        self.stc = mss.mss()

        path = os.path.dirname(__file__)
        self.img_path = os.path.join(path, "accept.jpg")

    def match_finder(self):
        img = self.screenshot()
        match_found = cv.imread(self.img_path)

        result_try = cv.matchTemplate(img, match_found, cv.TM_CCOEFF_NORMED)

        _, mVal, _, mLoc = cv.minMaxLoc(result_try)

        return mVal > .9, mLoc

    def screenshot(self, left=0, top=0, width=1920, height=1080):
        scr = self.stc.grab({
            'left': left,
            'top': top,
            'width': width,
            'height': height,
        })

        img = np.array(scr)
        img = cv.cvtColor(img, cv.IMREAD_COLOR)

        return img

    def click(self, x, y, wait=0):
        pydirectinput.moveTo(x, y)
        time.sleep(wait)
        pydirectinput.mouseDown()
        time.sleep(wait)
        pydirectinput.mouseUp()

    def watch(self):
        """Busca si se encontro la partida y clickea el boton de aceptar
        """
        found, mLoc = self.match_finder()
        x, y = mLoc
        if found:
            self.click(x, y)
            print("Partida aceptada!")
            time.sleep(5)
