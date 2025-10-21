import os
# =========================== File  manager ==================================
def create_file():
    user = input('\n Write name  of file to create:')
    if os.path.exists(user):
        print('File already exists')

    elif not os.path.exists(user):
        with open(user,'w') as f:
            f.write('File create automatically.\n')
        print('File not found.Created automatically')    
    else:
        print('Unknown error.')

def add_str():
    user = input('\n Write name of file:')
    if os.path.exists(user):
        text = input('write text to add:')
        print('file with this name already have')
        with open(user,'a') as f:
            f.write(text)
            print('New line add successfully.')
    elif not os.path.exists(user):
        print('File  not found.')  
    else:
        print('Unknown error')


def clean_file():
    user = input('\n Write name file:')
    if os.path.exists(user):
        with open(user,'w') as f:
            pass
        print('file cleaned successfully')
    elif not os.path.exists(user):
        print('Unknown error')                  
    else:
        print('Unknown error')

def remove_file():
    user = input('\n Write name file:')
    if os.path.exists(user):
        os.remove(user)

    else:
        print('Unknown error')    


def file_text():
    user = input('Write name file:')
    if os.path.exists(user):
        with open(user,'r') as f:
            print(f.readlines())

def main():
    while True:
        print('\n ==========================')
        print('File Manager - Dzezhyts Yauheni')
        print('=============================')
        print('1 - Create file')
        print('2 - Add new line')
        print('3 - Clean file')
        print('4 - Delete file')
        print('5 - Show file content')
        print('6 - Exit')
        print('=============================')
        choice = input('Write number your choice:')
        if choice == '1':
            create_file()
        elif choice == '2':
            add_str()
        elif choice == '3':
            clean_file()
        elif choice == '4':
            remove_file()
        elif choice == '5':
            file_text() 
        elif choice == '6':
            print('Exit')
            break                               
        else:
            print('Error')
if __name__ == '__main__':
    main()    