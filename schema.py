import graphene
from graphene.relay import Node
from graphene_mongo import MongoengineConnectionField, MongoengineObjectType
from models import Tasks as TasksModel
import utils

class Tasks(MongoengineObjectType):

    class Meta:
        model = TasksModel
        interfaces = (Node,)

# class CreateTaskInput(graphene.InputObjectType, Tasks):
#     pass

# class CreateTask(graphene.Mutation):
#     task = graphene.Field(lambda:Tasks, description="Tasks created by this mutation")

#     class Arguments:
#         input = CreateTaskInput(required=True)

#     def mutate(self,info, input):
#         data = utils.input_to_dictionary(input)

#         task = TasksModel(**data)
#         db_session.add(task)
#         db_session.commit()

class Query(graphene.ObjectType):
    node = Node.Field()
    all_tasks = MongoengineConnectionField(Tasks)

schema = graphene.Schema(query=Query)