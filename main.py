#import libraries
from tkinter import *
from tkinter import ttk
import PIL
from PIL import ImageTk, Image

def main():
    print("Running")
    
root = Tk(className="Naztech Image Optimizer") #init Tk
root.title("Image Optimizer V1.0") #set title
root.geometry('300x500') #set window
root.resizable(False, True)

root.mainloop() #run tkinter window

if __name__ == "__main__":
    main()

    
