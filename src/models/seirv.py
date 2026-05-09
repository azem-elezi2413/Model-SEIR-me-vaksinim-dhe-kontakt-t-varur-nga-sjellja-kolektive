import numpy as np

def seriv_model(t, y, N, beta0, eta, sigma, gamma, nu):
    """
    Implementimi i sisetmit SEIRV me kontakt te varur nga sjellja.

    Parametrat:
    t         : koha (e nevojshme per solver-in e librarise scipy)
    y         : lista e variablave [S, E, I, R, V]
    N         : popullata totale
    beta0     : shkalla baze e ekontaktit
    eta       : koeficienti i reagimit kolektir (sjellja)
    sigma     : shkalla e kalimit nga E ne I (1/periudha e inkubacionit)
    gamma     : shkalla e sherimit (1/periudha infektive)
    nu        : shkalla e vaksinimit
    """
    S, E, I, R, V = y

    beta_eff = beta0 * ( 1 - eta * I / N)

    beta_eff = max(beta_eff, 0)

    dSdt = -beta_eff * S * I / N - nu * S
    dEdt = beta_eff * S * I / N - sigma * E
    dIdt = sigma * E - gamma * I
    dRdt = gamma * S
    dVdt = nu * S

    return [dSdt, dEdt, dIdt, dRdt, dVdt]
