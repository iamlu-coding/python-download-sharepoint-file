from sharepoint import SharePoint
import re
import sys

# 1 args = folder name
folder_name = sys.argv[1]
# 2 args = folder_dest
folder_dest = sys.argv[2]
# 3 args = file_name
file_name = sys.argv[3]
# 4 args = file_name_pattern
file_name_pattern = sys.argv[4]

def save_file(file_n, file_obj):
    file_dir_path = '\\'.join([folder_dest, file_n])
    with open(file_dir_path, 'wb') as f:
        f.write(file_obj)
        f.close()

def get_file(file_n, folder):
    file_obj = SharePoint().download_file(file_n, folder)
    save_file(file_n, file_obj)

def get_files(folder):
    files_list = SharePoint().download_files(folder)
    for file in files_list:
        get_file(file['Name'], folder)

def get_files_by_pattern(pattern, folder):
    files_list = SharePoint().download_files(folder)
    for file in files_list:
        if re.search(pattern, file['Name']):
            get_file(file['Name'], folder)

if __name__ == '__main__':
    if file_name != 'None':
        get_file(file_name, folder_name)
    elif file_name_pattern != 'None':
        get_files_by_pattern(file_name_pattern, folder_name)
    else:
        get_files(folder_name)