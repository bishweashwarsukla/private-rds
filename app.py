import os

import mysql.connector
from flask import Flask, render_template

app = Flask(__name__)


def fetchData():
    ENDPOINT = "bishweashwardb.cldb1lgd5bay.us-east-1.rds.amazonaws.com"
    PORT = "3306"
    USER = "admin"
    DBNAME = "assignmentDB"
    password = "sonu0503"
    os.environ["LIBMYSQL_ENABLE_CLEARTEXT_PLUGIN"] = "1"
    conn = mysql.connector.connect(
        host=ENDPOINT, user=USER, passwd=password, port=PORT, database=DBNAME
    )
    print('******Coonected to RDS Successfully*****')
    cur = conn.cursor()
    cur.execute("""INSERT INTO log(entry) VALUES (CURRENT_TIMESTAMP);""")
    conn.commit()
    cur.execute("""SELECT * FROM log""")
    results = cur.fetchall()
    data = []
    for result in results:
        data.append(result[0])
    conn.close()
    return data


@app.route("/")
@app.route("/home")
def home():
    try:
        posts = fetchData()
        return render_template("index.html", posts=posts)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
