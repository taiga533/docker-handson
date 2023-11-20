from flask import Flask, jsonify, render_template
from mysql.connector import connect, Error

app = Flask(__name__)

# データベース設定値
db_config = {
  'host': 'db',
  'user': 'test',
  'password': 'test',
  'database': 'test'
}

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route('/users')
def get_users():
    try:
        # データベースに接続
        conn = connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users")
        user_rows = cursor.fetchall()
        return render_template('users.html', users=user_rows)  # user_rowsを渡す
    except Error as e:
        return jsonify({"error": str(e)}), 500
    finally:
        # コネクションを閉じる
        if conn.is_connected():
            cursor.close()
            conn.close()


app.run(debug=True, host='0.0.0.0', port=80)
