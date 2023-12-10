#!/usr/bin/env python
""" Define a Review Class Inherite from Base Model"""
from models.base_model import BaseModel


class Review(BaseModel):
    """ Define a Review Class Inherite from Base Model"""
    place_id = ""
    user_id = ""
    text = ""
