def mamdani_norm(mu_A, mu_B):
    return min(mu_A, mu_B)


def sugeno_norm(mu_A, mu_B):
    return mu_A * mu_B
