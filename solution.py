import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 388568881 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    
    alpha = 1 - p
    loc = (2*x - 0.038).mean()
    scale = np.sqrt(np.var(2*x - 0.038)) / np.sqrt(len(2*x - 0.038))
    return loc + scale * norm.ppf(1 - alpha / 2), \
           loc + scale * norm.ppf(alpha / 2)
