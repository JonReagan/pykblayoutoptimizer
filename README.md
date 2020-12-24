# pykblayoutoptimizer

## About 
PyKBLayoutOptimizer - The Python Keyboard Layout Optimizer - find suggested keyboard layout based on your writing patterns.

This script provides a suggested keyboard layout based on your writing style.  Specifically, this 
script imports a selection of your writing in the form of a .txt document.  Then, the script 
parses this text providing a total character count.  Based on the frequency of letters in your writing,
the script provides a suggested layout, in semi-graphical form where keys are indicated by the following
format:  **| (a, 20) |**

Each key is contained in the "|" characters, and inside you can see the suggested letter ("a" in our expample)
and the count of the total number of times that character appears in your text ("20" in our example).  

This application is released under the GPLv3 license.  Please see the LICENSE file for a copy of the license. 

## Requirements 
* Python 3 - this app has been build using Python 3.8.  It uses the "collections" and "string" built-in modules.

## How to Use  
When you run this script, a prompt will ask for the file that you would like to use to create your suggested keyboard layout.  
Type the entire directory, including the file and extension.  **At this time, only .txt files are supported. Please convert
your writing sample to .txt if needed.**

For example, you could write /home/user/helloworld.txt if on Linux, or C:\Users\UserName\Documents\HelloWorld.txt on Windows.
Hit "Enter" on your keyboard once you have entered the file location name.  Depending on the size of the file, it may take up 
to 30 or more seconds to compute your suggested optimized keyboard layout.
