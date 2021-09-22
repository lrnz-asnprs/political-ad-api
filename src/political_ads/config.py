from pathlib import Path
import numpy as np
import pandas as pd

data_dir_raw = Path('..\data')

data_sample = pd.read_csv(data_dir_raw / 'sample.csv') # global variable that can be used in jupyter notebooks 