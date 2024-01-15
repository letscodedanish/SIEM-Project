from pymongo import MongoClient
import re

client=MongoClient('localhost',27017)
db = client['project_db']
collection1 = db['dev_log2']

linux_pattern = r"""\"<(\d+)>([a-zA-Z]*) (.)([0-9]) (\d{2}:\d{2}:\d{2}) (\w*) ([a-z]*) ([a-zA-Z]*|([a-z]*[-][a-z][^[]*))([)([0-9]*)(]|): (.*)"""
mac_pattern=r"""\"<(\d+)>(\d+): [*|.]([a-zA-Z]*) (.)([0-9]) (\d{2}:\d{2}:\d{2}(|([.]\d*))): %([A-Z]*)-([0-9])-(\w*):(.*)"""

def parsing(filename):
    acount,exception_count,line_count,ncount=0,0,0,0
    doc_list=[]
    linux=0
    mac=0
    doc_dict={}
    with open(filename, 'r') as logfile:
        
        lines=logfile.readlines()
        line_count+=1

        for l in lines:     
            try:
                matches1=re.findall(linux_pattern,l)
                matches2=re.findall(mac_pattern,l)
                if len(matches1):
                    doc_dict={
                        'month':matches1[0][1],
                        'date' : matches1[0][2] + matches1[0][3],
                        'time' :matches1[0][4],
                        'hostname' :matches1[0][5],
                        'severity' :matches1[0][6],
                        'app_name' :matches1[0][7],
                        'message' :matches1[0][-1]
                    }
                    linux+=1
                elif len(matches2):
                    doc_dict={
                        'month':matches2[0][2],
                        'date' : matches2[0][3] + matches2[0][4],
                        'time' :matches2[0][5],
                        'hostname' :matches2[0][10],
                        'severity' :matches2[0][9],
                        'app_name' :matches2[0][8],
                        'message' :matches2[0][-1]
                    }
                    mac+=1
                acount+=1
                doc_list.append(doc_dict)
                print(doc_dict)
                if acount==5:
                    collection1.insert_many(doc_list)
                    print(line_count, "-------------------")
                    acount=0
                    doc_list.clear()
                print("linux ",linux)
                print("mac ",mac)
                print("not",ncount)
            except:
                exception_count+=1
                print(line_count," Lines processed 1")
                
    if len(doc_list)>1:
        collection1.insert_many(doc_list)
        print(line_count, "lines processed")
        doc_list.clear()            
   
if __name__ == '__main__':
    parsing('C:\\project\\data6.csv')
