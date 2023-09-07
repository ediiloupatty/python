import random

def pilihan_komputer():
    pilihan = ['batu', 'kertas', 'gunting']
    return random.choice(pilihan)

def tentukan_pemenang(pemain, komputer):
    if pemain == komputer:
        return 'Seri'
    elif pemain == 'batu':
        return 'Pemain Menang!' if komputer == 'gunting' else 'Komputer Menang!'
    elif pemain == 'kertas':
        return 'Pemain Menang!' if komputer == 'batu' else 'Komputer Menang!'
    elif pemain == 'gunting':
        return 'Pemain Menang!' if komputer == 'kertas' else 'Komputer Menang!'

def main():
    print("Selamat datang di game Batu, Kertas, Gunting!")
    while True:
        pilihan_pemain = input("Masukkan pilihan Anda (batu, kertas, gunting) atau 'keluar' untuk berhenti: ").lower()

        if pilihan_pemain == 'keluar':
            break

        if pilihan_pemain not in ['batu', 'kertas', 'gunting']:
            print("Pilihan tidak valid!")
            continue

        pilihan_komp = pilihan_komputer()
        print(f"Komputer memilih: {pilihan_komp}")
        
        hasil = tentukan_pemenang(pilihan_pemain, pilihan_komp)
        print(hasil)
        print("-" * 40)

if __name__ == "__main__":
    main()
