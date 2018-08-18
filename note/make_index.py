import os


# 若html文件存在是否重复生成
generate_exist = False



for root, dirs, files in os.walk("./source", topdown=False):
    for name in files:
        print(os.path.join(root, name))
    print('DIRS:\n'+'*'*16+'\n')
    for name in dirs:
        print(os.path.join(root, name))

if generate_exist == True:
    pass
else:
    pass




