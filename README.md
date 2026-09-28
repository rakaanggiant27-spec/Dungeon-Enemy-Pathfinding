# Dungeon Enemy Pathfinding

## Deskripsi
Program ini mensimulasikan Enemy yang mendeteksi Player di dalam dungeon. Enemy akan:
1. Mendeteksi posisi Player.
2. Menghitung jarak Enemy ke Player.
3. Mengecek apakah Player berada dalam jangkauan Enemy.
4. Jika Player berada dalam jangkauan, Enemy menggunakan algoritma A* (A-Star) untuk mencari jalur menuju Player.
5. Enemy bergerak mengikuti jalur yang ditemukan.

## 1. Identifikasi Algoritma

Algoritma yang digunakan adalah:

### A. Distance Check
Digunakan untuk menentukan apakah Player berada dalam jangkauan Enemy.

Rumus jarak Euclidean:

`distance = sqrt((x2 - x1)^2 + (y2 - y1)^2)`

Jika jarak <= detection range, Player dianggap terdeteksi.

### B. A* (A-Star) Pathfinding
A* digunakan untuk mencari jalur dari posisi Enemy menuju posisi Player dengan mempertimbangkan obstacle/dinding dungeon.

A* menggunakan:
- `g(n)` = biaya dari posisi awal ke node saat ini.
- `h(n)` = perkiraan jarak node saat ini ke tujuan.
- `f(n) = g(n) + h(n)` = nilai total yang digunakan untuk memilih node berikutnya.

### C. Enemy Movement
Setelah jalur ditemukan, Enemy bergerak dari satu node ke node berikutnya sampai mencapai posisi Player.

## 2. Flowchart

Flowchart tersedia pada file `flowchart.png`.

Alur utama:

START
↓
Enemy mendeteksi Player
↓
Hitung jarak Enemy → Player
↓
Apakah Player dalam jangkauan?
- Tidak → Enemy tetap melakukan patroli/menunggu → cek kembali
- Ya → Jalankan A*
↓
Apakah jalur ditemukan?
- Tidak → Enemy berhenti/patroli → cek kembali
- Ya → Enemy mengikuti jalur
↓
Apakah Enemy sudah mencapai Player?
- Tidak → lanjut bergerak
- Ya → Player tercapai / Enemy menyerang
↓
Selesai

## 3. Code Snippet

Bahasa pemrograman yang digunakan: **Python**.

Program menggunakan grid sederhana:
- `0` = area yang dapat dilewati
- `1` = obstacle/dinding
- `E` = posisi Enemy
- `P` = posisi Player

Program tidak membutuhkan library tambahan selain library bawaan Python.

## Cara Menjalankan

1. Download atau clone repository.
2. Buka terminal.
3. Jalankan:

```bash
python enemy_pathfinding.py
```

## Contoh Output

Program akan menampilkan:
- Posisi Enemy
- Posisi Player
- Jarak Enemy ke Player
- Status apakah Player berada dalam jangkauan
- Jalur A* yang ditemukan
- Langkah Enemy menuju Player

## Kesimpulan

Pada kasus ini, kombinasi **Distance Check + A* Pathfinding + Movement** digunakan agar Enemy dapat mendeteksi Player, menentukan apakah Player berada dalam jangkauan, menemukan jalur yang dapat dilewati, dan bergerak menuju Player.
