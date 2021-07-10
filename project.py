from sharepoint import SharePoint

# set file name
file_name = 'sample.pdf'

# set the folder name
folder_name = '2020'

# get file
file  = SharePoint().download_file(file_name, folder_name)

# save file
with open(file_name, 'wb') as f:
    f.write(file)
    f.close()
