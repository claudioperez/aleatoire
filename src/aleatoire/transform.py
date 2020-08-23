import numpy as np

nataf_correlation = {
    'lognorm':{
        'lognorm': lambda rho,deli,delj: np.log(1+rho*deli*delj)/rho/np.sqrt(np.log(1+deli**2)*np.log(1+delj**2)),
        'gamma': lambda rho, delj, deli: 1.001 + 0.033*rho + 0.004*deli - 0.016*delj + 0.002*rho**2 + 0.223*deli**2 + 0.130*delj**2 + 0.029*delj*deli - 0.104*rho*deli - 0.119*rho*delj,
    },
    'gamma':{
        'lognorm': lambda rho,deli,delj: 1.001 + 0.033*rho + 0.004*deli - 0.016*delj + 0.002*rho**2 + 0.223*deli**2 + 0.130*delj**2 + 0.029*delj*deli - 0.104*rho*deli - 0.119*rho*delj,
    },
    'gumbel':{
        'gamma': lambda rho,deli,delj: 1.031 + 0.052*rho + 0.011*deli-0.210*delj + 0.002*rho**2 + 0.220*deli**2 + 0.350*delj**2 + 0.009*deli*delj+0.005*rho*deli-0.174*rho*delj
    }
}