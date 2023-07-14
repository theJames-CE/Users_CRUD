from mysqlconnection import connectToMySQL

db = "users_schema"

# Update the updated_at field when editing the User's information
class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    def full_name(self):
        fullname = f"{self.first_name} {self.last_name}"
        return fullname

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(db).query_db(query)
        users = []
        for user in results:
            users.append(cls(user))
        return users

    @classmethod
    def get_by_id(cls, user_id):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        data = {'id': user_id}
        result = connectToMySQL(db).query_db(query, data)
        if result:
            return cls(result[0])
        return None

    @classmethod
    def save(cls, data):
        query = """
        INSERT INTO users (first_name, last_name, email, created_at, updated_at)
        VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW());
        """
        return connectToMySQL(db).query_db(query, data)

    def update(self):
        query = """
        UPDATE users
        SET first_name = %(first_name)s,
            last_name = %(last_name)s,
            email = %(email)s,
            updated_at = NOW()
        WHERE id = %(id)s;
        """
        data = {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email
        }
        return connectToMySQL(db).query_db(query, data)

    def delete(self):
        query = "DELETE FROM users WHERE id = %(id)s;"
        data = {'id': self.id}
        return connectToMySQL(db).query_db(query, data)
