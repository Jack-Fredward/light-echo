READ ME FOR Lamppost_v_1.3.py
written for python3
this code is designed to calculate the time delay of light echos of black hole bianary star systems

INPUT
directly follow the file name seperated by a space the code will take 8 arguments
for the output options and the input of the model parameters

python3 Lamppost_v_1.3.py nor h radius nob obsx obsy obsz debug csv hpng lpng
python3 Lamppost_v_1.3.py #ofrays height radius #ofbins obsx obsy obsz debug csv histogrampng modelpng
see below for data types and option results


debug option if yes then graphs will be generated
either a Y/y or N/n answer

csv option if yes then will produce a csv of hist data
either a Y/y or N/n answer

hpng = historgram png option if yes then will save histogram as png
either a Y/y or N/n answer

lpng = lamppost model option if yes then will save graph of lamppost model as png
either a Y/y or N/n answer

nor = number of rays
an integer

nob = number of bins
an integer

observer location
obsx = x coord
obsy = y coord
obsz = z coord


constants for height and radius in meters
height = h is a float
radius = radius is a float

OUTPUT
delay is given in seconds
