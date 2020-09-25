import pickle, matplotlib.pyplot as plot, numpy as np

with open('data.pkl', 'rb') as file:
    data = pickle.load(file)

key_list = list(data.keys())
val_list = list(data.values())

def plotmypie():
    plot.pie(val_list, labels=key_list, autopct='%1.1f%%')
    plot.axis('equal')
    plot.show()

def plotmybar():
    index = np.arange(len(key_list))
    plot.bar(index, val_list)
    plot.xlabel('Subject', fontsize=10)
    plot.ylabel('Marks Obtained', fontsize=10)
    plot.xticks(index, key_list, fontsize=8)
    plot.title('Report Card')
    for i, data in enumerate(val_list):
        plot.text(x=i-.12, y =data+1 , s=f"{data}" , fontdict=dict(fontsize=10))
    plot.show()

plotmypie()
plotmybar()