import _user_data
from prettytable import PrettyTable
#Tidak bisa import menu gui jadi fungsi null sy pindahkan

def NUH_DiksiJoran(DiksiJoran : int, PilihanX : int):
    table = PrettyTable()
    table.field_names = ["Nama", "Ukuran", "Harga"]
    table.add_row([DiksiJoran["Joran_" + str(PilihanX)][0], 
                   DiksiJoran["Joran_" + str(PilihanX)][1],
                   DiksiJoran["Joran_" + str(PilihanX)][2]])
    return table

def CRUD_Null_Check(variables : str):
    if variables == "":
        return 1
    return 0

def CRUD_Dupe_Check(List1, List2):
    for isi1 in List1:
        for isi2 in List2:
            if isi1[0] == isi2:
                return 1
    return 0

def CRUD_Anomaly_Detector(ListX):
    #Cek Kosongan
    Kosong_Counter = 0
    for isi in ListX:
        if CRUD_Null_Check(isi) == 1:
            Kosong_Counter = 0
            print("Jangan masukkan huruf kosong!, silahkan coba lagi!")
            break
        else:
            Kosong_Counter = 1
    #Cek Digitan
    if not ListX[1].isdigit() or not ListX[2].isdigit():
        print("Dibagian Ukuran dan Harga tolong masukkan angka yang sesuai!")
        Kosong_Counter = 0
                        
    #Cek Duplikat
    if CRUD_Dupe_Check(dict_to_list(_user_data.DiksiJoran), ListX):
        print ("Terdeteksi adanya kesamaan dengan joran yang sudah ada!\n" \
                "Silahkan Coba Lagi!")
        Kosong_Counter = 0
    return Kosong_Counter
        
def dict_to_list(dictionary : dict):
    ListX = []
    for isi in dictionary.values():
        ListX.append(isi)
    return ListX

#Pilihan 1
def New_Joran(PilihanX):
    Kosong_Counter = 0

    while Kosong_Counter != 1:
        ListX = []
        PilihanX = input("Masukkan Nama Joran Baru: ")
        ListX.append(PilihanX)
        PilihanX = input("Masukkan Ukuran Joran (cm): ")
        ListX.append(PilihanX)
        PilihanX = input("Masukkkan Harga Joran (Rp): ")
        ListX.append(PilihanX)
        #Cek Kosongan
        Kosong_Counter = CRUD_Anomaly_Detector(ListX)
    
    #Perbaiki Format
    ListX[1] = (ListX[1] + "cm")
    ListX[2] = ("Rp." + ListX[2])
    return ListX

def Add_Joran(DiksiJoran : dict):
    PilihanX = ""
    while PilihanX != 'n':
        UkuranDiksiJoran = len(DiksiJoran)
        DiksiJoran.update({"Joran_" + str(UkuranDiksiJoran + 1) : New_Joran(PilihanX)})
        print("Joran Berhasil ditambahkan ke dalam katalog!")
        PilihanX = input("apakah anda ingin menambahkan joran lagi?\n" \
                         "ketik 'y' atau huruf lain jika iya\n" #disini kenapa eror pas '\' diletakan, saya tidak tau
                         "ketik 'n' jika tidak: " )
                         #Jika itu bekerja, jangan disentuh
#Pilihan 1

#Pilihan 2

def View_Joran(DiksiJoran : dict):
    PilihanX = ""
    while PilihanX != "n":
        print ("Nama-Nama Joran di Inventori")
        count = 0
        for key in DiksiJoran:
            count += 1
            print(str(count) + ".", DiksiJoran[key][0])
                        
        PilihanX = input("Untuk mengetahui lebih lanjut mengenai joran, ketik 'y', " \
                        "Untuk kembali ke menu, ketik 'n'\n" \
                        "Pilihan                          : ")    
        if PilihanX == 'y':
            while PilihanX != "n":
                PilihanX = input(
                            "Pilih angka Joran                : ")
                try:
                    print (NUH_DiksiJoran(DiksiJoran, PilihanX))
                    PilihanX = input("Ketik huruf apapun untuk lanjut, huruf 'n' untuk ke menu utama: ")
                    if PilihanX == 'n':
                        break
                except KeyError:
                    print ("Jangan masukkan angka negatif, string, atau angka yang tidak ada didalam dictionary!")
        elif PilihanX != "n":
            print ("Jangan masukkan huruf lain selain (y/n)")
#Pilihan 2

#Pilihan 3

def Tampilkan_Edit(iterasi: int, ListX : list):
    ListEdit = ["Nama baru     ", "Ukuran baru   ", "Harga baru    "]
    if iterasi == 0:
        print(ListEdit[0] + ": " + ListX[0])
        return 1
    else:
        Tampilkan_Edit(iterasi-1, ListX)
        print(ListEdit[iterasi] + ": " + ListX[iterasi])


def Edit_Diksi():
    Kosong_Counter = 0
    while Kosong_Counter != 1:
        PilihanY = ""
        ListX = []
        PilihanY = input("Nama          : ")
        ListX.append(PilihanY)
        PilihanY = input("Ukuran        : ")
        ListX.append(PilihanY)
        PilihanY = input("Harga         : ")
        ListX.append(PilihanY)
        print ("Mengedit Joran.............")

    #Cek Kosongan
        Kosong_Counter = CRUD_Anomaly_Detector(ListX)
    
    #Perbaiki Format
    ListX[1] = (ListX[1] + "cm")
    ListX[2] = ("Rp." + ListX[2])

    Tampilkan_Edit(2, ListX)
    return ListX

def Edit_Joran(DiksiJoran : dict):
    PilihanX = ""
    while PilihanX != "n":
        print("||||FORMAT PENYIMPANAN KATALOG||||")
        print(">>>>Nama, Ukuran, Harga<<<")
        count = 0
        for item in DiksiJoran:
            count += 1
            print(str(count) + ".", DiksiJoran[item][0], DiksiJoran[item][1], DiksiJoran[item][2])
        PilihanX = input("Pilih nomor item joran yang ingin diedit: ")
        try:
            print ("Data Joran:", DiksiJoran["Joran_" + str(PilihanX)])
            DiksiJoran["Joran_" + str(PilihanX)] = Edit_Diksi()
            print("Nama sukses terganti!")
            print ("apakah anda ingin mengedit lagi?\n" \
                    "ketik 'y' atau huruf selain 'n' jika iya\n" \
                    "ketik 'n' jika tidak")
            PilihanX = input(": ")
        except KeyError:
            print("Jangan masukkan angka negatif, string, atau angka yang tidak ada didalam dictionary!")
#Pilihan 3

#Pilihan 4
def Remove_Joran():
    PilihanX = ""
    while PilihanX != "n":
        DiksiX = {}
        try:
            PilihanX = input("Pilih nomor item joran yang ingin dihapus dari list: ")
            KeyX = "Joran_" + str(PilihanX)
            print("Menghapus Joran", _user_data.DiksiJoran[KeyX])
        except KeyError:
            print("Jangan masukkan angka negatif, string, atau angka yang tidak ada didalam dictionary!")
        else:
            _user_data.DiksiJoran.pop(KeyX) 
            print("Joran telah dihapus!")
            #Menyusun Ulang Urutan Joran
            count = 1
            for x in _user_data.DiksiJoran.values():
                DiksiX["Joran_" + str(count)] = x
                count += 1
            _user_data.DiksiJoran = DiksiX
            print ("apakah anda ingin menghapus lagi?\n" \
                    "ketik 'y' jika iya\n" \
                    "ketik 'n' jika tidak")
            PilihanX = input(": ")
#Pilihan 4