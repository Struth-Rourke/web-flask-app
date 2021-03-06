# web_app/models.py

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Instantiating the DataBase from the SQLAlchemy Class
db = SQLAlchemy()

# Instantiating Migrate
migrate = Migrate()

# Defining new class "Book":
class Book(db.Model):
    ###__table_name__ = "books" #> configuing table name
    # Configuring the DataBase columns: id, title and author_id
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128))
    author_id = db.Column(db.String(128))

# Defining the parse_records function
def parse_records(database_records):
    """
    A helper method for converting a list of database record objects into a list 
    of dictionaries, so they can be returned as JSON.

    Param: database_records (a list of db.Model instances)

    Example: parse_records(User.query.all())

    Returns: a list of dictionaries, each corresponding to a record, like...
        [
            {"id": 1, "title": "Book 1"},
            {"id": 2, "title": "Book 2"},
            {"id": 3, "title": "Book 3"},
        ]
    """
    parsed_records = []
    for record in database_records:
        print(record)
        parsed_record = record.__dict__
        del parsed_record["_sa_instance_state"]
        parsed_records.append(parsed_record)
    return parsed_records