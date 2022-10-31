#!/usr/bin/python3
"""Creates an instance of class FileStorage and calls method reload"""


import json
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
