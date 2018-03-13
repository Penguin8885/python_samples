import sys

def parse(args, default):
    values = default.copy()
    args = args[1:] #delete file_name
    for argv in args:
        index = argv.find('=')
        key = argv[:index]
        value = float(argv[index+1:])
        if key in default:
            values[key] = value
    return values

if __name__ == '__main__':
    default = {'a':1, 'b':2, 'c':5}
    vals = parse(sys.argv, default)
    print(default)
    print(vals)
