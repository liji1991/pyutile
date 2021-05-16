import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import sys
from IPython import display
#%matplotlib inline
# sys.path.append(r'D:\CodeField\Python\pyutile')
display.set_matplotlib_formats('svg')
plt.rcParams['figure.figsize'] = (10, 10)
plt.rcParams['font.sans-serif'] = ['SimHei'] # 步骤一（替换sans-serif字体）
plt.rcParams['axes.unicode_minus'] = False   # 步骤二（解决坐标轴负数的负号显示问题）
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

pyutile = sys.modules[__name__]


