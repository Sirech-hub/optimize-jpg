import os

#we smoke a manual - mozilapeg releases v4.0.3


directory = "Ñ:\\images\\"
directory_compressed = "U:\\optimized\\"

with os.scandir(path=directory) as it:
    for entry in it:
        if not entry.is_file():
            print("dir:\t" + entry.name)
        else:
            print("file:\t" + entry.name)
            os.system("cjpeg -quant-table 2 -quality 60 -outfile {} {}".format(directory_compressed+entry.name, directory+entry.name))