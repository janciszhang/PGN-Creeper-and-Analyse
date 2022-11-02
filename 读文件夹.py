# -*- coding: utf-8 -*-


import os

import os
f=open('pgn_file_path.txt','w')
for root, dirs, files in os.walk("G:\pgn", topdown=False):
    for name in files:
        f.write(os.path.join(root, name)+'\n')
    # for name in dirs:
    #     print(os.path.join(root, name))



