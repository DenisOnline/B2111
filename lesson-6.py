# import os
#
# dir_1 = "Windows"
# dir_2 = "Web"
# path = os.path.join(dir_1, dir_2)
# print(path)
# for path, dirnames, filenames in os.walk(f"C:/{path}"):
#     print(f"path = {path}")
#     print(f"dirnames = {dirnames}")
#     print(f"filenames = {filenames}")
#
# print(os.path.isabs(f"C:/{path}"))
# print(os.path.isfile(f"C:/{path}"))
# print(os.path.isdir(f"C:/{path}"))
# print(os.path.islink(f"C:/{path}"))
#
# new_path = os.path.normpath("new_dir")
# os.mkdir(new_path)
# os.rmdir(new_path)
#
#
# file = open("file.txt", "w")
# file.write("Hello world!")
# file.close()
# file = open("file.txt", "a")
# file.write("\nHi!")
# file.close()
# file = open("file.txt", "r")
# print(file.read())
# file.close()
#
# with open("file.txt", "w") as file:
#     file.write("Hello world!")
# with open("file.txt", "a") as file:
#     file.write("Hello world!")
# with open("file.txt", "r") as file:
#     print(file.read())

import os


def file_collector(path):
    path = os.path.normpath(path)
    result = {"dirs": [], "files": []}
    for path, dirnames, filenames in os.walk(path):
        for dir in dirnames:
            result["dirs"].append(dir)
        for file in filenames:
            result["files"].append(file)
    with open("skiper.txt", "w") as file:
        file.write("\n{:-<50}\n".format("Directories"))
        for dir in result["dirs"]:
            file.write(f"\t{dir}\n")
            file.write("\n{:-<50}".format("Files"))
        for files in result["files"]:
            file.write(f"\t{files}\n")


path = "C:\\Windows\\Web"
file_collector(path)