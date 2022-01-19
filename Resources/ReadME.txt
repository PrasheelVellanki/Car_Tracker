Hey there, this repository includes a highway footage video from youtube 
as the default media source. You can add your own footage to the resources file and
its appropriate PATH inside Car_Tracker.

The object_detection.py is a pre-trained YOLO v4 model for car recognition I found online. Sadly, the model is too large even when compressed to add to github.
I've used OpenCV to visualize the tracking in the Car_Tracker file.

Please check requirement.txt for any downloads you may need to create the required environment.

For the future, I'm planning to improve the readability of my code with some comments, and expand
upon this project to include car speeds, possible pedestrian detection, and multi-threading to increase
frame rate.
