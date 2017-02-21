#**Finding Lane Lines on the Road** 
---

**Finding Lane Lines on the Road**

The goals / steps of this project are the following:

* Make a pipeline that finds lane lines on the road


[//]: # (Image References)

[image1]: ./examples/grayscale.jpg "Grayscale"

---

### Project Approach steps by steps
1. Importing all the required library for image processing and computaion.
2. We have several helper functions to compute all the complex calculation out of the class. Details of those functions are given below: </br>
   a. grayscale(img): This function takes a RGB image and convert into grayscale image.</br>
   b. canny(img,low_threshold,high_threshold): It detects the edge of the image by using canny edge detection algorithm. </br>
   c. gaussian_blur(): It blurs the images. </br>
   d. region_of_interest(img, vertices): It find the region where we are looking for the lanes. </br >
   e. draw_lines(img, lines, color=[255, 0, 0], thickness=10): Draw the lines after finding the lane. </br>
   f. hough_lines(...): This method finds the lines cordinate for distinguishing the lane. 
3. After finding edge from the gray scale image and bluring, I had to find the region of interest. To do that I used the constant cordinate of the image. such as [(0,imshape[0]),(450, 320), (490, 320), (imshape[1],imshape[0])]. Hough Lines method helps to find all the cordinates of the line. Then I had to draw the line what gives us lanes. 
4. Drawing solid line to identify the left and right lane, From my points of interest, I identify a particular point in x cordinates what seperates both lanes. Then I create two list of line cordinates (got from hough line). Then by using min and max value of x,y, found two points and draw the solid line. 

![alt tag][https://github.com/nanofaroque/SelfDrivingCar/blob/master/Term1/Lesson_2_Finding_Lanes/CarND-LaneLines-P1/test_images/solidWhiteCurve.jpg]


###2. Potential shortcomings 
One of the potential challenge would be how it will work in curve road. 
One of the video, it shows some weird lane detections. 


###3. Improvements

Mentioning the details of the codebase and steps.