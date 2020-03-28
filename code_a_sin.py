import numpy as np
import operations as op

startvalue = np.random.uniform()
numberofgenerated = 70
numberofadditional = 30
x_array = np.array([])
y_array = np.array([])

for i in range(numberofgenerated):
    new_value = np.pi * np.random.uniform(startvalue, startvalue + 1)
    while new_value in x_array:
        new_value = np.pi * np.random.uniform(startvalue, startvalue + 1)
    x_array = np.append(x_array, new_value)
    y_array = np.append(y_array, np.absolute(np.sin(np.take(x_array, i))))
xlist = op.convertion(x_array, numberofgenerated)
ylist = op.convertion(y_array, numberofgenerated)
print(x_array)
print(y_array)
print(xlist)
print(ylist)

learndata = open("learndata.txt", "w+")
for i in range(len(xlist)):
    learndata.write(op.make_spaceboard(xlist[i]) + " ")
    learndata.write(op.make_spaceboard(ylist[i]) + '\n')
learndata.close()
for i in range(numberofadditional):
    new_value = np.pi * np.random.uniform(startvalue, startvalue + 1)
    while new_value in x_array:
        new_value = np.pi * np.random.uniform(startvalue, startvalue + 1)
    x_array = np.append(x_array, new_value)
    y_array = np.append(y_array, np.absolute(np.sin(np.take(x_array, i))))
xlist = op.convertion(x_array, numberofgenerated+numberofadditional)
ylist = op.convertion(y_array, numberofgenerated+numberofadditional)


testdata = open("testdata.txt", "w+")
for i in range(len(xlist)):
    testdata.write(op.make_spaceboard(xlist[i]) + " ")
    testdata.write(op.make_spaceboard(ylist[i]) + '\n')
testdata.close()
