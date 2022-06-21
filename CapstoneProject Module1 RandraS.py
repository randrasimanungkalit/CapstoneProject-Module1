
list_contact = {
        'rsmitraabadi' :{'No.Id':'001','Sektor':'Kesehatan','Nama':'RS Mitra Abadi','Alamat':'Jln. Bekasi Raya no 2','Phone':'021-444555'},
        'rssehatterus' :{'No.Id':'002','Sektor':'Kesehatan','Nama':'RS Sehat Terus','Alamat':'Jln. Kalimalang no 45','Phone':'021-666777'},
        'cyberindonesia' :{'No.Id':'003','Sektor':'Keamanan','Nama':'Cyber Indonesia','Alamat':'Jln. Pondok Gede no 1','Phone':'021-888999'},
        'securityindonesia' :{'No.Id':'004','Sektor':'Keamanan','Nama':'Security Indonesia','Alamat':'Jln. Cipinang no 8','Phone':'021-101010'},
        'financeindonesia' :{'No.Id':'005','Sektor':'Keuangan','Nama':'Finance Indonesia','Alamat':'Jln. Sudirman  no 5','Phone':'021-123456'},
        'insuranceindonesia' :{'No.Id':'006','Sektor':'Keuangan','Nama':'Insurance Indonesia','Alamat':'Jln. Dukuh Atas no 9','Phone':'021-654321'}
    }


def default_contact():
    if len(list_contact) == 0:
        print('Contact not Found')
    else:
        print('='*83)
        print(' ' *30+'CONTACT BOOK LIST')
        print('='*83)
        print('No.Id \t|Sektor \t|Nama \t\t\t|Alamat \t\t|Phone')
        for key in list_contact.keys():
            print('{} \t|{} \t|{} \t|{} \t|{}\t'.format(list_contact[key]['No.Id'],list_contact[key]['Sektor'],list_contact[key]['Nama'],list_contact[key]['Alamat'],list_contact[key]['Phone']))

def view_contact():
    while len(list_contact) == 0:
        print('Contact not Found')
        break
    else:
        while True:
            pilih_menu = int(input('=====CONTACT MENU===== \n1. View by Sector\n2. View All Contacts\n3. Search by Name\n4. Back to Main Menu\n Choose Menu Number: '))
            if pilih_menu == 1:
                pilih_sector = int(input('=====SECTOR LIST=====\n1. Kesehatan\n2. Keuangan\n3. Keamanan\n4. Back to Main Menu\n Choose Sector: '))
                if pilih_sector == 1:
                    print('No.Id \t|Sektor \t|Nama \t\t\t|Alamat \t\t|Phone')
                    for key in list_contact.keys():
                        if list_contact[key]['Sektor'] == 'Kesehatan':
                            print('{} \t|{} \t|{} \t|{} \t|{}\t'.format(list_contact[key]['No.Id'],list_contact[key]['Sektor'],list_contact[key]['Nama'],list_contact[key]['Alamat'],list_contact[key]['Phone']))
                        else:
                            continue
                elif pilih_sector == 2:
                    print('No.Id \t|Sektor \t|Nama \t\t\t|Alamat \t\t|Phone')
                    for key in list_contact.keys():
                        if list_contact[key]['Sektor'] == 'Keuangan':
                            print('{} \t|{} \t|{} \t|{} \t|{}\t'.format(list_contact[key]['No.Id'],list_contact[key]['Sektor'],list_contact[key]['Nama'],list_contact[key]['Alamat'],list_contact[key]['Phone']))
                        else:
                            continue
                elif pilih_sector == 3:
                    print('No.Id \t|Sektor \t|Nama \t\t\t|Alamat \t\t|Phone')
                    for key in list_contact.keys():
                        if list_contact[key]['Sektor'] == 'Keamanan':
                            print('{} \t|{} \t|{} \t|{} \t|{}\t'.format(list_contact[key]['No.Id'],list_contact[key]['Sektor'],list_contact[key]['Nama'],list_contact[key]['Alamat'],list_contact[key]['Phone']))
                        else:
                            continue
                elif pilih_sector == 4:
                    break
                else:
                    print('Sector not Found')
            elif pilih_menu == 2:
                default_contact()
            elif pilih_menu == 3:
                search = input("Search Contact Name: ")
                print('No.Id \t|Sektor \t|Nama \t\t\t|Alamat \t\t|Phone')
                for key in list_contact.keys():
                    if search.lower() in list_contact[key]["Nama"].lower():
                        print('{} \t|{} \t|{} \t|{} \t|{}'.format(list_contact[key]["No.Id"],list_contact[key]["Sektor"],list_contact[key]["Nama"],list_contact[key]["Alamat"],list_contact[key]["Phone"]))
                    else:
                        continue
            elif pilih_menu == 4:
                break
            else:
                print('Menu not Found')  

