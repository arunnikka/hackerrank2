# 1. insert i e: Masukkan bilangan bulat pada posisi .
# 2. print: Mencetak daftar.
# 3. remove e: Hapus kemunculan pertama bilangan bulat .
# 4. append e: Sisipkan bilangan bulat di akhir daftar. 
# 5. sort: Mengurutkan daftar.
# 6. pop: Munculkan elemen terakhir dari daftar.
# 7. reverse: Balikkan daftar.

angka = []
angka.insert(0, 6)
angka.insert(1, 5)
angka.insert(2, 10)
print(angka)
angka.remove(6)
angka.append(9)
angka.append(1)
angka.sort()
print(angka)
angka.pop(-1)
angka.reverse()
print(angka)
