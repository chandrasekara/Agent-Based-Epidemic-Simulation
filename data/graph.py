from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
import pandas as pd

def display_results(results_file):
    df = pd.read_csv(results_file)
    
    df['Infected'].plot()
    
    plt.show()


