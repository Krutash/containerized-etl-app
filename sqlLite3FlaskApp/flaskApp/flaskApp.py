from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

DB_PATH = '../chinook_test.db'

def query_db(query):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(query)

    rows = cursor.fetchall()
    columns = [description[0] for description in cursor.description]
    conn.close()
    return [dict(zip(columns, row)) for row in rows ]

@app.route('/usersArchive', methods=['GET'])
def get_users():
    where_clause = request.args.get('where')

    base_query = "select * FROM users"
    if where_clause:
        try:
            query = f"{base_query} WHERE {where_clause}"
            results = query_db(query)
        except Exception as e:
            return jsonify({'error': str(e)}), 400

    else:
        results = query_db(base_query)

    return jsonify(results)

@app.route('/humanresourceArchive', methods=['GET'])
def get_humanresourceArchive():
    where_clause = request.args.get('where')

    base_query = "select * FROM humanresource"
    if where_clause:
        try:
            query = f"{base_query} WHERE {where_clause}"
            results = query_db(query)
        except Exception as e:
            return jsonify({'error': str(e)}), 400

    else:
        results = query_db(base_query)

    return jsonify(results)

@app.route('/textContent', methods=['GET'])
def get_text_context():
    where_clause = request.args.get('where')

    base_query = "select * FROM text_document"
    if where_clause:
        try:
            query = f"{base_query} WHERE {where_clause}"
            results = query_db(query)
        except Exception as e:
            return jsonify({'error': str(e)}), 400

    else:
        results = query_db(base_query)

    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
