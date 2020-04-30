import requests
import cv2
import os
import csv
import sys
             
pathname = os.path.abspath(sys.argv[0])         
base_path = os.path.abspath(os.path.dirname(os.path.dirname(pathname)))

prop_file = open(os.path.join(base_path,'csvs\\kritik.csv'), 'r')
csv_reader = csv.reader(prop_file)
counter = 0
for row in csv_reader:
    try:
            coded_url = row[0]
            r = requests.get(coded_url)
            with open(os.path.join(base_path,"data\\training_images\\non-violent\\" + str(counter) + ".png"),'wb') as f: 
                f.write(r.content)
            print( str(counter) + " Non-violent Image(s) Downloaded ", end = "\r")
            counter = counter + 1
    except Exception as e:
            print(e)
            print("Failed to download url number :-", end = " ")
            print(counter)

print()

counter = 0
prop_file = open(os.path.join(base_path,'csvs\\tanya.csv'), 'r')
csv_reader = csv.reader(prop_file)        
for row in csv_reader:
    try:
            coded_url = row[0]
            r = requests.get(coded_url)
            with open(os.path.join(base_path,"data\\training_images\\violent\\" + str(counter) + ".png"),'wb') as f: 
                f.write(r.content)
            print( str(counter) + " violent Image(s) Downloaded ", end = "\r")
            counter = counter + 1
    except Exception as e:
            print(e)
            print("Failed to download url number :-", end = " ")
            print(counter)

print()