def add_contact():
    while True:
        default_contact()
        input_nama = input('Enter name: ')
        new_name_input = input_nama.replace(' ','')
        if new_name_input.lower() not in list_contact.keys():
            print('Please fill in the new contact information')
            input_new_name = input('Enter Name: ')
            input_noid = input('Enter No.Id: ')
            input_sector = input('Enter Sector: ')
            input_address = input('Enter Address: ')
            input_phone = input('Enter Phone: ')
            cek = input(f'Are you sure you want to add this all information = {input_new_name},{input_noid},{input_sector},{input_address},{input_phone} Yes/No: ')
            if cek != 'Yes':
                print('Contact is cancel to add')
                break
            else:
                list_contact[new_name_input.lower()]={'No.Id' : input_noid, 'Sektor': input_sector,'Nama': input_new_name,'Alamat': input_address,'Phone': input_phone}
                default_contact()
                print('Contact added to list')
                break
        else:
            print('Contact Name already listed')
            break

def update_contact():
    update_contact = int(input('=====CONTACT UPDATE=====\n1. Update by Name\n2. Back to Main Menu\nEnter menu number: '))
    if update_contact == 1: 
        default_contact()
        update_contact = input('Enter name to update: ')
        new_update = update_contact.replace(' ','')
        while new_update.lower() in list_contact.keys():
            pilih_update = int(input('=====UPDATE CONTACT INFORMATION===== \nWhat would you like to update? :\n1. Nama\n2. No.Id\n3. Sektor\n4. Alamat\n5. Phone\n6. Back to Main Menu\nEnter number: '))
            if pilih_update == 1:    
                update_name = input('Enter new name: ')
                new_name_update = update_name.replace(' ','')
                while new_name_update.lower() in list_contact.keys():
                    print('Name already exist')
                    update_name = input('Enter new name: ')
                    new_name_update = update_name.replace(' ','')
                check1= input('Are you sure want update? Yes/No: ')
                if check1 != 'Yes':
                    break
                else:
                    list_contact[new_name_update] = list_contact[new_update.lower()]
                    del list_contact[new_update.lower()]
                    list_contact[new_name_update]['Nama'] = update_name
                    default_contact()
                    print('Name updated')
                    break
            elif pilih_update == 2:
                new_noid_update = input('Enter new id number: ')
                check2= input('Are you sure want update? Yes/No: ')
                if check2 != 'Yes':
                    break
                else:
                    list_contact[new_update.lower()]['No.Id'] = new_noid_update
                    default_contact()
                    print('No.Id updated')
                    break
            elif pilih_update == 3:
                new_sector_update = input('Enter new sector: ')
                check3= input('Are you sure want update? Yes/No: ')
                if check3 != 'Yes':
                    break
                else:
                    list_contact[new_update.lower()]['Sektor'] = new_sector_update
                    default_contact()
                    print('Sector updated')
                    break
            elif pilih_update == 4:
                new_address_update = input('Enter new address: ')
                check4= input('Are you sure want update? Yes/No: ')
                if check4 != 'Yes':
                    break
                else:
                    list_contact[new_update.lower()]['Alamat'] = new_address_update
                    default_contact()
                    print('Address updated')
                    break   
            elif pilih_update == 5:
                new_phone_update = input('Enter new id number: ')
                check5= input('Are you sure want update? Yes/No: ')
                if check5 != 'Yes':
                    break
                else:
                    list_contact[new_update.lower()]['Phone'] = new_phone_update
                    default_contact()
                    print('Phone updated')
                    break
            else:
                break
        else:
            print('Contact name doesnt exist')
     
def delete_contact():
    default_contact()
    delete_contact = input('Enter contact name you want to delete: ')
    new_delete_contact = delete_contact.replace(' ','')
    while new_delete_contact.lower() not in list_contact.keys():
        print('Contact not Found')
        break
    else:
        check6 = input(f'Are you sure want to delete {delete_contact} ? Yes/No: ')
        while check6 != 'Yes':
            print('Contact not deleted')
            break
        else:
            del list_contact[new_delete_contact.lower()]
            default_contact()
            print('Contact deleted')



while True:
    pilih_menu = int(input('''
    MAIN MENU:
    1. View contacts
    2. Add a contact
    3. Update contact
    4. Delete contact
    0. Exit program
    
    Please enter menu number: '''))

    if pilih_menu == 1:
        view_contact()
    elif pilih_menu == 2:
        add_contact()
    elif pilih_menu == 3:
        update_contact()
    elif pilih_menu == 4:
        delete_contact()
    elif pilih_menu == 0:
        quit()
    else:
        print('Menu not Found')

        
