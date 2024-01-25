#!/usr/bin/env python3
'''
Python 7 nodarbības mājasdarbs Nr.2

Uzdevums: aizpildīt vietas ar atzīmi TODO

'''
import cv2


class IntroOpenCV:
    '''
    Izveidot klasi, kurai ir 5 publiskas metodes:
    - setBilde -  definē bildes failu
    - bilde 
    - melnbalts

    !Klasei nav neviena publiski pieejami parametri!
    '''
    def set_picture(self, BildeFails):
        self.__picture = BildeFails

    def get_picture(self):
        originala_bilde = cv2.imread(self.__picture)
        cv2.imshow("Originālbilde", originala_bilde)
        return 0

    def get_black_white(self):
        originala_bilde = cv2.imread(self.__picture, cv2.IMREAD_GRAYSCALE)
        cv2.imshow("Melnbalta bilde", originala_bilde)
        return 0

if __name__ == "__main__":
    obj = IntroOpenCV()
    obj.set_picture("python.jpg")
    
    
