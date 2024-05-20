#import libraries
from tkinter import *
from tkinter import ttk
import os
import PIL
from PIL import ImageTk, Image
import openFiles

selectedFiles = None
filePreview = None
fileList = None
imgPreview = None


def main():
    print("Running...")
    root = initializeRoot()
    menubar = initializeMenu(root)
    root.config(menu=menubar)
    initializeWidgets(root)
    root.mainloop()

def initializeRoot():
    root = Tk(className="Naztech Image Optimizer")
    root.title("Image Optimizer V1.0")

    # Linux Logo Declare
    myIcon = Image.open('icon.png')
    logo = ImageTk.PhotoImage(myIcon)
    root.wm_iconphoto(True, logo)
    # Windows Logo Declare
    # root.iconbitmap('icon.ico')

    root.geometry('600x500')
    # root.minsize('500x300')
    root.resizable(False, False)
    return root

def initializeMenu(root):
    menubar = Menu(root)

    #File menu
    file_menu = Menu(menubar, tearoff=0)
    file_menu.add_command(label="Open File", command=openFile)
    file_menu.add_command(label="Open Directory", command=openDir)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.destroy)
    menubar.add_cascade(label="File", menu=file_menu)

    #Edit menu
    edit_menu = Menu(menubar, tearoff=0)
    edit_menu.add_command(label="QuikOptimize")
    edit_menu.add_separator()
    edit_menu.add_command(label="Preferences")
    menubar.add_cascade(label="Edit", menu=edit_menu)

    #Debug menu
    debug = Menu(menubar, tearoff=0)
    debug.add_command(label="Print File Dir", command=lambda: print(selectedFiles))
    menubar.add_cascade(label="Debug", menu=debug)

    return menubar

def initializeWidgets(root):
    global filePreview
    global fileList
    global imgPreview
    #Banner

    #File Preview
    filePreview = LabelFrame(root, text="")
    fileList = ttk.Treeview(filePreview)
    imgPreview = Label(filePreview, width=40, height=13, relief=SOLID )

    fileList.pack(side= 'left')
    imgPreview.pack(side= 'left', padx=15, pady=15)

    filePreview.pack()
    
    #Workspace and Options

    workspace = Frame(root)
    dimensions = ttk.Notebook(workspace)

    aspectRatio = Frame(dimensions)
    pixels = Frame(dimensions)

    #Add aspect ratio tab here
    Label(aspectRatio, text="Aspect Ratio:").pack(side="left")
    ratioWidth = Entry(aspectRatio, width=3)
    ratioHeight = Entry(aspectRatio, width=3)

    ratioWidth.pack(side="left")
    ratioHeight.pack(side="left")
    
    #Add pixel sizing tab here
    Label(pixels, text="Width:").pack()
    pixelWidth = Entry(pixels, width=3)
    pixelWidth.pack()
    Label(pixels, text="Height:").pack()
    pixelHeight = Entry(pixels, width=3)
    pixelHeight.pack()
    
    dimensions.add(aspectRatio, text='Aspect Ratio')
    dimensions.add(pixels, text='Size (Pixels)')
    
    dimensions.pack(padx=15, pady=15, ipadx=15, ipady=15)

    workspace.pack(side='left')

    return filePreview, fileList, imgPreview

def openFile():
    selectedFiles = openFiles.openFile(openFiles.imageFileTypes)
    filePreview.config(text=selectedFiles)
    loadImage(str(selectedFiles))

def clearDir():
    for item in fileList.get_children():
            fileList.delete(item)

def openDir():
    dir, selectedFiles = openFiles.openDirectory(openFiles.imageFileTypes)
    clearDir()
    for file in selectedFiles:            
        fileList.insert('', 'end', text=str(file), values=(str(file)))
    filePreview.config(text=dir)

def loadImage(imgPath):
    print(imgPath)

if __name__ == "__main__":
    main()
