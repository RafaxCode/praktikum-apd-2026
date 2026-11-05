import CRUD
import os
import _user_data
import time
#time dan os = library lain
#Variables

#Menu
def menu_admin():
    #menu_admin
    print ("<||||[Selamat Datang menu admin]||||>")
    Pilihan = ""
    while Pilihan != "6":
        print ("Apa yang ingin anda lakukan?\n" \
            "1. Buat Kategori Joran Baru\n" \
            "2. Lihat Joran Yang Sudah Ada\n" \
            "3. Edit Nama Joran\n" \
            "4. Hapus Joran Dari Toko\n" \
            "5. Bersihkan Layar\n" \
            "6. Keluar Dari Menu Admin")
        Pilihan = input("Pilih Aksi: ")

        if Pilihan == "1": #Menambahkan Joran Baru
            CRUD.Add_Joran(_user_data.DiksiJoran)
                    
        elif Pilihan == "2":
            CRUD.View_Joran(_user_data.DiksiJoran)
                
        elif Pilihan == "3": #Edit Joran
            CRUD.Edit_Joran(_user_data.DiksiJoran)
                        
        elif Pilihan == "4": #Menghapus Joran dari List
            CRUD.Remove_Joran()

        elif Pilihan == "5":
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                
        elif Pilihan == "6":
            print("Terimakasih sudah menggunakan program ini !")
        else:
            print("Tolong Masukkan Input Yang Benar!")
        time.sleep(0.25)
        os.system("cls")
    #MENU ADMIN

def menu_user():
    global DiksiJoran
    print("░███     ░███    ░███    ░██     ░██    ░███    ░██     ░██    ░███    ░███     ░███        ░█████    ░███    ░██     ░██    ░███    \n" \
          "░████   ░████   ░██░██   ░██     ░██   ░██░██   ░██    ░██    ░██░██   ░████   ░████          ░██    ░██░██    ░██   ░██    ░██░██   \n" \
          "░██░██ ░██░██  ░██  ░██  ░██     ░██  ░██  ░██  ░██   ░██    ░██  ░██  ░██░██ ░██░██          ░██   ░██  ░██    ░██ ░██    ░██  ░██  \n" \
          "██ ░████ ░██ ░█████████ ░██████████ ░█████████ ░███████    ░█████████ ░██ ░████ ░██          ░██  ░█████████    ░████    ░█████████\n" \
          "░██  ░██  ░██ ░██    ░██ ░██     ░██ ░██    ░██ ░██   ░██   ░██    ░██ ░██  ░██  ░██    ░██   ░██  ░██    ░██     ░██     ░██    ░██ \n" \
          "░██       ░██ ░██    ░██ ░██     ░██ ░██    ░██ ░██    ░██  ░██    ░██ ░██       ░██    ░██   ░██  ░██    ░██     ░██     ░██    ░██\n" \
          "░██       ░██ ░██    ░██ ░██     ░██ ░██    ░██ ░██     ░██ ░██    ░██ ░██       ░██     ░██████   ░██    ░██     ░██     ░██    ░██ ")
    print ("<||||[Selamat Datang di Toko Pancing Mahakam Jaya]||||>")
    Pilihan = ""
    while Pilihan != "3":
        print ("Apa yang ingin anda lakukan?\n" \
               "1. Lihat Katalog Joran Yang Ada\n" \
               "2. Bersihkan Layar\n" \
               "3. Keluar Dari Menu User")
        Pilihan = input("Pilih Aksi: ")
        if Pilihan == "1":
            CRUD.View_Joran(_user_data.DiksiJoran)
        elif Pilihan == "2":
            os.system("cls")
        elif Pilihan != "3":
            print("Silahkan Coba Lagi!")
            time.sleep(0.25)
            os.system("cls")
        time.sleep(0.25)
        os.system("cls")
    #MENU USER
    os.system("cls")
    print("Terimakasih Sudah Menggunakan Layanan Kami!")

def Dupe_Check(PilihanX : str):
    StatusDuplikat = 0
    for keys in _user_data.DiksiUser.keys():
        if keys != PilihanX:
            StatusDuplikat = 0
        else:
            StatusDuplikat = 1
            print ("Akun dengan nama itu sudah ada, silahkan coba lagi!")
            break
    return StatusDuplikat

def Null_Check(variables : str):
    if variables == "":
        return 1
    return 0

def Create_Account(DiksiUser : dict):
    print("Anda mau buat akun baru? silahkan silahkan!")
    PilihanX = ""
    while PilihanX != "n":
        PilihanX = input("Masukkan Nama     : ")
        PilihanY = input("Masukkan Password : ")
        if Dupe_Check(PilihanX) == 0 and Null_Check(PilihanX) != 1 and Null_Check(PilihanY) != 1:
            DiksiUser.update({PilihanX : PilihanY})
        elif Null_Check(PilihanX) == 1 or Null_Check (PilihanY) == 1:
            print("Jangan masukkan huruf kosong!")

        PilihanX = input("ketik apapun untuk membuat akun lagi!\n" \
                         "ketik n untuk kembali ke menu: ")
    #Sistem Registrasi

