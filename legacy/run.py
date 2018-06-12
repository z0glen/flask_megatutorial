#!flask/bin/python
from app import app
app.run()

"""
TODO list:
- add blocking users
- add filter posts displayed by custom groups
- better full text search engine? (e.g. haystack for django)
- full text doesn't work in python 3
- cosmetic changes (bootstrap)
- translations (?)
"""
