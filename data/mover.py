import os
import shutil

# source_folder = r"mypredictions\test\\"
# destination_folder = r"mypredictions\test\\"
#
# source_folder = r"mypredictions\train\\"
# destination_folder = r"mypredictions\train\\"
#
source_folder = r"perfectly_detected_ears\train\\"
destination_folder = r"perfectly_detected_ears\train\\"
#
# source_folder = r"perfectly_detected_ears\test\\"
# destination_folder = r"perfectly_detected_ears\test\\"

# fetch all files
for file_name in os.listdir(source_folder):
    # construct full file path
    source = source_folder + file_name
    os.makedirs(destination_folder + file_name[:4], exist_ok=True)
    destination = destination_folder + file_name[:4]+'\\'+file_name

    # move only files
    if os.path.isfile(source):
        shutil.move(source, destination)
        print('Moved:', file_name)