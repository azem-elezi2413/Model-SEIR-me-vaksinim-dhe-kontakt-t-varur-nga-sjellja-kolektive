import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.models.seirv import seirv_model

def scan_behavior():
    # Parametrat fiks
    N = 1000000
    beta0 = 0.5
    sigma = 1/5.0
    gamma = 1/10.0
    nu = 0.0005
    
    t_span = (0, 200)
    t_eval = np.linspace(0, 200, 1000)
    y0 = [N-10, 0, 10, 0, 0]

    eta_values = [0.0, 0.4, 0.8, 1.2]
    
    plt.figure(figsize=(10, 6))

    print(f"{'Eta':<10} | {'Kulmi (I max)':<15} | {'Dita e kulmit':<15}")
    print("-" * 45)

    for eta in eta_values:
        sol = solve_ivp(
            seirv_model, 
            t_span, 
            y0, 
            args=(N, beta0, eta, sigma, gamma, nu), 
            t_eval=t_eval
        )
        
        i_curve = sol.y[2]
        peak_idx = np.argmax(i_curve)
        peak_val = i_curve[peak_idx]
        peak_time = sol.t[peak_idx]

        print(f"{eta:<10} | {int(peak_val):<15} | {peak_time:<15.1f}")

        plt.plot(sol.t, sol.y[2], label=f'eta = {eta}')

    plt.title("Ndikimi i Sjelljes Kolektive (eta) në Kulmin Epidemik")
    plt.xlabel("Ditët")
    plt.ylabel("Numri i te infektuarve (I)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    os.makedirs('results/figures', exist_ok=True)
    plt.savefig('results/figures/scan_behavior_eta.png')
    plt.show()

if __name__ == "__main__":
    scan_behavior()
