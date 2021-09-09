from os import listdir
from os.path import isfile
from os.path import join as joinpath
import subprocess


mypath = "images"

for i in listdir(mypath):
   
    if isfile(joinpath(mypath,i)):
        print (i)
     
        cmd = 'jpegtran -progressive -copy none -optimize -outfile optimized/' +i+'  images/'+ i
        PIPE = subprocess.PIPE
       
        p = subprocess.Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=subprocess.STDOUT)

