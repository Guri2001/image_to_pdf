import os, sys
from PIL import Image


desktop_path = os.environ['USERPROFILE'] + "\Desktop"


def convert():
    name_of_file = input("Name of file: ")
    img_path = input(r"Enter path of file: ")
    image_1 = Image.open(img_path)
    convert = image_1.convert("RGB")
    convert.save(desktop_path + "\\" + name_of_file + ".pdf")
    print("Conversion successful file stored as PDF at location: " + desktop_path + "\nWith file name: " + name_of_file +"\n")

if __name__ == "__main__":
    while(1):
        convert()
        user = input("Do you want to stop? 'yes' or no': ")
        if(user.lower() == "no"):
            continue
        if(user.lower() == "yes"):
            break

        if(user.lower() != "yes" or user.lower != "no"):
            user = input("Do you want to stop? 'yes' or no': ")

