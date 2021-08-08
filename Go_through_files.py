#利用OS套件的os.walk抓取檔名裡面包含filters定義的字串，並加入inFileNames這個list
import os
#====input path===
dir_path=r'P:\PETE\Sam\10nS_Die66\10nS_Write_probability\1003_Die66_BA4_Wr1_80WLs_3Kloops_13VBLs\WL032_to_047\2999 vs 1'
#========
inFileNames=[]
filters=['.xlsx']
for alldir in [x[0] for x in os.walk(dir_path)]: # x[0] for all subdirectories
    files = os.listdir(alldir)
    for name in files:
        add = True
        for f in filters:
            if (not f in name):
                add = False
                continue
        if (add):  
            inFileNames.append(os.path.join(alldir, name))
