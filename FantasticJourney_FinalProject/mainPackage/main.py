#Name: Olivia Scott, Ebun Obisesan, and Kairal Johnson
#email: scottom, obiseseo, johns7kj (@mail.uc.edu)
#Assignment Title: Final Project
#Course: IS 4010
#Semester/Year: Spring 2023
#Brief Description: Scavenger Hunt
#Citations: 
#Anything else that's relevant:


from PIL import Image
import json

# Read english.txt File
with open('english.txt', 'r') as e:
    readFile = e.read()
    
my_list = readFile.split('\n')
english = list(filter(None, my_list))

#print(english)

#Upload json File
with open('EncryptedGroupHints Spring 2023 Section 002.json') as f:
    indexes = json.load(f)

#Index json file and english.txt
if "Fantastic Journey Group" in indexes:
    idx_list = indexes["Fantastic Journey Group"]
    for idx in idx_list:
        idx = int(idx) - 1
        if idx < len(english):
            print(english[idx])
        else:
            print(f"Index {idx} is out of range for the english list.")
else:
    print("Fantastic Journey Group not found in the JSON file.")

#Upload Image
groupImage = Image.open('groupPhoto.jpg')
groupImage.show()