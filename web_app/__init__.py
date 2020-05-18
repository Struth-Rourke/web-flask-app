# web_app/__init__.py

from flask import Flask

from web_app.models import db, migrate
from web_app.routes.home_routes import home_routes
from web_app.routes.book_routes import book_routes

# DataBase File Path
DATABASE_URI = "sqlite:///web_app_99.db" # using relative filepath
#DATABASE_URI = "sqlite://///Users/rourkestruthers/Desktop/ComputerScience/LambdaSchool/Unit3-DataEngineering/Sprint3-Productization_Cloud/DS-Unit-3-Sprint-3-Productization-and-Cloud/twitter-flask-app/twitter-flask-app-db.db" # using absolute filepath on Mac (recommended)


# Instiailizing the app inside of a function
def create_app():
    app = Flask(__name__)

    # Configures the DataBase
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
    # Initializes the DataBase
    db.init_app(app)
    # Migrates the app and DataBase
    migrate.init_app(app, db)

    # Registering the blueprints for the different app routes
    app.register_blueprint(home_routes)
    app.register_blueprint(book_routes)
    
    return app





# Factory pattern; Flask best practice
if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)