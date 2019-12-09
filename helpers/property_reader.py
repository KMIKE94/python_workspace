import os
import re
import sys
import subprocess
import requests
from bs4 import BeautifulSoup

def search(apiVersion):
    # apiVersion = "4.3"
    home = os.getenv("HOME")
    prepend = home + ""
    instance = ""
    directories = os.listdir(prepend)
    instanceSearchKey = ""
    versionKey = ""

    percentage = 0
    counter = 0
    length_of_directories = len(directories)
    agency_id_list = []
    for d in directories:
        counter = counter + 1
        if d != ".DS_Store":
            process = subprocess.check_output(["sed -n 's/^" + instanceSearchKey + "//p' " + prepend + d + "/" + instance], shell=True)
            try:
                response = requests.get(process, timeout=15)

                if response.status_code == 200:
                    soup = BeautifulSoup(response.content, "html.parser")
                    sierraVersion = soup.body.findAll(text=re.compile(versionKey))  
                    if apiVersion in str(sierraVersion[0]):
                        agency_id_list.append(d)
            except requests.RequestException as e:
                print("Requests exception", e)
        decimal = round((float(counter) / float(length_of_directories)) * 100)
        print( str(decimal) + "%")
    
    for agency_id in agency_id_list:
        print(agency_id)

if __name__ == "__main__":
    print("Takes one argument that must be a number to represent the Sierra api version.\n" +
        "An example might be: python property_reader.py 4.3")
    if len(sys.argv) != 2:
        print("Error - please see usage")
    else:
        search(sys.argv[1])