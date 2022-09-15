import pandas as pd
import numpy as np
import datetime

#create an empty list
chat = []

#read the text file
#replaace 'chat_text_name' with the name of the whatsapp chat file
with open('chat_text_name', mode='r', encoding='utf8') as c:
    data = c.readlines()
    
#android - this loop reads the lines in 'data' and splits them into columns    
for line in data:
    date = line.split(",")[0]
    time = line.split("-")[0].split(",")[-1]
    name_num = line.split("-")[-1].split(":")[0]
    message = line.split("-")[-1].split(":")[-1]
    
#iPhone - this loop reads the lines in 'data' and splits them into columns
#for line in data:
    #date = line.split("]")[0].split(",")[0]
    #time = line.split("]")[0].split(",")[-1]
    #name_num = line.split("]")[-1].split(":")[0]
    #message = line.split("]")[-1].split(":")[-1]

#append the split data into the empty list    
    chat.append([date, time, name_num, message])
    
#create a data frame with columns as required    
df = pd.DataFrame(chat, columns = ['Date', 'Time', 'Name/Number', 'Message'])

#cleaning the date column
df['Date'] = df["Date"].str.replace('[', '').replace('.', '')

#export to excel
#replace 'new_chat' with the name for output file
df.to_excel("new_chat.xlsx", index = False)