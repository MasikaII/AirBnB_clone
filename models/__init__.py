#!/usr/bin/python3
"""
    Updating the __init__ file
"""

from models.engine.filestorage import FileStorage

storage = FileStorage()
storage.reload()
