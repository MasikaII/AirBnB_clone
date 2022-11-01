#!/usr/bin/python3
"""Contains a derived class that inherits from BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """Inherits from BaseClass"""

    state_id = ""
    name = ""
