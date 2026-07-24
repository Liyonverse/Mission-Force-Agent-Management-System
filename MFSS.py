#Data
id=[]
code_name=[]
real_name=[]
country=[]
mission_stts=[]

#Login_Page
def main():
    login()
    while(True):
        os.system("cls")
        print("==========================================================")
        print("          MISSION FORCE CONTROL PANEL")
        print("==========================================================")
        print("1. Register New Agent")
        print("2. View All Agents")
        print("3. Search Agent")
        print("4. Update Agent")
        print("5. Delete Agent")
        print("6.Secret Terminal")
        print("7.Exit")
        menu_com=input("Enter Command ").lower()
    #process
        if (menu_com == "1"):
            register()
        elif (menu_com == "2"):
            view()
            exit_reg=input("Press Enter key to Exit...")
            os.system("cls")
        elif (menu_com == "3"):
            search()
        elif (menu_com == "4"):
            update()
            os.system("cls")
        elif (menu_com == "5"):
            delete()
            os.system("cls")
            continue
        elif(menu_com == "6"):
            terminal()
        elif(menu_com == "7"):
            break
        else:
            print("")
            print("\033[33mERROR 302\033[0m")
            print("\033[33mUnknown Command.\033[0m")
            print("\033[33mPlease Enter A Valid Operation.\033[0m")
            print("")
    print("Closing Secure Connection...")
    time.sleep(1)
    print("Logging Out...")
    time.sleep(1)
    print("Mission Force Server Offline.")
    time.sleep(1)
    os.system("cls")











#defines
import os
import time
def login_system():
    username=["Liyon","Kisha","Kavidaf"]
    password=["Spidy","Tiger","Batman"]
    print(">> Login ")
    print("")
    while(True):
        u_name=input("User Name : ")
        p_word=input("Password : ")
        count=0
        while(count<len(username)):
            if(u_name==username[count]):
                if(p_word==password[count]):
                    Do="First"
                    break
                else:
                    Do="Secound"
                    break
            else:
                count=count+1
                Do="Secound"
                continue
        if(Do=="First"):
            break
        else:
            print("Access Denied")
            continue
def register():
    os.system("cls")
    print(">> Register New Agent")
    print("")
    id.append(input("Agent ID : ")).strip()
    code_name.append(input("Code Name : ")).strip().title()
    real_name.append(input("Real Name : ")).strip().title()
    country.append(input("Country : ")).strip().title()
    mission_stts.append(input("Mission Status : ")).strip().title()
    print("")
    print("\033[34mAgent Successfully Registered.\033[0m")
    exit_reg=input("Press Enter key to Exit...")
    os.system("cls")
def view():
    os.system("cls")
    print("==========================================================")
    print("                  Registered Agents")
    print("==========================================================")
    count=0
    while(count<len(id)):
        print("")
        print("ID : ",id[count])
        print("Code Name : ",code_name[count])
        print("Real Name : ",real_name[count])
        print("Country : ",country[count])
        print("Mission Status : ",mission_stts[count])
        count = count +1
def delete():
    del_code=(input("Code Name : ")).strip().title()
    print("\033[33mWARNING\033[0m")
    print("")
    print("\033[33mThis operation cannot be undone.\033[0m")
    print("")
    print("\033[33mDelete Agent?\033[0m")
    print("")
    conf=input("Y/N ").lower()
    if (conf == "y"):
        count=0
        while(count<len(code_name)):
            if(del_code==code_name[count]):
                id.pop(count)
                code_name.pop(count)
                real_name.pop(count)
                country.pop(count)
                mission_stts.pop(count)
                print("\033[34mAgent Successfully Deleted.\033[0m")
                exit_del=input("Press Enter key to Exit...")
                os.system("cls")
                break
            else:
                count=count+1
                continue
def search():
    search_code=(input("Code Name : ")).strip().title()
    count=0
    while(count<len(code_name)):
        if(search_code==code_name[count]):
            print("Searching...")
            time.sleep(2)
            print("Got it...")
            time.sleep(2)
            os.system("cls")
            print("Detailes of ",search_code)
            print("")
            print("ID : ",id[count])
            print("Code Name : ",code_name[count])
            print("Real Name : ",real_name[count])
            print("Country : ",country[count])
            print("Mission Status : ",mission_stts[count])
            print("")
            exit_search=input("Press Enter key to Exit...")
            os.system("cls")
            break
        else:
            count=count+1
def update():
    os.system("cls")
    print(">> Update Agent")
    print("")
    update_code=input("Enter the Code Name...").strip().title()
    count=0
    while(count<len(code_name)):
        if(update_code==code_name[count]):
            id[count]=(input("Agent ID : "))
            code_name[count]=(input("Code Name : "))
            real_name[count]=(input("Real Name : "))
            country[count]=(input("Country : "))
            mission_stts[count]=(input("Mission Status : "))    
            print("\033[34mAgent Successfully Updated.\033[0m")
            update_del=input("Press Enter key to Exit...")
            os.system("cls")
            break
        else:
            count=count+1
            continue
def terminal():
    os.system("cls")
    print("MISSION FORCE SECURE SERVER v1.0")
    print("")
    print("Author : Liyon")
    exit_reg=input("Press Enter key to Exit...")
    os.system("cls")
def login():
        print("==========================================================")
        print("          MISSION FORCE SECURE SERVER v1.0")
        print("==========================================================")
        print("")
        print("Security Status : ACTIVE")
        print("Database Status : ENCRYPTED")
        print("Classification  : TOP SECRET")
        print("")
        print("Login Required...")
        login_system()
        print("Initializing Server...")
        time.sleep(1)
        print("[##########] 100%")
        time.sleep(1)
        print("Loading Agent Database...")
        time.sleep(1)
        print("Done.")
        time.sleep(1)
        print("Connecting...")
        time.sleep(1)
        print("Connection Secure.")
        time.sleep(1)
        #main_menu
        os.system("cls")


if __name__ == "__main__" :
    main()
