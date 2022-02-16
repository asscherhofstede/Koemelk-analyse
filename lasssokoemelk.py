import spc
import pandas as pd
import numpy as np
import os

df = []
listdir = os.listdir('Spectra')
for s in listdir:
    path = os.path.join("D:\\ai_semesterwindesheim\\koemelk\\Spectra", s)
    
    f = spc.File(path)  # read file
    file = f.data_txt()  # output data
    df_in_one_go=pd.DataFrame(np.array([f.sub[0].y,f.sub[1].y,f.sub[2].y]),columns=f.x)
    df_in_one_go['samplename'] = s
    df.append(df_in_one_go)
df = pd.concat(df)
print(df)


    # print(df_in_one_go)
    # df = df_in_one_go.concat([df_in_one_go, df_in_one_go], axis=1)
    # df = pd.concat()



  


# f = spc.File('Spectra/f.spc')  # read file

# file = f.data_txt()  # output data
# df_in_one_go=pd.DataFrame(np.array([f.sub[0].y,f.sub[1].y,f.sub[2].y]),columns=f.x)
# print(df_in_one_go)

#gemiddelde per sample
