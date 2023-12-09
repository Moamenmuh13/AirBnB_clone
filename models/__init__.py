#!/usr/bin/env python
"""
This package provides utilities for working with airbnb console app
"""
from .engine import file_storage as fs

storage = fs.FileStorage()
storage.reload()
