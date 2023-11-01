import graphene
from graphene import Field, String, List
from mutation import CreateUser, UpdateUser, DeleteUser
from query import Query
from type import User


class MyMutations(graphene.ObjectType):
    create_user = CreateUser.Field()
    update_user = UpdateUser.Field()
    delete_user = DeleteUser.Field()


class MyQuery(Query):
    user = Field(User)
    get_user = Field(User, id=String())
    get_users = List(User)


schema = graphene.Schema(query=MyQuery, mutation=MyMutations)

# result = schema.execute(
#     """
#     mutation {
#         createUser(id: "1", name:"John Doe", email:"benzps01@gmail.com", password:"123456"){
#             user{
#                 id
#                 name
#                 email
#                 password
#             }
#         }
#     }
#     """
# )
# print(result.data)

result = schema.execute(
    """
    mutation {
        updateUser(id: "1", name:"John Doe", email:"JohnDoe@gmail.com", password:"4141341"){
            user{
                id
                name
                email
                password
            }
        }
    }
    """
)
print(result.data)


result = schema.execute(
    """
    query {
        getUser(id: "1") {
                id
                name
                email
                password
        }
    }
    """
)

print(result.data)

result = schema.execute(
    """
    query {
        getUsers {
                id
                name
                email
                password
        }
    }
    """
)

print(result.data)

result = schema.execute(
    """
    mutation {
        deleteUser(id: "1") {
            user {
                id
                name
                email
                password
            }
        }
    }
    """
)

print(result.data)

result = schema.execute(
    """
    query {
        getUsers {
                id
                name
                email
                password
        }
    }
    """
)

print(result.data)
