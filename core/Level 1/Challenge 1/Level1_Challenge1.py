import pickle
file = open("data.pkl", "rb")
for i, msg in enumerate(pickle.load(file)):
    print(f"({i+1}) {msg}")
file.close()