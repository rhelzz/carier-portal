# CarierPro - Platform Portal Karir

Selamat datang di **CarierPro**, portal karir terpadu yang menghubungkan pencari kerja dengan perusahaan-perusahaan terkemuka di Indonesia.

## 🆕 NEW: Microsoft 365 Integration Ready!

CarierPro sekarang dilengkapi dengan **Login & Register Flow Microsoft 365** yang siap di-slice ke **SharePoint** dan **Power Platform**!

### ✨ Fitur Terbaru
- 🔐 **Microsoft 365 Single Sign-On (SSO)** - Flow simulasi login dengan akun Microsoft
- � **SharePoint-Compatible UI** - Menggunakan Segoe UI dan Microsoft Design Language
- 🎨 **Power Platform Ready** - Komponen siap diconvert ke Power Apps
- 🔄 **Multi-Step Registration** - Wizard 3 langkah dengan progress indicator
- 🔒 **Password Strength Checker** - Real-time validation
- ✅ **Form Validation** - Client-side validation yang robust

### 📦 File Baru
- `login.html` - Halaman login dengan Microsoft 365 SSO
- `register.html` - Halaman registrasi multi-step
- `SHAREPOINT-GUIDE.md` - Panduan lengkap slicing ke SharePoint
- `MS365-COMPONENTS.md` - Komponen reusable untuk Power Platform

---

## �📋 Daftar Halaman

Website ini terdiri dari **9 halaman utama** dengan design responsive dan corporate style:

### 1. **Beranda (index.html)**
- Hero section dengan call-to-action
- Statistik penempatan dan fitur unggulan
- Lowongan kerja terbaru
- Section call-to-action untuk pendaftaran
- Footer dengan link navigasi

### 2. **Lowongan Kerja (lowongan.html)**
- Sidebar filter pencarian (lokasi, jenis kerja, gaji, kategori)
- Daftar lowongan dengan status aktif/segera ditutup
- Search bar untuk pencarian
- Kartu lowongan dengan detail singkat
- Pagination untuk navigasi

### 3. **Daftar Perusahaan (perusahaan.html)**
- Grid tampilan perusahaan partner
- Informasi singkat setiap perusahaan
- Jumlah lowongan terbuka per perusahaan
- CTA untuk pendaftaran sebagai perusahaan
- Search perusahaan

### 4. **Daftar Pelamar (daftar.html)**
- Form pendaftaran pencari kerja lengkap
- Input untuk data pribadi, posisi, pengalaman
- Upload CV/lamaran (drag & drop)
- Pilihan lokasi preferensi
- Checkbox kesepakatan T&K
- Section benefits dengan 3 kolom

### 5. **FAQ & Panduan (faq.html)**
- 7 kategori FAQ dengan accordion details
- Pertanyaan & jawaban komprehensif sesuai instruksi
- Search FAQ functionality
- CTA untuk hubungi support
- Topik mencakup: Portal Karir, Lowongan, Upload CV, Notifikasi, Dashboard HR, Statistik, Keamanan

### 6. **Masuk (login.html)** ⭐ NEW
- **Microsoft 365 SSO Flow** dengan modal interaktif
- Traditional email/password login
- Password visibility toggle
- SharePoint-compatible styling
- Mobile responsive
- Loading states & animations
- Link ke halaman register

### 7. **Daftar Akun (register.html)** ⭐ NEW
- **Multi-step registration** (3 steps dengan progress indicator)
- Microsoft 365 quick sign-up option
- Password strength indicator
- Form validation real-time
- Review data sebelum submit
- Success modal dengan next steps
- Terms & conditions checkbox

### 8. **Detail Lowongan (detail-lowongan.html)**
- Header dengan informasi lowongan dan status
- Deskripsi lengkap pekerjaan
- Kualifikasi wajib dan yang diharapkan
- Benefit & fasilitas
- Skill tags yang dibutuhkan
- Sidebar dengan profile perusahaan
- Tombol lamar & simpan
- Share lowongan ke social media
- Related jobs suggestions

---

## 🚀 Microsoft 365 & SharePoint Integration

### Cara Menggunakan di SharePoint

#### Opsi 1: Embed Langsung (Quick & Simple)
```html
1. Upload login.html & register.html ke SharePoint Document Library
2. Tambahkan Script Editor Web Part ke page
3. Link ke file HTML Anda
4. Done! 🎉
```

#### Opsi 2: Power Apps Integration
```
1. Buka Power Apps Studio
2. Recreate UI menggunakan komponen dari MS365-COMPONENTS.md
3. Connect ke Office365Users connector untuk SSO
4. Deploy ke SharePoint sebagai app
```

#### Opsi 3: SharePoint Framework (SPFx)
```bash
1. Extract komponen dari login.html
2. Convert ke React components
3. Build SPFx solution
4. Deploy ke App Catalog
```

### 📚 Dokumentasi Lengkap
Lihat file berikut untuk panduan detail:
- **SHAREPOINT-GUIDE.md** - Tutorial lengkap slicing ke SharePoint & Power Platform
- **MS365-COMPONENTS.md** - Komponen reusable dan code snippets

### 🎨 Design System
- **Font**: Segoe UI (SharePoint default)
- **Color Scheme**: Microsoft Fluent Design
  - Primary Blue: `#0078d4`
  - Hover Blue: `#106ebe`
  - Success Green: `#107c10`
  - Warning Orange: `#f7630c`
  - Error Red: `#d13438`

---

## 🔐 Authentication Flow (Simulasi)

### Login Flow
1. User klik "Masuk dengan Microsoft 365"
2. Modal muncul dengan input email
3. Masukkan password Microsoft
4. Simulasi loading 2 detik
5. Redirect ke dashboard

