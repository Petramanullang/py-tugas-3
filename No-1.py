umur = int(input("Masukkan Umur: "))

if umur >= 18:
    status_bekerja = input("Masukkan Status Bekerja ya/tidak: ").lower()
    if status_bekerja == "ya":
            pendapatan_perbulan = int(input("Masukkan Pendapatan Perbulan: Rp."))
            jumlah_tanggungan = int(input("Masukkan Jumlah Tanggungan jika tidak ada ketik 0: "))
            # Kondisi Kalau Tanggungannya 0
            if jumlah_tanggungan == 0:
                biaya_hidup = pendapatan_perbulan
            # Kondisi Kalau Tanggungannya lebih dari 0
            else:
                biaya_hidup = pendapatan_perbulan / jumlah_tanggungan
                
            if biaya_hidup < 300000:
                print("\nAnda Penduduk Miskin")
            else:
                print("\nAnda Bukan Penduduk Miskin")
            
    elif status_bekerja == "tidak":
        # Kondisi di lewatkan
        pass

    else:
        print("\nANDA PENDUDUK MISKIN, di suruh milih ya/tidak malah jawab yang lain")

else:
    pass

if umur < 18 or status_bekerja == "tidak":
    status_sekolah = input("Masukkan Status Sekolah ya/tidak: ").lower()
    if status_sekolah == "ya":
        print("Anda Bukan Penduduk Miskin")
    elif status_sekolah == "tidak":
        print("\nAnda Penduduk Miskin")
    else:
        print("\nANDA PENDUDUK MISKIN, di suruh milih ya/tidak malah jawab yang lain")