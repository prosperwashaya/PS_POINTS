import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

a=sns.load_dataset("rail_pspoints2")
sns.replot(x="time", y="point", data =a, kind="line")