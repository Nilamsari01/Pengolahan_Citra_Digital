# Mini Project PCD – Deteksi Keberadaan Tanda Tangan Kepala Sekolah

**Nama:** Nilam Sari | **NIM:** F1G124046 | **Prodi:** Ilmu Komputer

Program mendeteksi apakah area tanda tangan kepala sekolah pada citra ijazah terisi tanda tangan
(`SIGNATURE PRESENT`) atau kosong (`SIGNATURE ABSENT`) memakai OpenCV.

## Pipeline
1. **Crop** area tanda tangan (koordinat relatif 0–1, default `0.50 0.72 0.83 0.80`)
2. **Grayscale**
3. **Thresholding**: Global (127), Otsu, Adaptive Gaussian – dibandingkan
4. **Morphology**: opening → closing (kernel 3×3)
5. **Karakteristik area**: jumlah piksel foreground, persentase, kontras tinta
6. **Aturan keputusan**: `PRESENT` jika foreground ≥ 2% **dan** kontras (median − persentil 2) ≥ 40

## Struktur Repository
```
├── Tugas6_PCD_NILAM_SARI.ipynb   # versi Google Colab (laporan + analisis)
├── signature_detection.py        # versi script lokal
├── requirements.txt
├── images/                       # citra uji: present_*.jpg / absent_*.jpg
└── output/                       # dibuat otomatis (CSV + gambar pipeline)
```

## How to Run

### Opsi A – Google Colab
1. Klik badge *Open in Colab* di bagian atas notebook.
2. `Runtime → Run all`, upload citra saat diminta.
3. Beri nama file `present_...` / `absent_...` bila ingin akurasi dihitung.

### Opsi B – Lokal
```bash
git clone https://github.com/Nilamsari01/Pengolahan_Citra_Digital.git
cd Pengolahan_Citra_Digital

python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt

python signature_detection.py
```

Opsi tambahan:
```bash
python signature_detection.py --input images --output output \
    --roi 0.50 0.72 0.83 0.80 --min-ratio 0.02 --min-contrast 40
```

**Penting:** label aktual diambil dari awalan nama file (`present_` / `absent_`).
ROI harus disesuaikan dengan tata letak ijazah masing-masing.

### Output
- `output/hasil_deteksi.csv` – prediksi, foreground, akurasi per citra
- `output/perbandingan_thresholding.csv` – perbandingan Global/Otsu/Adaptive
- `output/<nama>_pipeline.png` – visualisasi tiap tahap

## Hasil Uji (contoh)
| Citra | Otsu | Foreground | Kontras | Prediksi | Aktual |
|---|---|---|---|---|---|
| absent_ijazah3 | 0 | 0.00% | 0.0 | ABSENT | ABSENT |
| present_ijazah2 | 217 | 30.44% | 135 | PRESENT | PRESENT |

Foreground per metode (setelah morphology) pada `present_ijazah2`: Global 0%, Adaptive 20.24%, Otsu 30.44%.
Global threshold 127 gagal karena tinta/stempel pada citra ini lebih terang dari 127; Otsu menyesuaikan diri otomatis.

## Analisis
**Mengapa thresholding diperlukan?** Grayscale masih 256 tingkat intensitas, sehingga "ada tinta atau tidak"
belum bisa dihitung. Thresholding mengubahnya menjadi biner (foreground = tinta, background = kertas), lalu
piksel foreground bisa dihitung dan dipakai sebagai dasar aturan keputusan.

**Threshold terlalu tinggi:** terlalu banyak piksel dianggap foreground — kertas, noise, tekstur, dan
watermark ikut terdeteksi, sehingga area kosong bisa salah menjadi PRESENT (false positive).
**Threshold terlalu rendah:** hanya piksel sangat gelap yang lolos; goresan tipis atau tinta terang
hilang/terputus, sehingga tanda tangan asli bisa salah menjadi ABSENT (false negative).
*(Catatan: arah ini berlaku untuk `THRESH_BINARY_INV`, yaitu piksel ≤ threshold menjadi foreground. Pada kode ini global threshold 127 yang "terlalu rendah" terbukti memberi 0% pada tanda tangan terang.)*

