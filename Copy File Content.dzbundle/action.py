# Dropzone Action Info
# Name: Copy File Content
# Description: Copy the content of a text file.
# Handles: Files
# Creator: Alex Kuang
# URL: http://github.com/alexkuang0
# Events: Dragged
# KeyModifiers: Command, Option, Control, Shift
# SkipConfig: No
# RunsSandboxed: Yes
# Version: 1.0
# MinDropzoneVersion: 3.5

import time

def dragged():

    file_path = items[0]
    f = open(file_path)
    text_to_copy = f.read()
    f.close()

    dz.finish("Copied!")

    dz.text(text_to_copy)
 
def clicked():
    # This method gets called when a user clicks on your action
    dz.finish("You clicked me!")
    dz.url(False)
