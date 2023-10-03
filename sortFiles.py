import os

def sortFiles(directoryPath, pathToSaveFiles):
    if os.path.exists(directoryPath) and os.path.exists(pathToSaveFiles):
        files = os.listdir(directoryPath)
        if files:
            os.chdir(pathToSaveFiles)
            saveDirectory = "Files"
            if not os.path.exists(saveDirectory):
                os.mkdir(saveDirectory)
            os.chdir(os.path.join(pathToSaveFiles, saveDirectory))
            subdirectories = ['Images', 'Videos', 'Documents', 'Other']
            for item in subdirectories:
                if not os.path.exists(item):
                    os.mkdir(item)

            PICTURE_EXTENSIONS = ["jpg", "jpeg", "png", "gif", "bmp", "tiff", "webp"]
            VIDEO_EXTENSIONS = ["mp4", "avi", "mkv", "mov", "wmv", "flv", "webm"]
            DOCUMENT_EXTENSIONS = ["doc", "docx", "pdf", "txt", "rtf", "odt"]
            for item in files:
                fileExtension = item.split('.')[-1]
                if fileExtension in PICTURE_EXTENSIONS:
                    fileType = "Pictures"
                elif fileExtension in VIDEO_EXTENSIONS:
                    fileType = "Videos"
                elif fileExtension in DOCUMENT_EXTENSIONS:
                    fileType = "Documents"
                else:
                    fileType = "Other"
                os.chdir(os.path.join(pathToSaveFiles, saveDirectory, fileType))

                try:
                    filePath = os.path.join(directoryPath, item)
                    with open(filePath, 'rb') as file:
                        data = file.read()
                        with open(filePath, 'wb') as newFile:
                            newFile.write(data)
                except:
                    print(f"Ошибка при чтении/записи файла '{item}'!")
            print("Сортировка файлов успешно выполнена!")
        else:
            print(f"Папка '{directoryPath}' - пустая!")
    else:
        print("Передан некоректный путь!")