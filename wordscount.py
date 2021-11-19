import pandas as pd
import string

sample= input('Enter your text file path \nPlease, remember to put slashes to the right : ')
mytxt=open(sample, 'r').read()
mytxt=mytxt.translate(str.maketrans('', '', string.punctuation))
mylist=mytxt.split(' ')
a=(map(lambda i: i.lower(), mylist))
mylist=list(a)
mydata=pd.DataFrame(columns=('Words', 'Count'))

for i in range(len(mylist)):

    if mylist[i] not in list(mydata['Words']):
        newrow={'Words': mylist[i], 'Count': mylist.count(mylist[i])}
        mydata=mydata.append(newrow, ignore_index=True)

print(mydata)
