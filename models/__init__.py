#!/usr/bin/env python
"""
This package provides utilities for working with airbnb console app
the airbnb clone porject is clone of the original airbnb but right now
it only works in terminal
"""
from .engine import file_storage as fs

storage = fs.FileStorage()
storage.reload()
