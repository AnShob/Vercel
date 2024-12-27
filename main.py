from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        # Ambil data dari form
        tahun_lahir = int(request.form['tahun_lahir'])
        tahun_sekarang = datetime.now().year
        usia = tahun_sekarang - tahun_lahir
        return render_template('cek_usia.html', Sinopsis=sinopsis, Genre=genre_prediksi)
    return render_template('cek_usia.html', Sinopsis= None, Genre=None, Foto=None)
    
if __name__ == "__main__":
    app.run(host='0.0.0.0')
