#!/usr/bin/env python

from models.base_model import BaseModel

""" Define a Review Class Inherite from Base Model"""


class Review(BaseModel):
    place_id = ""
    user_id = ""
    text = ""
