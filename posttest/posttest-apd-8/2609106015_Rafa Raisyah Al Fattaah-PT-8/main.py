import _user_data
import menu_gui
#Variabel

#Program Utama
def login():
    while _user_data.StatusUser != "none":
        _user_data.StatusUser = menu_gui.User_Check()
        menu_gui.klasifikasi_user()

login()