#prompt the user to enter 5 numbers. Store them in a list.
#Display the list as entered, small to large, and large to small
#Calculate and display the mean and median
#This is a guided practice. You can follow the video or your instructor will go
#over this in class

theList = []
#What allows people to type in numbers, range makes it repeat
for i in range(5):
    theList.append(int(input("Number {i+1}:")))

print("as entered: " + str(theList))
#Sort...sorts it, reversing it does biggest to smallest but normally does small to large
theList.sort()

print(f"small to large: {theList}")

theList.sort(reverse=True)

print(f"Large to small: {theList}")
#Median, no need for math, it's the middle of the sorted list
median = theList[2]

sum = 0

for i in range(5):
    sum += theList[i]
mean = sum / 5

print(f"The median is {median} and the mean is {mean}")
