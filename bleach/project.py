import os
import shutil

def main():

    src = os.path.realpath("bleachEpub")
    root_dir, tail = os.path.split(src)

    if not os.path.isfile("bleach.epub"):

        fileName = shutil.make_archive("bleach", 'zip', tail)
        base = os.path.splitext(fileName)[0]

        target = base + '.epub'
        os.rename(fileName, target)

    else: 
        os.remove("bleach.epub")

        fileName = shutil.make_archive("bleach", 'zip', tail)
        base = os.path.splitext(fileName)[0]

        target = base + '.epub'

        os.rename(fileName, target)


    os.startfile(r'C:\Users\ahmet\Desktop\bleach\bleach.epub')


if __name__ ==  "__main__":
    main()