import numpy as np
from scipy.integrate import solve_ivp

from src.models.seirv import seirv_model
from src.visualization.epidemic_plots import plot_seirv_curves

def main():
    N = 1000000
    beta0 = 0.5
    eta = 0.8
    sigma = 1/5.0
    gamma = 1/10.0
    nu = 0.001
    
    y0 = [N-10, 0, 10, 0, 0]
    t_span = (0, 160)
    t_eval = np.linspace(0, 160, 1000)
    
    print("Po ekzekutohet simulimi bazë (eta = 0.8)...")
    sol = solve_ivp(seirv_model, t_span, y0, args=(N, beta0, eta, sigma, gamma, nu), t_eval=t_eval)
    
    plot_seirv_curves(
        sol, 
        N, 
        title="Dinamika e Modelit SEIRV (eta = 0.8)", 
        save_path="results/figures/default_simulation.png"
    )

if __name__ == "__main__":
    main()