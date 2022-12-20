from flask import Flask, render_template
from src.sql_requests import database


def create_app():
    app = Flask(__name__,   instance_relative_config=True)
    app.register_blueprint(database)

    @app.route('/')
    def main_page():
        return render_template("main_page.html")

    @app.route('/view_db')
    def all_db():
        return render_template("view_db.html")


    return app


if __name__ == "__main__":
    create_app().run(port=4000)