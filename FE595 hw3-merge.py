with open("output.txt","r") as fp:
    data = fp.read()
    
with open("output-1.txt","r") as fp:
    data1 = fp.read()

with open("web_scrape.txt","r") as fp:
    data2 = fp.read()

with open("inputs.txt","r") as fp:
    data3 = fp.read()

with open("companies.txt","r") as fp:
    data4 = fp.read()
data += "\n"
data += data1
data += "\n"
data += data2
data += "\n"
data += data3
data += "\n"
data += data4


#for data clean, I remove the unimport characters like "[]", in order to make the data looks consistent
data = data.replace('[','')
data = data.replace(']','')
data = data.replace(':',',')
data = data.replace("'","")
for i in range(50):
    data = data.replace(str(i),'')


with open ('output-hw#3.txt', 'w') as fp: 
    fp.write(data) 
