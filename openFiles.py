import sys, os
import tkinter as tk
from tkinter.filedialog import *

imageFileTypes = [("All files", "*.jpg *.jpeg *.png *.gif"), ("JPEG files", "*.jpg *.jpeg"), ("PNG files", "*.png"), ("GIF files", "*.gif")]
textFileTypes = [("Text files", "*.txt"), ("All files", "*.*")]

def openFile(fileType):
    file = askopenfilename(
        title="Select a file",
        filetypes=fileType
    )
    return file

def openDirectory(fileType):
    dir = askdirectory()
    files = os.listdir(dir)
    file_list = ''
    for i in files:
        file_list = file_list + i + '\n'
    return dir, files