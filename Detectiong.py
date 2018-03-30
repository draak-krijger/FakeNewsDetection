import csv
from sklearn import svm
import matplotlib.pyplot as plt

X = []
Y = []


with open('vector.csv',encoding="utf8") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    flag = False 
    
    for row in readCSV:
        if flag:
            dic = row[0].split(' ')
            tarr = []
            tmp = []
            
            for value in dic:
                if len(value) > 0 :
                    tarr.append(int(value))
            
            #for i in range(2):
                #tmp.append(tarr[i]-tarr[i+1])
                
            X.append(tarr)
            
            tarr = []
            tarr.append(int(row[1]))
            Y.append(tarr)
            
        else:
            flag = True

train_x = []
test_x = []

train_y = []
test_y = []

total = len(Y)
train = total*0.8

for i in range(total):
    if i < int(train) :
        train_x.append(X[i])
        train_y.append(Y[i][0])
        #plt.plot(X[i][0],X[i][1],'x')
        
    else:
        test_x.append(X[i])
        test_y.append(Y[i][0])
        #plt.plot(X[i][0],X[i][1],'o')
        
# =============================================================================
#     if Y[i][0] == 0 :
#         plt.plot(X[i][0],X[i][1],'ro')
#     else:
#         plt.plot(X[i][0],X[i][1],'go')
#         
# plt.show()
# =============================================================================
#classifier = svm.SVC()
classifier = svm.SVC(kernel='rbf')
#classifier = svm.LinearSVC()
#classifier = svm.SVR()
classifier.fit(train_x,train_y)

true_positive = 0 
true_negative = 0 
false_positive = 0 
false_negative = 0 

predict = classifier.predict(test_x) 

for i in range(total-int(train)):
    if test_y[i] == 1 :
        if predict[0] == 1:
            true_positive = true_positive + 1
        else:
            true_negative = true_negative + 1
    else:
        if predict[0] == 0:
            false_negative = false_negative + 1
        else:
             false_positive = false_positive + 1

# =============================================================================
# print(total-int(train))
# print("Confution Matrics")            
# print("    ","TRUE","FALSE")
# print("TRUE",true_positive,true_negative)
# print("FALSE",false_positive,false_negative)
# =============================================================================

accuracy = (true_positive+false_negative)/(true_negative+true_positive+false_negative+false_positive)

print("accuracy",accuracy*100)
