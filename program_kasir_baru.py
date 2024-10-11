def main():
    print("""
                        ====================================
                                     GEMA'Y RESTO                 
                                    Jl. Satunus 89                
                              Ruko Village blok F no.8            
                                JKT City, DKI Jakarta             
                                     021-51643782                 
                        ====================================""")
    print()

    print("""
    ================ MENU MAKANAN =================================== MENU MINUMAN ==================
    No Nama                 |       Harga          ===    No Nama                 |     Harga
    =================================================================================================
    1. Kari Kambing         |       Rp.41.000      ===    6. Milktea              |     Rp.10.000
    2. Soup Buntut          |       Rp.54.000      ===    7. Air Mineral          |     Rp.5.000 
    3. Chicken Grill        |       Rp.65.000      ===    8. Juice Mangga         |     Rp.15.000
    4. Tonyam               |       Rp.45.000      ===    9. Es Cendol            |     Rp.18.000
    5. Udang Mentega        |       Rp.75.000      ===    10.Es Teh Manis         |     Rp.12.000
    =================================================================================================
    """)

    import datetime
    import pandas as pd

    # tanggal dan waktu saat ini
    sekarang  = datetime.datetime.now()

    # tanggal
    tanggal   = sekarang.strftime("%Y-%m-%d")
    print("Tanggal        :",tanggal)

    # jam
    jam       = sekarang.strftime("%H:%M:%S")
    print("Jam            :",jam    )

    pelanggan = input("Nama Pelanggan : ")
    no_meja   = input("No. Meja       : ")
    kasir     = input("Kasir          : ")

    def order():
        menu=[]
        harga=[]
        porsi=[]
        kode=[]
        jumlah=[]

        pesan = int(input("\nBanyak Variasi Menu : "))
        for i in range(pesan):
            print("="*20)
            print("Menu ke-", i+1)
            kode.append(input("Masukkan Nomor Menu : "))
            porsi=int(input("Banyak Porsi        : "))

            if kode[i] == "1":
                menu.append("Kari Kambing")
                harga.append(41000*porsi)
                jumlah.append(porsi)
                print()
                print(porsi,menu[i],harga[i])
            elif kode[i] == "2":
                menu.append("Soup Buntut")
                harga.append(54000*porsi)
                jumlah.append(porsi) 
                print()
                print(porsi,menu[i],harga[i])
            elif kode[i] == "3":
                menu.append("Chicken Grill")
                harga.append(65000*porsi) 
                jumlah.append(porsi) 
                print()
                print(porsi,menu[i],harga[i])
            elif kode[i] == "4":
                menu.append("Tonyam")
                harga.append(45000*porsi) 
                jumlah.append(porsi) 
                print()
                print(porsi,menu[i],harga[i])
            elif kode[i] == "5":
                menu.append("Udang Mentega")
                harga.append(75000*porsi) 
                jumlah.append(porsi) 
                print()
                print(porsi,menu[i],harga[i])
            elif kode[i] == "6":
                menu.append("Milktea")
                harga.append(10000*porsi)
                jumlah.append(porsi) 
                print()
                print(porsi,menu[i],harga[i])
            elif kode[i] == "7":
                menu.append("Air Mineral")
                harga.append(5000*porsi)
                jumlah.append(porsi) 
                print()
                print(porsi,menu[i],harga[i])
            elif kode[i] == "8":
                menu.append("Juice Mangga")
                harga.append(15000*porsi)
                jumlah.append(porsi) 
                print()
                print(porsi,menu[i],harga[i])
            elif kode[i] == "9":
                menu.append("Es Cendol")
                harga.append(18000*porsi)
                jumlah.append(porsi) 
                print()
                print(porsi,menu[i],harga[i])
            elif kode[i] == "10":
                menu.append("Es Teh Manis")
                harga.append(12000*porsi)
                jumlah.append(porsi) 
                print()
                print(porsi,menu[i],harga[i])
            else:
                print("\nSalah input kode!!")
                ulang=input("Ulangi Pesanan ?[Y/T]")
                if ulang=="Y" or ulang=="y":
                        order()
                        exit()
                else:
                        exit()

        total=sum(harga)
        pajak=total*0.1
        total_semua=total+pajak

        data={
            "Menu": menu,
            "Jumlah": jumlah,
            "Harga": harga,
            }    

        data_plg = pd.DataFrame(data)
        data_plg.index +=1

        print("="*31)
        print("\tINVOICE PEMESANAN")
        print("="*31)
        print(data_plg)
        print("="*31)
        repeat=input("Ingin Ubah Pesanan? [Y/T]")
        if repeat=="Y" or repeat=="y":
                order()
                exit()
        else:
                print("Jumlah Harga        :Rp.",total)
                print("Pajak 10%           :Rp.",pajak)
                print("Total Bayar         :Rp.",total_semua)

        def bayar():
                uang = int(input("Tunai               :Rp. "))
                kembalian = int(uang-total_semua)
                print("Kembalian           :Rp. ", kembalian)

                if uang<total_semua:
                    print("Uang kurang")
                    bayar()
                    exit()
                
                # Struk
                print("==============================================")
                print("\nMencetak Struk .....     ")
                print("==============================================")
                print("                 GEMA'Y RESTO                 ")
                print("                Jl. Satunus 89                ")
                print("          Ruko Village blok F no.8            ")
                print("            JKT City, DKI Jakarta             ")
                print("                 021-51643782                 ")
                print("==============================================")
                print("Tanggal           :", tanggal)
                print("Jam               :", jam)
                print("Nama Pelanggan    :", pelanggan)
                print("No. Meja          :", no_meja)
                print("Kasir             :", kasir)
                print("==============================================")
                print("                     MENU                     ")
                print("==============================================")
                print(data_plg)
                print("==============================================")
                print("Total                 :Rp",total)
                print("Pajak 10%             :Rp",pajak)
                print("Total Bayar           :Rp",total_semua)
                print("Dibayar               :Rp",uang)
                print("Kembalian             :Rp",kembalian)
                print("==============================================")
                print("                TERIMA KASIH                  ")
                print("             SEMOGA DATANG LAGI               ")
                print("==============================================")
        bayar()
    order()
main()