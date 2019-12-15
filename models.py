from mongoengine import Document
from mongoengine.fields import (
    StringField, BooleanField, IntField)

class Tasks(Document):

    meta = {'collection': 'tasks'}
    # id = IntField()
    title = StringField()
    description = StringField()
    done = BooleanField()

