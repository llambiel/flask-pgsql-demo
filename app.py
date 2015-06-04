from flask import Flask
from flask import jsonify
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)

@app.route("/")
def home():
    result = db.engine.execute("select * from pg_stat_replication ;")
    names = []
    for row in result:
        names.append(row)
    return str(names)


app.run(host='0.0.0.0', port=8080, debug=True)
