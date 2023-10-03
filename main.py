from sortFiles import *

if __name__ == "__main__":
    directoryPath = input("Введите путь директори с которой нужно отсортировать файлы: ")
    pathToSaveFiles = input("Введите путь где нужно сохранить отсортированые файлы: ")
    sortFiles(directoryPath, pathToSaveFiles)