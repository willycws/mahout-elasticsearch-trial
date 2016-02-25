import fileinput
from string import join
import json
import csv
import json
### read the output from MAHOUT and collect into hash ###
with open('/home/osboxes/Downloads/mahout-trial/mloutput/part-r-00000','rb') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter='\t')
    old_id = ""
    indicators = []
    update = {"update" : {"_id":""}}
    doc = {"doc" : {"indicators":[], "numFields":0}}
    for row in csv_reader:
        id = row[0]
        if (id != old_id and old_id != ""):
            update["update"]["_id"] = old_id
            doc["doc"]["indicators"] = indicators
            doc["doc"]["numFields"] = len(indicators)
            print(json.dumps(update))
            print(json.dumps(doc))
            indicators = [row[1]]
        else:
            indicators.append(row[1])
        old_id = id
