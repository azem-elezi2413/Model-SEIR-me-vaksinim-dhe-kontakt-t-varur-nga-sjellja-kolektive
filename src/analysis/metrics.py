import numpy as np

def calculate_peak(sol):
    peak_val = np.max(sol.y[2])
    peak_day = sol.t[np.argmax(sol.y[2])]
    return peak_val, peak_day
