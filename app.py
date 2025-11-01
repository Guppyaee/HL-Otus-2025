from flask import Flask, request, jsonify
import psycopg2
import bcrypt
import uuid
from datetime import datetime

app = Flask(__name__)

DB_PARAMS = {
    'dbname': 'mydatabase',
    'user': 'myuser',
    'password': 'mysecretpassword',
    'host': 'localhost'
}

def get_db_connection():
    return psycopg2.connect(**DB_PARAMS)

@app.route('/user/register', methods=['POST'])
def register():
    data = request.json
    required = ['firstname', 'secondname', 'birthdate', 'city', 'password']
    if not all(field in data for field in required):
        return jsonify({'error': 'Missing fields'}), 400
        
    hashed = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
    conn = get_db_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO users (id, firstname, secondname, birthdate, biography, city, password_hash) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (str(uuid.uuid4()), data['firstname'], data['secondname'], data['birthdate'], data.get('biography', ''), data['city'], hashed.decode('utf-8'))
        )
        conn.commit()
    except Exception as e:
        conn.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        cur.close()
        conn.close()
    return jsonify({'message': 'User registered'}), 200

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    if 'id' not in data or 'password' not in data:
        return jsonify({'error': 'Missing credentials'}), 400
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT password_hash FROM users WHERE id = %s", (data['id'],))
    row = cur.fetchone()
    cur.close()
    conn.close()
    if row and bcrypt.checkpw(data['password'].encode('utf-8'), row[0].encode('utf-8')):
        # возвращаем простой токен - для примера просто UUID
        token = str(uuid.uuid4())
        return jsonify({'token': token}), 200
    return jsonify({'error': 'Invalid credentials'}), 401

@app.route('/user/get/<user_id>', methods=['GET'])
def get_user(user_id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, firstname, secondname, birthdate, biography, city FROM users WHERE id = %s", (user_id,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    if row:
        user = {
            'id': row[0],
            'firstname': row[1],
            'secondname': row[2],
            'birthdate': row[3].isoformat(),
            'biography': row[4],
            'city': row[5]
        }
        return jsonify(user), 200
    return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
