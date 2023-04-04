import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 388568881 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    
    alpha = 1 - p
    loc = x.mean()
    scale = np.sqrt(np.var(x)) / np.sqrt(len(x))
    return 2*loc + 2*scale * norm.ppf(1 - alpha / 2), \
           2*loc + 2*scale * norm.ppf(alpha / 2)
