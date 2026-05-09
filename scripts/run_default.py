import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.models.seirv import seirv_model

def run_simulation():
    N = 1000000
    beta0 = 0.5
    eta = 0.8
    sigma = 1/5.0
    gamma = 1/10.0
    nu = 0.001

    I0 = 10
    E0 = 0
    R0 = 0
    V0 = 0
    S0 = N - I0 - E0 - R0 - V0
    y0 = [S0, E0, I0, R0, V0]

    t_span = (0, 160)
    t_eval = np.linspace(0, 160, 1000)

    sol = solve_ivp(
        seirv_model, 
        t_span, 
        y0, 
        args=(N, beta0, eta, sigma, gamma, nu), 
        t_eval=t_eval,
        method='RK45'
    )

    total_pop = sol.y[0] + sol.y[1] + sol.y[2] + sol.y[3] + sol.y[4]
    pop_error = np.max(np.abs(total_pop - N))
    print(f"Gabimi maksimal në ruajtjen e popullatës: {pop_error:.2e}")

    plt.figure(figsize=(10, 6))
    plt.plot(sol.t, sol.y[0], label='Susceptible (S)')
    plt.plot(sol.t, sol.y[1], label='Exposed (E)')
    plt.plot(sol.t, sol.y[2], label='Infectious (I)', linewidth=2)
    plt.plot(sol.t, sol.y[3], label='Recovered (R)')
    plt.plot(sol.t, sol.y[4], label='Vaccinated (V)')
    
    plt.title(f"Evolucioni SEIRV (eta={eta}, nu={nu})")
    plt.xlabel("Ditët")
    plt.ylabel("Numri i individëve")
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    os.makedirs('results/figures', exist_ok=True)
    plt.savefig('results/figures/default_simulation.png')
    plt.show()

if __name__ == "__main__":
    run_simulation()
