#!/usr/bin/python
'''

A simple tool to bundle package into a python script. The python script
execute command as specified in the manifest file

Permission is granted to use, modify and redistribute this software. 
No warranty is provided.

Ang Way Chuang <wcang@sfc.wide.ad.jp>
'''
import tarfile
import json
import os
import shutil
import base64

manifest = json.load(open("manifest.json", "r"))

if not os.path.isdir(manifest['directory']):
    sys.stderr.write("manifest.json directory entry %s is not directory\n" %
            manifest['directory'])
    sys.exit(1)

with tarfile.open("bundle.tar.bz2", "w:bz2") as tar:
    tar.add('manifest.json')
    for root, dirs, names in os.walk(manifest['directory']):
        for name in names:
            tar.add(os.path.join(root, name))

tar_data = base64.b64encode(open("bundle.tar.bz2", "r").read())

extract_py = '''#!/usr/bin/python
import tarfile
import os
import base64
import json
import sys

tar_data = "%s"

tar = open("bundle.tar.bz2", "w")
tar.write(base64.b64decode(tar_data))
tar.close()

with tarfile.open("bundle.tar.bz2", "r:bz2") as tar:
    tar.extractall()

os.unlink("bundle.tar.bz2")
manifest = json.load(open("manifest.json", "r"))
sys.exit(os.system(manifest['execute']))

#os.unlink("bundle.tar.bz2")
''' % tar_data

with open("extract.py", "wt") as out:
    out.write(extract_py)

os.unlink("bundle.tar.bz2")
