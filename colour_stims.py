# -*- coding: utf-8 -*-

# colour_stims.py
#
# Created by Thomas Nelson <tn90ca@gmail.com>
#
# Created..........2015-03-24
# Modified.........2015-03-24


# Import required modules
import os
from psychopy import visual, event, gui


def get_colour(win, shape, text, col, dlg_info):
    # Display the colour and text to screen
    colour = [(x/127.5 - 1) for x in col]
    shape.setFillColor(colour, colorSpace='rgb')
    text.setText(col)
    win.flip()

    # Wait for user response
    event.waitKeys() 
    
    # Get user response of photometer reading
    colour_dlg = gui.DlgFromDict(dictionary=dlg_info,
                                 title="Enter the Photometer Results")
    if S1.OK == False:
      exit(1)

    x = dlg_info['x']
    y = dlg_info['y']
    Y = dlg_info['Y']

    return ['x', 'y', 'Y', x, y, Y]
# end def get_colour


# Set program runtime constants
BG_COLOUR  = [-0.5, -0.5, -0.5]
SHAPE_SIZE = 4.0

# Set the RGB values for display
RGB_VALS = [[255, 0, 0],
            [0, 255, 0],
            [0, 0, 255],
            [40, 40, 40],
            [90, 90, 90],
            [140, 140, 140],
            [190, 190, 190],
            [240, 240, 240]]

# Set RGB test values for display
RGB_TEST = [[200, 200, 100],
            [100, 100, 200],
            [200, 100, 50],
            [25, 150, 250],
            [150, 50, 25],
            [175, 250, 50],
            [25, 10, 50]]

# Define the visual window where the colour stims will appear
win = visual.Window(fullscr=True, screen=0, allowGUI=False, allowStencil=False,
                    monitor='vcnLab', color=BG_COLOUR, colorSpace='rgb',
                    units='deg')

# Define the shape stim that will change colour
shape = visual.Rect(win, width=SHAPE_SIZE, height=SHAPE_SIZE, 
                    LineColor=BG_COLOUR, lineColorSpace='rgb')

# Define the text window to display the colour RGB value
text = visual.TextStim(win=win, ori=0, name='text', text="", font=u'Arial',
                       pos=[-15,15], height=.5, color=u'white',
                       colorSpace=u'rgb', opacity=1, depth=-1.0)

# Define the dictionary for user input
dlg_info = {'x':'', 'y':'', 'Y':''}

# Draw the shape and text stims to the screen
shape.setAutoDraw(True)
text.setAutoDraw(True)

output = []

# Loop through each of the RGB values
for col in rgbvals:
    output.append(get_colour(win, shape, text, col, dlg_info))

# Loop through each of the RGB test values
for col in rgbtest:
    output.append(get_colour(win, shape, text, col, dlg_info))