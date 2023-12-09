#!/usr/bin/env python
"""User Class"""
from .base_model import BaseModel


class User(BaseModel):
    """User Class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
