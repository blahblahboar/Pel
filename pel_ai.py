from __future__ import division
import pygame
import time
import random
import math
import os
import subprocess


def start_ai(lives, blobs, paddlepos):
    if lives >= 0:
        for blob in blobs:
             if 852 > blob[2][1] > 820:
                  paddlepos = blob[5]    
        
##
##if __name__ == "__main__":
##    start_ai()
##       




