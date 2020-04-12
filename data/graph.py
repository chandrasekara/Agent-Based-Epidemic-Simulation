from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
import pandas as pd

def display_results(results_file):
    df = pd.read_csv(results_file)
     
    df.drop(['Time'], axis=1, inplace=True)

    ax = df.plot()

    ax.set_xlabel('Time')

    ax.set_ylabel('Number Infected/Recovered')
    
    plt.show()


