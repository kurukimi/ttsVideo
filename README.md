# ttsVideo

### What?
Program to help creating text to speech videos from images (and videos) and upload them easily to e.g. youtube.
### State
Early development
### Implementation
The UI is currently being created with PyQt, because it is fast to develop with in general. It however doesn't have 
many other good attributes for implementing a desktop or webapp. The project might shift to using Typescript and something like Electron to build it.



The processing side uses Python and pyTesseract. Python is a valid choice for such processing due to easy access to powerful libraries.
pyTesseract will probably need to be enhanced or replaced due to current inaccuracy. 


Overview of the UI flow
![image](https://github.com/kurukimi/ttsVideo/assets/88735086/fa3786d6-d5d3-4739-8634-daf9d4b9d6c6)
### Why?
Because I was bored and had an idea. (tts ytubers make big bank)
### To Who?
Currently for my own fun and laughs.

### Development
#### Requirements
Both processing and UI side use Python3.11. PyQt is needed for now for the UI.\
The project is going to try to implement some image to text functionality. To achieve such functionality, for now it uses Tesseract, but it might change since
the accuracy isn't great.\
It is a good idea to install all python packages in requirements.text to a virtual environment such as venv.


### Project Structure
- [Processing](https://github.com/kurukimi/ttsVideo/tree/main/processing), includes the processing e.g. rendering the video, image to text etc.
- [Frontend](https://github.com/kurukimi/ttsVideo/tree/main/frontend) PyQt based user interface
