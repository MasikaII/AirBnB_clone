#!/usr/bin/python3
"""Creates an instance of class FileStorage and calls method reload"""


from models.engine.file_storage import FileStorage
import json


storage = FileStorage()
storage.reload()
