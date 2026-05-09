import matplotlib.pyplot as plt
import os
import numpy as np

def plot_seirv_curves(sol, N, title="Dinamika e Modelit SEIRV", save_path=None):
    """
    Ndërton grafikun për të gjitha kategoritë (S, E, I, R, V).
    """
    plt.figure(figsize=(12, 7))
    
    t = sol.t
    
    plt.plot(t, sol.y[0], label='S (Të ndjeshmit)', color='#1f77b4', linewidth=2)
    plt.plot(t, sol.y[1], label='E (Të ekspozuarit)', color='#ff7f0e', linewidth=2)
    plt.plot(t, sol.y[2], label='I (Të infektuarit)', color='#d62728', linewidth=2.5)
    plt.plot(t, sol.y[3], label='R (Të shëruarit)', color='#2ca02c', linewidth=2)
    plt.plot(t, sol.y[4], label='V (Të vaksinuarit)', color='#9467bd', linewidth=2)
    
    plt.title(title, fontsize=14, fontweight='bold')
    plt.xlabel('Ditët', fontsize=12)
    plt.ylabel('Numri i Popullatës', fontsize=12)
    plt.legend(loc='upper right', frameon=True, shadow=True)
    plt.grid(True, linestyle='--', alpha=0.6)
    
    if save_path:
        folder = os.path.dirname(save_path)
        if folder and not os.path.exists(folder):
            os.makedirs(folder)
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Grafiku u ruajt në: {save_path}")
    
    plt.show()

def plot_behavior_comparison(results_list, title="Ndikimi i Sjelljes Kolektive (eta) në Infektim", save_path=None):
    """
    Krahason vetëm kurbën e të infektuarve (I) për vlera të ndryshme të eta.
    results_list duhet të jetë një listë me tregues: {'t': koha, 'I': infektuarit, 'eta': vlera}
    """
    plt.figure(figsize=(12, 7))
    
    for res in results_list:
        plt.plot(res['t'], res['I'], label=f'eta = {res["eta"]}', linewidth=2)
    
    plt.title(title, fontsize=14, fontweight='bold')
    plt.xlabel('Ditët', fontsize=12)
    plt.ylabel('Numri i të infektuarve (I)', fontsize=12)
    plt.legend(title="Parametri i sjelljes", loc='upper right')
    plt.grid(True, linestyle='--', alpha=0.6)
    
    if save_path:
        folder = os.path.dirname(save_path)
        if folder and not os.path.exists(folder):
            os.makedirs(folder)
        plt.savefig(save_path, dpi=300, bbox_inches='tight')
        print(f"Grafiku i krahasimit u ruajt në: {save_path}")
    
    plt.show()
