print("Kriteria Penilaian Siswa")
nilai=float(input("Masukan Nilai :"))
try: 
    if nilai<=0.3 :
        print("Nilai Akhir : E")
    elif nilai<=0.5 :
        print("Nilai Akhir : D")
    elif nilai<=0.65 :
        print("Nilai Akhir : C")
    elif nilai<= 0.85 :
        print("Nilai Akhir : B")
    elif nilai<=1.0 :
        print("Nilai Akhir : A")
    else :
        print("Masukan Nilaimu Kembali")
except:  