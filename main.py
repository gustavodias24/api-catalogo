from flask import Flask
from blueprints import cat_bp

app = Flask(__name__)

app.register_blueprint(cat_bp)

if __name__ == "__main__":
    app.run()
