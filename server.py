from flask import Flask, request, render_template, send_file
from sqlalchemy import create_engine
from sqlalchemy.sql import text

app = Flask(__name__)

FILE_PATH = r".\sample.accdb"

@app.route('/xml')
def response_xml():
    return send_file("sample.xml")
    

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        item_name = request.form["item_name"]
        info = get_from_db(item_name)
        return render_template("index.html", **info)
        
    else:
        return render_template("index.html", message=None)


def get_from_db(item_name):
    url = "access+pyodbc:///?Driver={{Microsoft Access Driver (*.mdb, *.accdb)}};Dbq={0};".format(FILE_PATH)
    engine = create_engine(url)
    connection = engine.connect()
    
    sql = r"SELECT * FROM Item WHERE item_name = :name"
    db = connection.execute(text(sql), name = item_name)

    result = { "message": None }
    for row in db:
        # 最初に見つかった1件のみ表示
        result = {
            "message": "Result: {0}".format(row['item_name']),
            "item_id": row['ID'],
            "item_name":  row["item_name"],
        }
        
    # http://stackoverflow.com/questions/21738944/how-to-close-a-sqlalchemy-session
    # engine.dispose()しないと、`sample.laccdb`が残る
    connection.close()
    engine.dispose()

    return result
    
    
if __name__ == '__main__':
    app.run(debug=True)