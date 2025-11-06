# Gunakan base image Python 3.10
FROM python:3.10-slim

# Set direktori kerja di dalam container
WORKDIR /app

# Salin file requirements
COPY requirements.txt requirements.txt

# Install semua library yang dibutuhkan
RUN pip install -r requirements.txt

# Salin sisa kode aplikasi
COPY . .

# Perintah untuk menjalankan aplikasi saat container dimulai
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]