import os
from platform import freedesktop_os_release

def createIfNotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def move(folderName, files):
    for file in files:
        os.replace(file, f"{folderName}/{file}") 

if __name__ == "__main__":
        
    files = os.listdir()
    files.remove("main.py")

    createIfNotExist('Images')      # This is the code, Now I will run it
    createIfNotExist('Docs')
    createIfNotExist('Media')
    createIfNotExist('Others')

    imgExts = [".png", ".jpg", ".jpeg"]
    images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts ]

    docExts = [".txt", ".docx", "doc", ".pdf"]
    docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]


    mediaExts = [".mp4", ".mp3", ".flv"]
    medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaExts]

    others = []
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if (ext not in mediaExts) and (ext not in docExts) and (ext not in imgExts) and os.path.isfile(file):
            others.append(file)

    move("Images", images)
    move("Docs", docs)
    move("Media", medias)
    move("Others", others)



        # # So personally I don't like clutter of anything at all,
        # And when it comes to my pc, so as an engineering student , programmer 
        # and a developer I have to deal with a lot of files and data which makes my pc directories look messy and horrible,

        # So to manage it I made a python program to make my pc clutter free and also to enhance my productivity
        # as a clutter free pc help me to fetch my desired file in less time 

        # SO we seen that after running my program all the files get catogarized as docs, images, media and others 
        

        # THANK YOU!!🤩🙂
