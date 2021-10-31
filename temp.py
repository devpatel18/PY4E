import pandas as pd
from pandasgui import show

pokemon = pd.read_csv("pokemon.csv")
gui = show(pokemon)
