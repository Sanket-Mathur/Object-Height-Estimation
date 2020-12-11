# Object-Height-Estimation

This is a project based on opencv-python which estimates height of an object based upon its picture. It uses a the height reference of a standard object that is recognised by the system and must be in the frame of the object to be measured standing parallel to it.

## Problem Definition

The objective of this project is to give estimates of height of an object without need to measure it, using a picture of that object in parallel to a fixed standard measure. It can be useful of various purposes like estimating height of buildings, trees, and industrial vehicles which can take a lot of time and effort if done manually.

The project includes a desktop application and a mobile application, both of which can be used to estimate height of the object using images either clicked by the camera or by importing an image from the gallery. However, the desktop application does provide a lot more flexibility on how to use the application including changing the standard measure that will be used by the application as a reference to also select any part of the image that is to be measured.

## The Proposed System

The proposed system is described in the steps as follows:

Step 1. The first step will include user either capturing or importing the image of the object that they want to measure.  
Step 2. The next step will be to identify the standard in the image, this will be done in two sub-parts  
&emsp;Step 2.1 Filtering the color of the object that we want to recognize from the image.  
&emsp;Step 2.2 Checking the edges of the object that are left on the masking layer after filtering out the excess, unnecessary colors.  
&emsp;Step 2.3 Marking the object with correct number of edges (4 in this case) and using its height for further calculation.  
Step 3. The third step will be to asking the user about the object that he wants to measure from the image that he has selected. This will be done by the user by marking two points on the image representing the height that is to be measured.  
Step 4. The last step will be to comparing the height (in px) that the user has selected to the reference height. The reference height is set to be 1m by default thus, the required height will be the ratio of the reference height.

## Technology Used

The software is only tested on Linux environment as of writing this report. The packages to be installed for execution of the software are Python with some of its libraries installed (OpenCV, NumPy, tkinter and flask), Flutter and Android Studio (or VS Code) integrated with the flutter installation and including flutter plugin and dart plugin. The android application uses a REST API which is required to be started before using the applications such that a HTTP communication can be established.

The major technologies associated with the project as represented in the tree as follows:

    • Python
        ◦ numpy
        ◦ cv2 (OpenCV)
        ◦ tkinter
        ◦ flask
        ◦ json
        ◦ base64
        ◦ pickle
    • Dart
        ◦ Flutter
        ◦ Additional Packages
            ▪ cupertino_icons v1.0.0
            ▪ http v0.12.2
            ▪ image_picker v0.6.7+12
    • IDE and Text Editors
        ◦ VS Code
        ◦ Android Studio
    • Version Control
        ◦ git
        ◦ GitHub


