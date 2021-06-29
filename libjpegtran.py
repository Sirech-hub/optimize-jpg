from os import listdir
from os.path import isfile
from os.path import join as joinpath
import subprocess

# прописываем имя исходной папки 
mypath = "images"

# Перебираем каждый файл в папке
for i in listdir(mypath):
    # Проверяем не папка ли этот файл
    if isfile(joinpath(mypath,i)):
        print (i)
        # Формируем команду для jpegtran
        cmd = 'jpegtran -progressive -copy none -optimize -outfile optimized/' +i+'  images/'+ i
        PIPE = subprocess.PIPE
        # Выполняем команду 
        p = subprocess.Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=subprocess.STDOUT)

#jpegtran читаем мануал 