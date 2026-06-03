import numpy as np
from scipy.integrate import solve_ivp

from src.models.seirv import seirv_model
from src.analysis.metrics import get_peak_data
from src.visualization.epidemic_plots import plot_behavior_comparison

def main():
    N = 1000000
    beta0 = 0.5
    sigma = 1/5.0
    gamma = 1/10.0
    nu = 0.001
    
    y0 = [N-10, 0, 10, 0, 0]
    t_span = (0, 160)
    t_eval = np.linspace(0, 160, 1000)
    
    eta_values = [0.0, 0.4, 0.8, 1.2]
    all_results = []
    
    print(f"\n{'Eta':<10} | {'Peak I':<10} | {'Day':<8}")
    print("-" * 30)
    
    for e in eta_values:
        sol = solve_ivp(seirv_model, t_span, y0, args=(N, beta0, e, sigma, gamma, nu), t_eval=t_eval)
        
        metrics = get_peak_data(sol)
        print(f"{e:<10} | {int(metrics['peak']):<10} | {metrics['day']:<8.1f}")
        
        all_results.append({
            't': sol.t,
            'I': sol.y[2],
            'eta': e
        })
        
    plot_behavior_comparison(
        all_results, 
        title="Efekti i Sjelljes Kolektive (eta)", 
        save_path="results/figures/behavior_comparison.png"
    )

if __name__ == "__main__":
    main()