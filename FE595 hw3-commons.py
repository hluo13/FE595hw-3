from collections import Counter 

with open("output-hw#3.txt","r") as fp:
    data5 = fp.readlines()

purpose = list()
for item in range(0,len(data5)):
    if data5[item][0]=='P':
        purpose.append(data5[item])


with open("purpose.txt",'w') as out_file:
        for t in range(len(purpose)):
            res=""
            res += str(purpose[t])
            res += "\n"
            out_file.write(res)

with open("purpose.txt","r") as fp:
    data6 = fp.read()

split_it = data6.split() 
Counter = Counter(split_it) 
most_occur = Counter.most_common()


#Since the first output is the title of the data. So I generate 11 most common words.
print(most_occur[0:11])
