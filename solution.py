import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 388568881 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    
    alpha = 1 - p
    loc = x.mean()
    return (loc - 0.038)/(1 - alpha / 2) + 0.038, \
           (loc - 0.038)/(alpha / 2) + 0.038
