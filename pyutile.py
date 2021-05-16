import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import sys

pyutile = sys.modules[__name__]

def init():
    plt.rcParams['font.sans-serif'] = ['SimHei'] # 步骤一（替换sans-serif字体）
    plt.rcParams['axes.unicode_minus'] = False   # 步骤二（解决坐标轴负数的负号显示问题）
    print("done")