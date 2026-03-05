from flask import Flask
from config import Config
from flask import jsonify
from extensions import db
from routes import bp

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

app.register_blueprint(bp)

@app.route('/')
def hello_world():
  return jsonify({'message': 'Hello World!'})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)