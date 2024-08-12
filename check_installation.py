import pygame 
import PIL
import cv2
import moviepy
import importlib.metadata 
import tkinter as tk 

def check_installation():
    print("✅ Pygame version:", pygame.__version__)
    print("✅ Pillow version:", PIL.__version__)
    print("✅ OpenCV version:", cv2.__version__)
    print("✅ MoviePy version:", moviepy.__version__)
    print("✅ Pydub version:", importlib.metadata.version('pydub'))
    print("✅ Tkinter is installed and working!")

if __name__ == "__main__":
    check_installation()
