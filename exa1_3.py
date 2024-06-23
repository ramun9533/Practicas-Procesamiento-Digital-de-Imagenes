import numpy as np
import scipy.stats as stats

# Datos
x = np.array([39, 43, 21, 64, 57, 43, 38, 75, 34, 52])
y = np.array([65, 75, 52, 82, 92, 80, 73, 98, 56, 75])

# Cálculo de la pendiente y el intercepto
beta_1, beta_0 = np.polyfit(x, y, 1)

# Predicciones
y_pred = beta_0 + beta_1 * x

# Error estándar
S_e2 = np.sum((y - y_pred)**2) / (len(x) - 2)
s_beta_1 = np.sqrt(S_e2 / np.sum((x - np.mean(x))**2))

# Prueba de hipótesis
t_stat = beta_1 / s_beta_1
p_value = 2 * (1 - stats.t.cdf(abs(t_stat), df=len(x) - 2))

beta_1, beta_0, t_stat, p_value

