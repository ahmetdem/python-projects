import os
import shutil
import glob
from zipfile import ZipFile

#Change Epub to zip
epubDir = r'C:\Users\ahmet\Documents\GitHub\python-projects\changeEpubSettings\Coral of the Moon.epub'
epubName = list(epubDir.split('\\'))[-1]
newName = epubName.replace(".epub" , ".zip")

os.rename(epubName, newName)

#Extract The zip
folderName = epubName.replace(".epub", "")
zipPath = r'C:\Users\ahmet\Documents\GitHub\python-projects\changeEpubSettings' + "\\" + folderName

with ZipFile(r"C:\Users\ahmet\Documents\GitHub\python-projects\changeEpubSettings\Coral of the Moon.zip", 'r') as zObject:
    zObject.extractall(
        path = zipPath
    )

# Find the styles
files = glob.glob(
    r'C:\Users\ahmet\Documents\GitHub\python-projects\changeEpubSettings\Coral of the Moon\**\*.css', 
    recursive = True
)

for file in files:
    if "style" in file.split("\\")[-1]:
        cssFile = file

cssFileName = cssFile.split("\\")[-1]

#change the former style with the new one
os.remove(cssFile)

shutil.copy(r'C:\Users\ahmet\Documents\GitHub\python-projects\changeEpubSettings\stylesheet.css',
            r'C:\Users\ahmet\Documents\GitHub\python-projects\changeEpubSettings\Coral of the Moon\OEBPS\Styles' + "\\" + cssFileName)


src = r'C:\Users\ahmet\Documents\GitHub\python-projects\changeEpubSettings\Coral of the Moon'
n = shutil.make_archive(folderName + "-Test", "zip", src)

os.rename(n, epubName)
os.startfile(epubName)

# def main():

#     src = r'C:\Users\ahmet\Desktop\Masaüstü\Japon\LightNovels\Mushoku Tensei\mushoku'

#     if not os.path.isfile("mushoku.epub"):

#         fileName = shutil.make_archive("mushoku", "zip", src)
#         base = os.path.splitext(fileName)[0]

#         target = base + '.epub'
#         os.rename(fileName, target)

#     else: 
#         os.remove("mushoku.epub")

#         fileName = shutil.make_archive("mushoku", 'zip', src)
#         base = os.path.splitext(fileName)[0]

#         target = base + '.epub'

#         os.rename(fileName, target)



# if __name__ ==  "__main__":
#     main()