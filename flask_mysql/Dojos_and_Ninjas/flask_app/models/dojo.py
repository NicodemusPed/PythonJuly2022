# from flask_app.config.mysqlconnection import connectToMySQL

# class Dojos:
#     def __init__(self, data):
#         self.id = data['id']
#         self.name = data['name']
#         self.created_at = data['created_at']
#         self.updated_at = data['updated_at']

#     @classmethod
#     def get_all(cls):
#         query = "SELECT * FROM dojos;"
#         results = connectToMySQL('dojos_and_ninjas').query_db(query)
#         dojos = [ ]
#         for u in results:
#             dojos.append( cls(u) )
#         return dojos

#     @classmethod
#     def save(cls, data):
#         query = "INSERT INTO dojos ('name') VALUES (%(name)s);"

#         # comes back as the new row id
#         result = connectToMySQL('name').query_db(query,data)
#         return result

#     @classmethod
#     def get_one(cls,data):
#         query  = "SELECT * FROM dojos WHERE id = %(id)s";
#         result = connectToMySQL('name').query_db(query,data)
#         return cls(result[0])

#     @classmethod
#     def update(cls,data):
#         query = "UPDATE dojos SETname=%(name)s,updated_at=NOW() WHERE id = %(id)s;"
#         return connectToMySQL('first_name,last_name,email').query_db(query,data)

#     @classmethod
#     def destroy(cls,data):
#         query  = "DELETE FROM dojos WHERE id = %(id)s;"
#         return connectToMySQL('users_schema').query_db(query,data)