### Register Flow
1. **Step 1**: Input nama, telepon, tipe akun
2. **Step 2**: Email, password, konfirmasi password
3. **Step 3**: Review data, accept terms
4. Submit → Success modal
5. Email verification (simulasi)
6. Redirect ke login

> **Note**: Ini adalah halaman **statis untuk demo flow**. Tidak ada integrasi real ke Microsoft 365. Untuk production, gunakan MSAL.js dan Azure AD.

---## 🎨 Fitur Design

### Tech Stack
- **HTML5** - Semantic markup
- **Tailwind CSS** - Utility-first CSS framework (via CDN)
- **Font Awesome 6.4** - Icons (via CDN)
- **Responsive Design** - Mobile-first approach

### Design Elements
- **Color Scheme**: Indigo primary (#667eea), Purple secondary (#764ba2)
- **Typography**: Bold headlines, clear hierarchy
- **Components**: Cards, buttons, forms, accordions, grids
- **Animations**: Hover effects, transitions
- **Dummy Images**: placehold.co untuk semua images
- **Icons**: Font Awesome untuk UI elements

## 📊 Data Statis

Website ini dilengkapi dengan data dummy yang comprehensive:

### Statistik Utama
- 12,500+ lowongan kerja aktif
- 5,200+ perusahaan partner
- 85,000+ pencari kerja terdaftar
- 15,000+ penempatan sukses

### Sample Lowongan
- Senior Software Engineer (Rp 10-15 Juta)
- Data Analyst (Rp 6-9 Juta)
- HR Manager (Rp 7-10 Juta)
- UI/UX Designer (Rp 6-10 Juta)

### Sample Perusahaan
- PT. Teknologi Indonesia
- PT. Finansial Digital
- PT. Sumber Daya Manusia
- PT. Digital Creative
- PT. Retail Plus Indonesia
- PT. Logistik Sejaya

### Lokasi Coverage
- Jakarta
- Bandung
- Surabaya
- Medan

## 🔒 Keamanan & Privasi

- Sistem notifikasi email otomatis
- Dashboard HR untuk manajemen pelamar
- Akses role-based untuk menjaga privasi
- Upload CV & lamaran online
- Statistik dan laporan rekrutmen real-time

## 📱 Responsive Design

Semua halaman fully responsive untuk:
- Desktop (1024px+)
- Tablet (768px - 1023px)
- Mobile (< 768px)

## 🚀 Cara Menggunakan

1. Buka `index.html` di browser untuk melihat halaman utama
2. Gunakan navbar untuk navigasi antar halaman
3. Klik pada lowongan untuk melihat detail lengkap
4. Gunakan filter di halaman lowongan untuk pencarian
5. Daftar melalui halaman "Daftar" atau "Register"

## 📝 Fitur Utama

### Untuk Pencari Kerja
✅ Pencarian lowongan dengan filter
✅ Upload CV dan lamaran online
✅ Notifikasi email otomatis
✅ Akses dashboard personal
✅ Simpan lowongan favorit
✅ Track status lamaran

### Untuk Perusahaan
✅ Dashboard HR lengkap
✅ Kelola daftar pelamar
✅ Notifikasi lamaran masuk
✅ Statistik rekrutmen
✅ Follow-up management
✅ Access role-based

## 💡 Layout & Sections

Setiap halaman mencakup:
- **Navigation Bar** - Sticky header dengan logo, menu, tombol login/register
- **Header Section** - Judul dan deskripsi halaman
- **Main Content** - Konten utama dengan layout yang tepat
- **CTA Section** - Call-to-action untuk konversi
- **Footer** - Link navigasi, social media, copyright

## 📦 File Structure

```
carier-pro/
├── index.html              # Halaman utama
├── lowongan.html           # Daftar lowongan
├── perusahaan.html         # Daftar perusahaan
├── daftar.html             # Form registrasi pelamar
├── faq.html                # FAQ & Panduan
├── login.html              # Form login
├── register.html           # Pilihan registrasi
├── detail-lowongan.html    # Detail lowongan individual
└── README.md               # Dokumentasi ini
```

## 🎯 Instruksi Implementasi

Website ini dibuat sesuai instruksi dari tabel yang diberikan, mencakup:

- ✅ **Halaman Portal Karir** - Halaman utama dengan overview
- ✅ **Daftar Lowongan** - List dengan detail deskripsi, kualifikasi, lokasi, deadline
- ✅ **Upload CV & Lamaran** - Form upload file dengan drag & drop
- ✅ **Notifikasi Email** - Info tentang sistem notifikasi otomatis
- ✅ **Dashboard HR** - Info untuk manajemen pelamar
- ✅ **Statistik Rekrutmen** - Display statistik dan laporan
- ✅ **FAQ & Panduan** - 7 kategori dengan pertanyaan komprehensif
- ✅ **Akses Role-Based** - Info tentang keamanan dan privasi

## 🎨 Kustomisasi

Untuk mengubah warna:
1. Cari `from-indigo-600` atau `text-indigo-600` dalam file HTML
2. Ganti dengan warna Tailwind CSS yang diinginkan
3. Pilihan warna: slate, gray, zinc, neutral, stone, red, orange, amber, yellow, lime, green, emerald, teal, cyan, sky, blue, indigo, violet, purple, fuchsia, pink, rose

## 📄 Lisensi

Proyek ini adalah demo/dummy untuk keperluan presentasi. Menggunakan placeholder images dari placehold.co dan icons dari Font Awesome.

---

**Dibuat dengan ❤️ menggunakan HTML5, Tailwind CSS, dan Font Awesome**

Untuk pertanyaan atau modifikasi, silakan hubungi tim development.
