import spc
import pandas as pd
import numpy as np

f = spc.File('Spectra/Sample 1.spc')  # read file

file = f.data_txt()  # output data
df_in_one_go=pd.DataFrame(np.array([f.sub[0].y,f.sub[1].y,f.sub[2].y]),columns=f.x)
print(df_in_one_go)