import os

src_file_path = 'C:\\Users\\Vince\\Desktop\\temp_tf\\'
dst_file_path = 'C:\\Users\\Vince\\Desktop\\temp_tf2\\'
file = open("raw_taxFilings.txt")
content = file.readlines()

d = {}

for i in range(4,len(content),7):
    str = "taxFilings_Tf_"+ content[i-2].strip()+"_"+content[i+1].strip()+"_"+content[i].strip()
    #str = "taxFilings_Tf_"+[location]+"_"+[date]+"_"+[ref_id]
    (key, val) = (content[i].strip() , str)
    d[key] = val

k =  'desktop'
d[k] = 'null'


    

for x in os.listdir(src_file_path):
    p = x.strip()
    size = len(p)
    key = p[:size - 4]
    new_fileName = d.get(key)
    old_file_path = src_file_path + p
    new_file_path = dst_file_path + new_fileName+'.pdf'
    os.rename(old_file_path, new_file_path)






    
