import pandas as pd
from textblob import TextBlob

names_list = []

purpose_list = []

with open("output-hw3.txt","r") as fp:
    data6 = fp.readlines()

for line in data6:

    if line.startswith("Name"):
        names_list.append(line[6:-1])

    if line.startswith("Purpose"):
        purpose_list.append(line[10:-1])

        
polarity_list = [TextBlob(x).sentiment[0] for x in purpose_list]
data7=pd.DataFrame({'names':names_list,'purpose':purpose_list,'polarity':polarity_list})
print(data7.sort_values('polarity')[['names','polarity']])

with open("ReadMe.txt",'w') as out_file:
    line_a = ["on the first script, I set 5 similar parts can let user input their documents. And I set 5 because there are 5 files in this case. And the following codes will merge the files to a same format, and output to a txt document"]
    line_b = ["on the second script, in order to find the most common words, I make my codes fix all the 'purpose 'line together to a new file.in other cases, user can replace 'purpose' to any other variable they want. Next, input this new file which only contain the line we just selected, like 'purpose', can help user to find the most common words."]
    line_c = ["on the third script, user's file will be divided to different set by their variables automatically. In this case, there are two variable: Name and Purpose, So the codes also have two set with same name. And the packages will help people to calculate the polarity, and sorting codes can find the best and wost result base on the polarity in the end."]
    res = ""
    res+=str(line_a)
    res += "\n"
    res+=str(line_b)
    res += "\n"
    res+=str(line_c)
    out_file.write(res)

