import pandas as pd
from matplotlib import pyplot as plt

def graf_a(graf):
    pl=pd.read_json(graf)
    pl.plot()
    return plt.show()
graf_a(graf="grupoa.json")