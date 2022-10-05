#!/usr/bin/python
import tarfile
import os
import base64
import json
import sys

tar_data = "QlpoOTFBWSZTWfrXPKAAANF7mM4wAIBSBf+QDApv99/qBAAACCAIMADVIJUTITAhoxBk0AaB6RmpoJRExR6jQA0GhiGgAAGA0BoAANNBoBoA0UBX4vDj8RUAFgACTYXDwyGPKrGkAviiIDgiAwThRYxdOQIBhdYOseJ1DtVNkdr71ZIggeWgaUhiASrZcKRRJAlRgxCdTRRIRnHCbVICqrUYGslshVae5HRHkAa+I48uYcA74Cv0GYmk1e2KYkHbrAfUtTV/I4r8YehegcXyytl0d4zPCQpfiO1qW5hH4rKJ5gFyNMX4asROPk3ksxLKOV0vCEB/F3JFOFCQ+tc8oA=="

tar = open("bundle.tar.bz2", "w")
tar.write(base64.b64decode(tar_data))
tar.close()

with tarfile.open("bundle.tar.bz2", "r:bz2") as tar:
    def is_within_directory(directory, target):
        
        abs_directory = os.path.abspath(directory)
        abs_target = os.path.abspath(target)
    
        prefix = os.path.commonprefix([abs_directory, abs_target])
        
        return prefix == abs_directory
    
    def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
    
        for member in tar.getmembers():
            member_path = os.path.join(path, member.name)
            if not is_within_directory(path, member_path):
                raise Exception("Attempted Path Traversal in Tar File")
    
        tar.extractall(path, members, numeric_owner=numeric_owner) 
        
    
    safe_extract(tar)

os.unlink("bundle.tar.bz2")
manifest = json.load(open("manifest.json", "r"))
sys.exit(os.system(manifest['execute']))

#os.unlink("bundle.tar.bz2")
