# Instruksi Pemasangan untuk Agent

Paket ini berisi 10 skill penulisan ilmiah + satu SOUL.md. SOUL.md adalah perekatnya: di dalamnya tertulis kewajiban memuat tumpukan skill setiap kali menulis karya ilmiah. Karena SOUL.md menentukan persona dan perintah tetap agent, pemasangannya WAJIB mengikuti tata cara berikut. Jangan memasang apa pun sebelum langkah 3 selesai.

## Langkah 1 — Jelaskan dulu ke user

Sampaikan ringkas: paket ini akan memasang 10 skill penulisan, dan agar tumpukan itu termuat otomatis, SOUL.md user perlu diganti dengan SOUL.md dari paket ini (persona penulis akademik + tumpukan skill wajib di Bagian 7). Jangan membingkai ini sebagai hal kecil: penggantian SOUL.md mengubah cara agent bekerja.

## Langkah 2 — Cadangkan SOUL.md asli

Sebelum bertanya pun, buat cadangan SOUL.md user saat ini, misalnya `SOUL.md.bak-<tanggal>`. Cadangan ini jalan pemulihan user kapan pun ia ingin kembali.

## Langkah 3 — Minta persetujuan user secara eksplisit

Tanyakan dengan jelas, misalnya:

"SOUL.md kamu akan dicadangkan, lalu diganti dengan SOUL.md dari Paket Penulisan Ilmiah. Sesudah diganti, persona dan perintah tetapku mengikuti berkas itu, termasuk kewajiban memuat 10 skill penulisan setiap menulis karya ilmiah. Cadangan SOUL.md aslimu tersimpan dan bisa dipulihkan kapan pun. Kamu setuju?"

Hanya lanjut ke langkah 4 bila user menjawab setuju secara eksplisit. Keraguan atau jawaban tidak jelas berarti TIDAK.

## Langkah 4 — Bila user setuju

1. Timpa SOUL.md dengan SOUL.md dari paket ini.
2. Pasang skillnya:
   - Versi 1 (Lengkap): kesepuluh skill ada di folder `skills/` paket ini; salin semuanya ke folder custom-skills.
   - Versi 2 (Karya Asli): hanya 4 skill di folder `skills/` paket ini. Enam skill antislop WAJIB diambil dari repositori resmi pembuatnya, https://github.com/miqdadbadjuber/anti-slop (folder `skills/antislop`, `antislop-ui`, `antislop-copywriting`, `antislop-human`, `antislop-layoutmobile`, `antislop-code`), dipasang dengan nama `local-antislop*`. Jangan mengambil antislop dari sumber lain.
   - Alternatif yang sama hasilnya: jalankan `bash install.sh` dari paket ini; skrip itu mencadangkan SOUL.md, meminta persetujuan sebelum menimpa, lalu memasang semuanya.
3. Laporkan ke user: skill yang terpasang, versi antislop yang terpasang, dan lokasi berkas cadangan SOUL.md aslinya.

## Langkah 5 — Bila user tidak setuju

Jangan menimpa SOUL.md. Tawarkan memasang skillnya saja, dan jelaskan akibatnya dengan jujur: tanpa SOUL.md paket ini, tumpukan skill tidak termuat otomatis setiap sesi, karena perintah memuatnya tertulis di SOUL.md. Bila user mau, tawarkan jalan tengah: menempelkan hanya Bagian 7 SOUL.md paket ini (daftar tumpukan skill) ke dalam SOUL.md user yang sudah ada, juga hanya sesudah persetujuannya.
