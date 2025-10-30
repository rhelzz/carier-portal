# Admin Panel - CarierPro

Folder `admin/` berisi semua halaman untuk panel administrasi/HR dalam platform CarierPro.

## 📁 Struktur File

```
admin/
├── index.html              # Dashboard utama
├── pelamar.html            # Manajemen data pelamar
├── detail-pelamar.html     # Detail profil pelamar
├── lowongan-admin.html     # Kelola lowongan pekerjaan
├── perusahaan-admin.html   # Kelola data perusahaan
└── README.md              # File dokumentasi ini
```

## 📄 Penjelasan Masing-masing File

### 1. **index.html** - Dashboard Admin/HR
**Fitur:**
- Overview statistik (Total Pelamar, Lamaran Baru, Rekrutmen Aktif, Diterima)
- Visualisasi status lamaran dalam bentuk progress bar
- Daftar posisi paling diminati
- Tabel lamaran terbaru dengan status
- Navigasi sidebar untuk akses ke modul lain

### 2. **pelamar.html** - Manajemen Data Pelamar
**Fitur Sesuai Requirement:**
- ✅ **Filter berdasarkan Posisi** - Dropdown untuk memilih posisi diminati
- ✅ **Filter berdasarkan Status Lamaran** - Pilihan status (Baru, Sedang Diulas, Interview, Diterima, Ditolak)
- ✅ **Search Pelamar** - Pencarian nama atau email
- ✅ **Tampilan Tabel Lengkap** - Nama, Posisi, Email, No. Telepon, Tanggal Melamar, Status
- ✅ **Statistik** - Total pelamar per status
- Pagination untuk navigasi data

### 3. **detail-pelamar.html** - Detail Profil Pelamar
**Fitur:**
- Informasi lengkap pelamar (Nama, Email, No. Telepon, Jenis Kelamin, dll)
- Lihat dan download CV
- Tambah catatan dan penilaian
- Update status lamaran
- Timeline lamaran
- Aksi cepat (Terima, Schedule Interview, Tolak)

### 4. **lowongan-admin.html** - Kelola Lowongan
**Fitur:**
- List semua lowongan yang aktif
- Informasi: Posisi, Perusahaan, Lokasi, Jumlah Pelamar, Status
- Edit lowongan
- Tutup/buka kembali lowongan
- Tambah lowongan baru

### 5. **perusahaan-admin.html** - Data Perusahaan
**Fitur:**
- List perusahaan yang terdaftar
- Informasi: Nama, Website, Lokasi, Jumlah Karyawan, Industri, Lowongan Terbuka
- Status perusahaan (Aktif/Pending)
- Approve/Reject perusahaan baru
- Edit data perusahaan

## 🎨 Design & UI

- **Sidebar Navigation** - Menu utama untuk navigasi antar modul
- **Responsive Design** - Kompatibel dengan desktop dan tablet
- **Color Scheme** - Indigo (#4f46e5) sebagai warna primary
- **Status Badges** - Penggunaan badge untuk status dengan warna berbeda:
  - Biru: Baru
  - Kuning: Sedang Diulas / Pending
  - Oranye: Interview
  - Hijau: Diterima / Aktif
  - Merah: Ditolak
  - Abu-abu: Ditutup

## 🔐 Catatan Keamanan

Panel admin ini memerlukan:
- Sistem autentikasi (login)
- Role-based access control (RBAC)
- Session management
- Data validation

## 📱 Akses Panel Admin

URL: `yoursite.com/admin/`

Halaman utama: `admin/index.html`

## 🚀 Development

Untuk mengembangkan lebih lanjut:
1. Tambahkan backend API untuk fetch data
2. Implementasi authentication
3. Tambahkan form validation
4. Integrasi dengan database
5. Tambahkan export data functionality

---

**Dibuat dengan ❤️ untuk CarierPro**
