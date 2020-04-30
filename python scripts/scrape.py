import requests
import cv2
import os
import csv
import base64

prop_file = open('1.csv', 'r')
csv_reader = csv.reader(prop_file)
counter = 0
for row in csv_reader:
    try:
            coded_url = row[0]
            image_url = base64.b64decode(coded_url)
            r = requests.get(image_url)
            with open(str(counter) + ".png",'wb') as f: 
                f.write(r.content)
            counter = counter + 1
    except Exception as e:
            print(e)
