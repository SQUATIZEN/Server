from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

# Konfigurasi database
db = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'root',
    'port': '3306',
    'database': 'ngukurban'
}

# Membuat koneksi ke database
def create_db_connection():
    connection = mysql.connector.connect(**db)
    return connection

# Endpoint untuk mendapatkan semua data
@app.route('/data', methods=['GET'])
def get_all_data():
    # Membuat koneksi ke database
    connection = create_db_connection()

    # Membuat kursor untuk menjalankan query
    cursor = connection.cursor()

    # Menjalankan query SELECT untuk mengambil semua data dari tabel
    query = "SELECT * FROM ban"
    cursor.execute(query)

    # Mengambil hasil query
    result = cursor.fetchall()

    # Menutup koneksi ke database
    cursor.close()
    connection.close()

    # Mengembalikan respons JSON dengan data yang diperoleh
    return jsonify(result)

# Endpoint untuk menambahkan data baru
@app.route('/data', methods=['POST'])
def add_data():
    # Mengambil data dari permintaan POST
    data = request.json

    # Membuat koneksi ke database
    connection = create_db_connection()

    # Membuat kursor untuk menjalankan query
    cursor = connection.cursor()

    # Menjalankan query INSERT untuk menyimpan data baru ke dalam tabel
    query = "INSERT INTO ban (id_ban, id_user, foto_ban) VALUES (%s, %s, %s)"
    values = (data['id_ban'], data['id_user'], data['foto_ban'])
    cursor.execute(query, values)
    connection.commit()

    # Menutup koneksi ke database
    cursor.close()
    connection.close()

    # Mengembalikan respons JSON dengan pesan sukses
    return jsonify({'message': 'Data added successfully'})

@app.route('/', methods=['GET'])
def hello():
    return jsonify(status="running")

@app.route('/about')
def about():
    return 'This is the about page of the application.'

if __name__ == '__main__':
    app.run(debug=True, port=3307)