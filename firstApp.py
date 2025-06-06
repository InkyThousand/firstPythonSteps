myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]
for item in myMixedTypeList:
    print("{} is of the data type {}".format(item,type(item)))

myList = [4, 123.12, True, "Pavel",]

for item in myList:
    print(item, " is " , type(item)) 

# What is time now
import time
currentTime = time.localtime()
print("Current time is: {}:{}:{}".format(currentTime.tm_hour, currentTime.tm_min, currentTime.tm_sec))

# loop 1 to 10
