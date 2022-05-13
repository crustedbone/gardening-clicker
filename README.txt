Bot ini digunakan pada layar 1920x1080. Bot menggunakan Python 3.9. Bot berfungsi untuk mengerjakan life skill gardening pada permainan Ragnarok X: Next Generation.
Bot ini akan bekerja sebagai berikut:
1. Mengecek dan menekan tombol gardening jika muncul
2. jika muncul captcha maka akan mengisi captcha tersebut
3. Bot akan berhenti ketika sudah tidak hujan atau degan menekan tombol 'esc'

Tutorial:
1. Install Python 3.9 dan contreng "add to path" checkbox saat install
2. Install library python dalam (Admin) command prompt sebagai berikut:
	pip install pywin32
	pip install keyboard
	pip install pyautogui
	pip install Pillow
	pip install pytesseract
3. Install Tesseract OCR 
	https://github.com/tesseract-ocr/tesseract
	gw sih pake versi 5.0.1.20220107
4. Jangan lupa ganti directory tesseract dalam bot
5. Cek posisi pixel menggunakan position.py
6. Tidak disarankan menggunakan compiler selain IDLE editor untuk menjalankan bot namun bisa menggunakan command prompt biasa untuk menjalankannya dengan cara:
	-pindah ke directory botnya
	-ketik : python namaApp.py

Note:
-Tekan keyboard 'K' untuk pause bot
-Tekan keyboard '+' untuk unpause bot
-Tekan keyboard 'esc' saat unpause untuk stop

Referensi:
https://www.youtube.com/watch?v=fFOdqjBnSBw&t=99s
https://www.youtube.com/watch?v=YRAIUA-Oc1Y&t=745s
