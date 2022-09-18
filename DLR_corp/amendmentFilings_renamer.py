import os
from pathlib import Path

src_file_path = 'C:\\Users\\Vince\\Desktop\\temp_af\\'
dst_file_path = 'C:\\Users\\Vince\\Desktop\\temp_af2\\'
file = open("ref_af_bd.txt")
content = file.readlines()
file2 = open("raw_amendmentFiling.txt")
raw_content_spaced = file2.readlines()
raw_content = []

for y in raw_content_spaced:
    raw_content.append(y.strip())


file_list = sorted(Path('C:\\Users\\Vince\\Desktop\\temp_af').iterdir(), key=os.path.getmtime)

for (r,n) in zip(content , file_list):
    i = raw_content.index(r.strip())
    str_name = "amendmentFilings_Af_"+ raw_content[i-2].strip()+"_"+raw_content[i+1].strip()+"_"+raw_content[i].strip()
    #str_name = "Amendment Validation Recap Report_Af_"+ raw_content[i-2].strip()+"_"+raw_content[i+1].strip()+"_"+raw_content[i].strip() #doc 2
    #str_name = "amendmentFilings_Af_"+[location]+"_"+[date]+"_"+[ref_id]
    new_file_path = dst_file_path + str_name+'.xlsx'
    os.rename(n, new_file_path)
    


    