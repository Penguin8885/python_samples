from distutils.core import setup
import py2exe

'''
usage : python setup.py py2exe
'''

option = {
    "compressed" : 1,   # 0=False, 1=True
    "optimize" : 2,     # 0=nothing, 1=normal optimization, 2=strong optimization
    "bundle_files" : 2, # 1=include DLL 2=include DLL and Python, 3=nothing
    "includes" : ["hogehoge", "hugahuga"]
}

setup(
    options = {
        "py2exe" : option
    },
    windows = [     #GUI
        {"script" : "piyopiyo.py"}
    ],
    #console = [    #CUI
    #    {'script': 'piyopiyo.py'}
    #],
    zipfile = None
)