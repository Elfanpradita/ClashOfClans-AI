# 🤖 CoC AI Strategy Generator

Sebuah aplikasi web sederhana namun kuat yang memanfaatkan Google Gemini API (Pro Vision) untuk menganalisis dan membuat strategi penyerangan Clash of Clans (CoC). 

Pengguna dapat meng-upload dua gambar—gambar base lawan dan komposisi pasukan mereka—dan AI akan memberikan rekomendasi strategi serangan yang mendetail, langkah demi langkah.

## 💡 Fitur Utama

* **Analisis AI Cerdas:** Menggunakan model `gemini-pro-vision` untuk memahami tata letak base dan komposisi pasukan.
* **Upload Gambar Ganda:** Interface yang mudah untuk meng-upload gambar base lawan dan pasukan.
* **Strategi Mendetail:** Menerima output teks yang jelas berisi (1) Titik Masuk, (2) Funneling, (3) Deployment Pasukan, (4) Penempatan Spell, dan (5) Target Utama.
* **Interface Pengguna Sederhana:** Dibangun dengan Flask dan Bootstrap 5, lengkap dengan tutorial penggunaan dan ikon.
* **Efek Loading:** Tombol submit memiliki *spinner* loading agar pengguna tahu AI sedang memproses.
* **Siap Docker:** Dikemas sepenuhnya dengan `Dockerfile` dan `docker-compose.yml` untuk setup yang mudah.

---

## 🛠️ Teknologi yang Digunakan

* **Backend:** Python 3.10, Flask
* **AI:** Google Generative AI (Gemini API)
* **Frontend:** HTML, Bootstrap 5, JavaScript (sederhana)
* **Deployment:** Docker, Docker Compose

---

## 🚀 Instalasi & Cara Menjalankan

Ikuti langkah-langkah ini untuk menjalankan aplikasi di komputer Anda.

### Prasyarat

* [Docker](https://www.docker.com/get-started) dan [Docker Compose](https://docs.docker.com/compose/install/)
* [API Key Google Gemini](https://aistudio.google.com/app/apikey)

### Langkah-langkah

1.  **Clone Repository Ini**
    (Ganti `nama-repo-anda` dengan nama repo GitHub Bapak)
    ```bash
    git clone [https://github.com/Elfanpradita/nama-repo-anda.git](https://github.com/Elfanpradita/nama-repo-anda.git)
    cd nama-repo-anda
    ```

2.  **Buat File `.env`**
    Buat file baru bernama `.env` di folder utama project. Salin dan tempel konten di bawah ini ke dalamnya, lalu ganti dengan API Key Anda.
    ```plaintext
    GEMINI_API_KEY=YOUR_API_KEY_HERE
    FLASK_APP=app.py
    FLASK_DEBUG=1
    ```

3.  **Siapkan Folder `static`**
    Aplikasi ini menggunakan beberapa gambar untuk tutorial dan favicon.
    * Buat folder baru bernama `static`.
    * Masukkan gambar-gambar berikut ke dalamnya:
        * `IMG_0033.PNG` (Contoh gambar base lawan)
        * `IMG_0034.PNG` (Contoh gambar komposisi pasukan)

4.  **Build dan Jalankan Container**
    Buka terminal di folder utama project dan jalankan:
    ```bash
    docker-compose up --build
    ```
    Docker akan meng-install semua *dependency* (Flask, Pillow, dll.) dan menjalankan server web.

5.  **Buka Aplikasi**
    Buka browser Anda dan akses:
    `http://localhost`

## 👤 Kreator

Dibuat dengan ❤️ oleh **Elfan Pradita**.