def User_Check():
    PilihanA = ""
    StatusUser = ""
    while PilihanA != "4":
        print("<||||[Selamat Datang Toko Pancing Mahakam Jaya]||||>\n" \
            "Saat ini, anda login sebagai:\n" \
            "1. User\n" \
            "2. Admin \n" \
            "3. Buat Akun\n" \
            "4. Keluar")
        PilihanA = input("Masukkan Pilihan: ")
        if PilihanA == "1":
            StatusUser = "user"
            break
        elif PilihanA == "2":
            StatusUser = "admin"
            break
        elif PilihanA == "3": #Fitur ini cuma untuk mengisi kuota nilai plus
            Create_Account(_user_data.DiksiUser)
        elif PilihanA == "4":
            StatusUser = "none"
        else:
            print("Jangan Masukkan hal lain. Be a human")
    return StatusUser

def admin_login():
    StatusLogin = 0 #0 false, 1 true
    percobaan = 0
    while percobaan < 3:
        PilihanX = input("Username: ")
        PilihanY = input("Password: ")
        if PilihanX == _user_data.username and PilihanY == _user_data.password:
            StatusLogin = 1
            percobaan += 3                                                                           
            print("                                                         LOGIN BERHASIL")
            print("░███     ░███    ░███    ░██     ░██    ░███    ░██     ░██    ░███    ░███     ░███        ░█████    ░███    ░██     ░██    ░███    \n" \
                "░████   ░████   ░██░██   ░██     ░██   ░██░██   ░██    ░██    ░██░██   ░████   ░████          ░██    ░██░██    ░██   ░██    ░██░██   \n" \
                "░██░██ ░██░██  ░██  ░██  ░██     ░██  ░██  ░██  ░██   ░██    ░██  ░██  ░██░██ ░██░██          ░██   ░██  ░██    ░██ ░██    ░██  ░██  \n" \
                "██ ░████ ░██ ░█████████ ░██████████ ░█████████ ░███████    ░█████████ ░██ ░████ ░██          ░██  ░█████████    ░████    ░█████████\n"   \
                "░██  ░██  ░██ ░██    ░██ ░██     ░██ ░██    ░██ ░██   ░██   ░██    ░██ ░██  ░██  ░██    ░██   ░██  ░██    ░██     ░██     ░██    ░██ \n" \
                "░██       ░██ ░██    ░██ ░██     ░██ ░██    ░██ ░██    ░██  ░██    ░██ ░██       ░██    ░██   ░██  ░██    ░██     ░██     ░██    ░██\n"  \
                "░██       ░██ ░██    ░██ ░██     ░██ ░██    ░██ ░██     ░██ ░██    ░██ ░██       ░██     ░██████   ░██    ░██     ░██     ░██    ░██ ")
        else:
            print("Login Gagal, Silahkan coba lagi")
            percobaan += 1
    if percobaan >= 3 and StatusLogin == 0:
        print("Silahkan renungkan kembali pilihan hidupmu, dan coba lah mengingat apa passwordmu")
        return
    else:
        menu_admin()
    #ADMIN LOGIN

def user_login():
    count = 0
    _user_data.StatusUser = "noob"
    while count < 3:
        PilihanX = input("Username: ")
        PilihanY = input("Password: ")
        is_duplikat = 0 #photos_printed?
        for keys in _user_data.DiksiUser:
            if keys != PilihanX and _user_data.DiksiUser[keys] != PilihanY:
                _user_data.StatusUser = "noob"
                if is_duplikat != 1:
                    print("Gagal login, silahkan coba lagi!")
                    is_duplikat = 1 
                continue
            elif keys == PilihanX and _user_data.DiksiUser[keys] == PilihanY:
                _user_data.StatusUser = "user"
                count += 3
                break
            else:
                _user_data.StatusUser = "noob"
                if is_duplikat != 1:
                    print("Gagal login, silahkan coba lagi!")
                    is_duplikat = 1 
        count += 1
    #USER LOGIN

def klasifikasi_user():
    if _user_data.StatusUser == "admin":
        admin_login()
    elif _user_data.StatusUser == "user":
        user_login()
        #Jika login sukses, StatusUser tidak akan berubah
        if _user_data.StatusUser == "user":
            menu_user()
        else:
            print("Gagal Login, Silahkan reboot aplikasi dan buat akun baru!")
            #Selesai
    elif _user_data.StatusUser == "none":
        print("Terimakasih Sudah Menggunakan Layanan Kami!")



