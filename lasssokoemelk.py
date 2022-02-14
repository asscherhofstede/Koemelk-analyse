from pyspectra.readers.read_spc import read_spc_dir
import matplotlib.pyplot as plt

df_spc, dict_spc=read_spc_dir('Spectra')
df_spc.transpose()
f, ax =plt.subplots(1, figsize=(18,8))
ax.plot(df_spc.transpose())
plt.xlabel("nm")
plt.ylabel("Abs")
ax.legend(labels= list(df_spc.transpose().columns))
plt.show()