import pickle
def updatefile(name, number):
    mydict["planet_name"].append(name)
    mydict["planet_number"].append(number)
    print("After Updation => ")
    sendtofile(mydict)

def sendtofile(data):
    file = open('data.pkl', 'wb')
    pickle.dump(data, file)
    file.close()
    getfromfile()

def getfromfile():
    with open('data.pkl', 'rb') as file:
        print("Data in File: " + str(pickle.load(file)))

mydict = {"planet_name": ["Earth", "Mars"], "planet_number": [3, 4]}
print("Before Updating =>  ")
sendtofile(mydict)
# updatefile("Jupiter", 5)
