from flask import Flask, request, redirect, url_for, render_template
import psycopg2
import os

app = Flask(__name__)


app.config['DB_HOST'] = os.getenv('DB_HOST', 'localhost')
app.config['DB_NAME'] = os.getenv('DB_NAME', 'postgres')
app.config['DB_USER'] = os.getenv('DB_USER', 'postgres')
app.config['DB_PASS'] = os.getenv('DB_PASS', 'mysecretpassword')
app.config['FLASK_ENV'] = os.getenv('FLASK_ENV', 'development')

def get_db_connection():
    conn = psycopg2.connect(
        host=app.config['DB_HOST'],
        database=app.config['DB_NAME'],
        user=app.config['DB_USER'],
        password=app.config['DB_PASS']
    )
    return conn

@app.route('/', methods=('GET', 'POST'))
def index():
    try:
        conn = get_db_connection()
    except Exception as e:
        return f"<h1>Erro de Conexão com o Banco de Dados!</h1><p>Detalhes: {e}</p>", 500

    cursor = conn.cursor()

    if request.method == 'POST':
        item_text = request.form.get('item_text')
        action = request.form.get('action') 
        item_id = request.form.get('item_id')

        if action == 'add' and item_text:
            cursor.execute('INSERT INTO items (text) VALUES (%s)', (item_text,))
        
        elif action == 'remove' and item_id:
            cursor.execute('DELETE FROM items WHERE id = %s', (item_id,))

        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('index'))

    cursor.execute('SELECT id, text FROM items ORDER BY id DESC')
    items = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return render_template('index.html', items=items, flask_env=app.config['FLASK_ENV'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)