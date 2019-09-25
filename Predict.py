from knn import KNN
import numpy as np
import matplotlib.pyplot as plt
knn = KNN()
knn.Load_Dataset('iris.csv')



x = knn.data[:,0]
y = knn.data[:,1]
##iris_names = ["iris setosa", "iris versicolor", "iris virginica"]
##for i in range(0,3):
##    num_of_flowers = 0
##
##    for j in knn.target:
##        if j == i:
##            num_of_flowers += 1
##
##    print("number of flowers of type "+iris_names[i]+" = "+str(num_of_flowers))

trainX = knn.data[::2,1:3]
trainy = knn.target[::2]
testX = knn.data[1::2,1:3]
testy = knn.target[1::2]

#applying KNN
knn.Use_K_Of(15)
knn.Fit(trainX,trainy)
for i in range(len(testy)):
    actualClass = testy[i]
    prediction = knn.Predict(testX[i,:])
    #print(actualClass, prediction)


plt.figure()
#colors
colors = np.zeros((3,3),dtype='f')
colors[0,:] = [1,0.5,0.5]
colors[1,:] = [0.5,1,0.5]
colors[2,:] = [0.5,0.5,1]

##plt.scatter(trainX[:,0],trainX[:,1],c=trainy)
##plt.scatter(testX[:,0],testX[:,1],c=testy)

[numItems,numFeatures] = knn.data.shape
for i in range(0,numItems/2):
    itemClass = int(trainy[i])
    currColor = colors[itemClass,:]
    facecolor=currColor
    s=50
    plt.scatter(trainX[i,0],trainX[i,1],s=s, c=facecolor, edgecolors='black')

correctCount = 0
for i in range(0,numItems/2):
    itemClass = int(trainy[i])
    currColor = colors[itemClass,:]
    facecolor=currColor
    s=50
    prediction = int( knn.Predict( testX[i,:] ) )
    edgeColor = colors[prediction,:]
    plt.scatter(testX[i,0],testX[i,1],s=s, c=facecolor, edgecolors=edgeColor)

    if (prediction == itemClass):
        correctCount+=1
correctPercent = (float(correctCount)/(numItems/2))*(100)
print correctPercent

plt.show()

