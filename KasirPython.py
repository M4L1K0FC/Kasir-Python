import datetime
sekarang = datetime.datetime.now()

print("------------ SELAMAT DATANG DI WARUNG SAYA ------------")
print("Waktu:", sekarang)
pembeli = input("Masukkan nama Pembeli: ")
print ("Nama Pembeli :", pembeli) 

def fungsimakanan():
   global totalmkn
   global porsi
   global mkn
   print ("\n----------------- Menu Makanan -----------------")
   print("1. Nasi Goreng - Rp 8000")
   print("2. Soto - Rp 9000")
   print("3. Mie Ayam - Rp 11000")
   print("4. Bakso - Rp 17000")
   print("5. Sate Kambing - Rp 14000")
   print("6. Sop Buntut - Rp 23000")
   print("7. Seblak - Rp 15000")
   print("8. Steak Sapi - Rp 25000")
   print("9. Sambel Bakar - Rp 12000")
   print("10. Kentang Goreng - Rp 10000")
   nomor=int(input("Masukan Pilihan: "))
   porsi= int(input("Berapa Porsi: "))
   
   if nomor==1:
       totalmkn=porsi*8000
       print (porsi," porsi Nasi Goreng = Rp", totalmkn)
       mkn=("Nasi Goreng")
   elif nomor==2:
       totalmkn=porsi*9000
       print (porsi," porsi Soto = Rp", totalmkn)
       mkn=("Soto")
   elif nomor==3:
       totalmkn=porsi*11000
       print (porsi, " porsi Mie Ayam = Rp", totalmkn)
       mkn=("Mie Ayam")
   elif nomor==4:
       totalmkn=porsi*17000
       print (porsi, " porsi Bakso = Rp", totalmkn)
       mkn=("Bakso")
   elif nomor==5:
       totalmkn=porsi*14000
       print (porsi, " porsi Sate Kambing = Rp", totalmkn)
       mkn=("Sate Kambing")
   elif nomor==6:
       totalmkn=porsi*23000
       print (porsi, " porsi Sop Buntut = Rp", totalmkn)
       mkn=("Sop Buntut ")
   elif nomor==7:
       totalmkn=porsi*15000
       print (porsi," porsi Seblak = Rp", totalmkn)
       mkn=("Seblak")
   elif nomor==8:
       totalmkn=porsi*25000
       print (porsi, " porsi Steak Sapi = Rp", totalmkn)
       mkn=("Steak Sapi")
   elif nomor==9:
       totalmkn=porsi*12000
       print (porsi, " porsi Sambel Bakar = Rp", totalmkn)
       mkn=("Sambel Bakar")
   elif nomor==10:
       totalmkn=porsi*10000
       print (porsi, " porsi Kentang Goreng = Rp", totalmkn)
       mkn=("Kentang Goreng")
   else:
      print("Maaf Pilihan Anda Tidak Ada Dalam Menu!!")
      print("Harap Masukan Pesanan Anda Kembali!!")
      fungsimakanan()

def fungsiminuman():
   global totalmnm
   global mnm
   global gelas
   print("\n----------------- Menu Minuman -----------------")
   print("1. Es teh - Rp 2000")
   print("2. Es jeruk - Rp 3500")
   print("3. Es kopi - Rp 4000")
   print("4. Es Dawet - Rp 6000")
   print("5. Es Doger - Rp 7000")
   print("6. Es Cendol - Rp 5500")
   print("7. Es Serut - Rp 7000")
   print("8. Es Buah - Rp 9000")
   print("9. Es Pisang Ijo - Rp 8000")
   print("10. Es Oyen - Rp 6500")
   nomor=int(input("Masukan Pilihan: "))
   gelas= int(input("Berapa Gelas: "))

   if nomor==1:
       totalmnm=gelas*2000
       print (gelas," Es Teh = Rp", totalmnm)
       mnm=(" Gelas Es Teh")
   elif nomor==2:
       totalmnm=gelas*3500
       print (gelas, " Gelas Es Jeruk = Rp", totalmnm)
       mnm=("Es Jeruk")
   elif nomor==3:
       totalmnm=gelas*4000
       print (gelas, " Gelas Es Kopi = Rp", totalmnm)
       mnm=("Es Kopi")
   elif nomor==4:
       totalmnm=gelas*6000
       print (gelas, " Gelas Es Dawet = Rp", totalmnm)
       mnm=("Es Dawet")
   elif nomor==5:
       totalmnm=gelas*7000
       print (gelas, " Gelas Es Doger = Rp", totalmnm)
       mnm=("Es Doger")
   elif nomor==6:
       totalmnm=gelas*5500
       print (gelas, " Gelas Es Cendol = Rp", totalmnm)
       mnm=("Es Cendol")
   elif nomor==7:
       totalmnm=gelas*7000
       print (gelas, " Gelas Es Serut = Rp", totalmnm)
       mnm=("Es Serut") 
   elif nomor==8:
       totalmnm=gelas*9000
       print (gelas, " Gelas Es Buah = Rp", totalmnm)
       mnm=("Es Buah")
   elif nomor==9:
       totalmnm=gelas*8000
       print (gelas, " Gelas Es Pisang Ijo = Rp", totalmnm)
       mnm=("Es Pisang Ijo") 
   elif nomor==10:
       totalmnm=gelas*6500
       print (gelas, " Gelas Es Oyen = Rp", totalmnm)
       mnm=("Es Oyen")     
   else:
      print("Maaf Pilihan Anda Tidak Ada Dalam Menu")
      print("Harap Masukan Pesanan Anda Kembali!!")
      fungsiminuman()

fungsimakanan()
fungsiminuman()
totalsemua=totalmkn+totalmnm

print("\n------------------ Pembayaran ------------------")
print("\nTotal harus Dibayar : Rp",totalsemua)
uang=int(input("Masukan Nominal Uang Anda : Rp "))
kembalian=int(uang-totalsemua)
print("Kembalian :",kembalian)

print("\n==================================")
print("======= S T R U K   B E L I ======")
print("==================================")
print ("Nama\t\t:",pembeli)
print("Waktu Pembayaran:", sekarang)
print ("Beli\t\t:",porsi,mkn,"( Rp", totalmkn,")")
print ("\t\t ",gelas,mnm,"( Rp", totalmnm,")")
print ("Tagihan\t\t: Rp",totalsemua)
print ("Dibayar\t\t: Rp",uang)
print ("Kembalian\t: Rp",kembalian)
print("==================================")
print("===== T E R I M A  K A S I H =====")
print("==================================")
