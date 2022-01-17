import os
import shutil
import csv

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

# with open('perfectly_detected_ears/annotations/recognition/testAnotation.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter =',')
#     line_count = 0
#     for row in csv_reader:
#         print(row)
#         if(os.path.isdir('perfect_test\\'+row[1]) == False):
#             os.makedirs('perfect_test\\'+row[1], 0o777)
#         mapa = row[0].split('/')[1][:4]
#         for file_name in os.listdir('perfectly_detected_ears/test/'+mapa):
#             shutil.copy('perfectly_detected_ears/test/'+mapa+'/'+file_name, 'perfect_test\\'+row[1])

with open('perfectly_detected_ears/annotations/recognition/trainAnotation.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter =',')
    line_count = 0
    for row in csv_reader:
        print(row)
        if(os.path.isdir('my_train\\'+row[1]) == False):
            os.makedirs('my_train\\'+row[1], 0o777)
        mapa = row[0].split('/')[1][:4]
        if(os.path.isdir('mypredictions/train/'+mapa)):
            for file_name in os.listdir('mypredictions/train/'+mapa):
                shutil.copy('mypredictions/train/'+mapa+'/'+file_name, 'my_train\\'+row[1])
