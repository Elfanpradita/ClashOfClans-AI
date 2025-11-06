import os
import google.generativeai as genai
from flask import Flask, render_template, request, redirect, url_for, flash
from PIL import Image
from dotenv import load_dotenv

# Muat variabel lingkungan dari .env
load_dotenv()

app = Flask(__name__)
app.secret_key = 'supersecretkey' # Digunakan untuk flash messages

# Konfigurasi Gemini API
try:
    genai.configure(api_key=os.environ["GEMINI_API_KEY"])
    model = genai.GenerativeModel('models/gemini-2.5-pro') # Gunakan model yang support vision
except Exception as e:
    print(f"Error configuring Gemini: {e}")
    model = None

@app.route('/')
def index():
    """Menampilkan halaman utama (upload form)."""
    return render_template('index.html', strategy=None)

@app.route('/upload', methods=['POST'])
def upload_files():
    """Menangani upload gambar dan memanggil Gemini."""
    if model is None:
        flash('Error: Gemini API tidak terkonfigurasi. Periksa API Key Anda di .env', 'danger')
        return redirect(url_for('index'))

    if 'base_image' not in request.files or 'army_image' not in request.files:
        flash('Error: Kedua gambar (base dan pasukan) harus di-upload.', 'warning')
        return redirect(url_for('index'))

    base_image_file = request.files['base_image']
    army_image_file = request.files['army_image']

    if base_image_file.filename == '' or army_image_file.filename == '':
        flash('Error: Kedua gambar (base dan pasukan) harus di-upload.', 'warning')
        return redirect(url_for('index'))

    try:
        # Buka gambar menggunakan Pillow
        base_img = Image.open(base_image_file.stream)
        army_img = Image.open(army_image_file.stream)

        # Prompt untuk Gemini
        prompt_text = """
        Anda adalah seorang ahli strategi Clash of Clans (CoC) kelas dunia.
        Tugas Anda adalah menganalisis dua gambar yang diberikan:
        1.  Gambar pertama adalah base lawan yang akan diserang.
        2.  Gambar kedua adalah komposisi pasukan yang saya miliki.

        Tolong berikan strategi penyerangan yang mendetail, langkah demi langkah. 
        Jelaskan:
        1.  **Titik Masuk:** Dari arah mana (jam berapa) serangan harus dimulai dan mengapa.
        2.  **Funneling:** Bagaimana cara membuat jalur (funnel) agar pasukan utama masuk ke tengah.
        3.  **Deployment Pasukan:** Urutan penempatan setiap unit (misal: Golem dulu, lalu Wizard, lalu Hero).
        4.  **Penempatan Spell:** Kapan dan di mana harus menggunakan Spell (Heal, Rage, Jump, Freeze).
        5.  **Target Utama:** Apa yang harus dihancurkan terlebih dahulu (misal: Clan Castle, Eagle Artillery, Town Hall).
        6.  **Kelemahan Base:** Sebutkan kelemahan utama dari base lawan ini.

        Buatlah penjelasan Anda sejelas dan sedetail mungkin agar mudah diikuti.
        """

        # Kirim prompt multimodal (teks + gambar) ke Gemini
        response = model.generate_content([
            prompt_text,
            "Gambar 1: Base Lawan",
            base_img,
            "Gambar 2: Komposisi Pasukan Saya",
            army_img
        ])

        # Render ulang halaman index dengan hasil strategi
        # Gunakan markdown=True (jika Anda menambahkan library markdown) atau proses di template
        return render_template('index.html', strategy=response.text)

    except Exception as e:
        flash(f'Error saat memproses gambar atau memanggil API: {e}', 'danger')
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)