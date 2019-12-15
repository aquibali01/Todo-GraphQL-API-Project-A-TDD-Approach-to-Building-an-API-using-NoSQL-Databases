from mongoengine import connect

from models import Tasks

connect('graphene-mongo-example', host='mongomock://localhost', alias='default')

def init_db():
    first_task = Tasks(
        # id=1,
        title="medicine Time",
        description="Have to take medicine ",
        done=False
    )
    first_task.save()