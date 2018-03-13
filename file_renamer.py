import os

def rename(dir_, bias=0, top=None, bottom=None):
    file_names = os.listdir(dir_)
    for file_name in file_names:
        root, ext = os.path.splitext(file_name)

        new_name = ""
        if top is not None:
            new_name += top
        new_name += str(file_names.index(file_name)+bias)
        if bottom is not None:
            new_name += bottom
        os.rename(dir_+file_name, dir_+new_name+ext)

        print(file_name + " -> " + new_name+ext)

if __name__ == '__main__':
    print("=====================")
    print("0 : 8888.ext")
    print("1 : foo8888.ext")
    print("2 : 8888bar.ext")
    print("3 : foo8888bar.ext")
    print("=====================")
    print("choose type : ", end='')
    n = int(input())
    print("")

    if n == 0:
        print("dir : ", end='')
        dir_ = input()
        print("bias : ", end='')
        bias = int(input())
        rename(dir_, bias=bias)

    elif n == 1:
        print("dir : ", end='')
        dir_ = input()
        print("bias : ", end='')
        bias = int(input())
        print("top : ", end='')
        top = input()
        rename(dir_, bias=bias, top=top)

    elif n == 2:
        print("dir : ", end='')
        dir_ = input()
        print("bias : ", end='')
        bias = int(input())
        print("bottom : ", end='')
        bottom = input()
        rename(dir_, bias=bias, bottom=bottom)

    elif n == 3:
        print("dir : ", end='')
        dir_ = input()
        print("bias : ", end='')
        bias = int(input())
        print("top : ", end='')
        top = input()
        print("bottom : ", end='')
        bottom = input()
        rename(dir_, bias=bias, top=top, bottom=bottom)
