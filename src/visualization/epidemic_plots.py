import matplotlib.pyplot as plt

def plot_behavior_comparison(results_list):
    plt.figure(figsize=(10, 6))
    for res in results_list:
        plt.plot(res['t'], res['I'], label=f"eta = {res['eta']}")
    plt.title("Efekti i Sjelljes Kolektive (eta)")
    plt.legend()
    plt.grid(True, alpha=0.3)
