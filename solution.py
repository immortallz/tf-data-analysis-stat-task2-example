import pandas as pd
import numpy as np

from scipy.stats import norm
from scipy.stats import beta

chat_id = 388568881 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    
    alpha = 1 - p
    loc = x.mean()
    max_x = max(x)
    n = len(x)
    return (max_x - 0.038)/(1 - beta.ppf(alpha/2, 1, n)) + 0.038, \
           (max_x - 0.038)/(1 - beta.ppf(1 - alpha/2, 1, n)) + 0.038
