import csv
a=[]
with open('Dataset1.csv') as csfile:
    reader = csv.reader(csfile)
    for row in reader:
        a.append(row)
        print(row)
num_attributes=len(a[0])-1

print("The most general hypothesis:",["?"]*num_attributes)
print("The most specific hypothesis:",["0"]*num_attributes)

hypothesis=a[0][:-1]
print("\n Find S: Finding a maximally specific hypothesis")
for i in range (len(a)):
    if a[i][num_attributes] == "Y":
        for j in range(num_attributes):
            if a[i][j]!=hypothesis[j]:
                hypothesis[j]='?'
    print("The training example no:",i+1," the hyposthesis is:",hypothesis)
print("\n The maximally specific hypohthesis for training set is")
print(hypothesis)

testCase = input("Enter Test Case : \n")
testCase = testCase.split(",")
print ("Test Case : ")
print (testCase)
acceptFlag = 1

for i in range(len(hypothesis)):
    if hypothesis[i] != '?':
        if hypothesis[i] != testCase[i]:
            acceptFlag = 0
            break
if acceptFlag == 1:
    print ("Hypothesis Accepted")
else : 
    print ("Hypothesis Rejected")
