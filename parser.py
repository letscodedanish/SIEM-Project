from pymongo import MongoClient
import re
import csv


client=MongoClient('localhost',27017)
db = client['project_db']
collection1 = db['win2_log']
sev_list=["emerg(0)","alert(1)","crit(2)","err(3)","warning(4)","notice(5)","info(6)","debug(7)"]
sev_dict={"E":"emerg(0)","A":"alert(1)","C":"crit(2)","err":"err(3)","W":"warning(4)","N":"notice(5)","I":"info(6)","D":"debug(7)"}

month_list=["Jan","Feb","Mar","Apr","May","June","July","Aug","Sep","Oct","Nov","Dec"]

win2_pattern ="(\d{2}.\d{2}.\d{3}.\d{2}) <(\d+)>(\d+) (\d{4})-(\d{2})-(\d{2})[T](\d{2}:\d{2}:\d{2})[+](\d{2}:\d{2}) (\d{2}.\d{2}.\d{3}.\d{2}) ([A-Z]*) - (\w*) - %([A-Z]*)-([A-Z])-(\w*): (.*)"
win1_pattern ="(\d{2}.\d{2}.(\d{3}|\d{2}).(\d{3}|\d{2})) <(\d+)>(\d+): ([*|.]([a-zA-Z]*)|([a-zA-Z]*)) (.)([0-9]) (\d{2}:\d{2}:\d{2}(|([.]\d*))): %([A-Z]*)-([0-9])-(\w*):(.*)"
while True:
    doc_list=[]
    doc_dict={}
    if len(list(csv.reader(open(r'window_logs.csv'))))==3:
        fp=open("window_logs.csv","r+")
        lines=fp.readlines()
        fp.close()
        fp=open("window_logs.csv","w")
        fp.close()
    elif len(list(csv.reader(open(r'window_logs2.csv'))))==3:
        fp=open("window_logs2.csv","r+")
        lines=fp.readlines()
        fp.close()
        fp=open("window_logs2.csv","w")
        fp.close()
    else:
        continue
    print(lines)
    print("in loop-1")
    try:
        for l in lines:
            try:
                print('in try block')
                matches1=re.findall(win2_pattern, l)
                matches2=re.findall(win1_pattern,l)
                if len(matches1):
                    print('in if block')
                    doc_dict={
                        'ip_addr':matches1[0][0],
                        'month':month_list[int(matches1[0][4])-1],
                        'date' : matches1[0][5],
                        'time' :matches1[0][6],
                        'facility':matches1[0][11],
                        'mnemonic' :matches1[0][13],
                        'severity' :sev_dict[(matches1[0][12])],
                        'message' :matches1[0][-1]
                    }
                    print(doc_dict)
                    doc_list.append(doc_dict)
                elif len(matches2):
                    print('in if block2')
                    doc_dict={
                        'ip_addr':matches2[0][0],
                        'month':matches2[0][5],
                        'date' : matches2[0][8] + matches2[0][9],
                        'time' :matches2[0][10],
                        'facility':matches2[0][13],
                        'mnemonic' :matches2[0][15],
                        'severity' :sev_list[int(matches2[0][14])],
                        'message' :matches2[0][-1]
                    }
                    print(doc_dict)
                    doc_list.append(doc_dict)
            except:
                continue
        collection1.insert_many(doc_list)
    except:
        continue
