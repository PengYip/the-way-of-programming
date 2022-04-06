import os

#判断指定目录下包含的是文件还是目录
dir = r"C:\Users\whapp\PycharmProjects\pythonProject1"
files = os.listdir(dir)
i = 0
while i < files.__len__():
    fullpath = os.path.join(dir, files[i])
    if os.path.isfile(fullpath):
        print("我是一个文件")
    elif os.path.isdir(fullpath):
        print("我是一个目录")
    i += 1

#打印指定目录中包含main的文件
sub_str = "main"
cur_dir = os.getcwd()
files_2 = os.listdir(cur_dir)
for item in files_2:
    if os.path.isfile(os.path.join(cur_dir,item)):
        if item.find(sub_str) != -1:
            print(os.path.join(cur_dir,item))

#读取指定文件夹里面的目录，然后把目录的列表送入excle

