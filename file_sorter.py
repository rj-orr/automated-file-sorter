import os, shutil

target_folder = os.path.dirname(os.path.abspath(__file__))
script_name = os.path.basename(__file__)

extensions = {item.split('.')[-1] for item in os.listdir(target_folder) if os.path.isfile(os.path.join(target_folder, item)) and item != script_name}

# create folders
for extension in extensions:
    if not os.path.exists(os.path.join(target_folder, extension)):
        os.mkdir(os.path.join(target_folder, extension))

# move files
for item in os.listdir(target_folder):
    if os.path.isfile(os.path.join(target_folder, item)) and item != script_name:
        file_extension = item.split('.')[-1]
        
        src = os.path.join(target_folder, item)
        dest = os.path.join(target_folder, file_extension, item)
        
        if not os.path.exists(dest):
            shutil.move(src, dest)
