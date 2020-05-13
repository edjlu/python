import os
import time
import zipfile

source = r'C:\Users\Edmund\Documents\code'

target_dir = r'C:\Users\Edmund\backup'

target = target_dir + os.sep + time.strftime('%Y-%m-%d_%H_%M_%S') + '.zip'

if not os.path.exists(target_dir):
    os.mkdir(target_dir) #make directory

with zipfile.ZipFile(target, 'w') as zipf:
    for dirpath, dirnames, filenames in os.walk(source):
        arcpath = dirpath[len(source)+1:].replace('\\', '/')
        for filename in filenames:
            arcname = os.path.join(arcpath, filename)
            zipf.write(os.path.join(dirpath, filename), arcname)
