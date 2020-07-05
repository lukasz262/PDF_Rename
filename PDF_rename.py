'''change PDF names (delete first 6 symbols and delete 14 symbol)'''

import os

def FileRename(file, file_dir):
    try:
        if file.endswith('.pdf') and file.startswith('D_PDF_'):
            new_file_name = file[6:14] + file[15:]
            os.rename(r'{}\{}'.format(file_dir, file),
                      r'{}\{}'.format(file_dir, new_file_name))
    except FileExistsError:
        print('Nie można zmienić nazwy pliku {}, ponieważ istnieje już '
              'plik o nowej nazwie w określonej lokalizacji.'.format(file))

file_dir = r'D:\PDF'
if file_dir[0].lower() == 'c':
    print('Wybierz inną lokalizację niż C:')
else:
    file_list = os.listdir(file_dir)
    for file in file_list:
        FileRename(file, file_dir)
input('Naciśnij ENTER, aby zakończyć')