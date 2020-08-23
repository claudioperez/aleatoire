# My functions
import solrel
import solrel.systems as systems
from solrel.systems import Event
from ema.utilities.numerical import iHLRF

# Define limit state functions
def g_x1(x): return 0.0
def g_x2(x): return 0.0


grad_x1 = lambda x: np.squeeze(grad(g_x1)(x))
grad_x2 = lambda x: np.squeeze(grad(g_x2)(x))


# Define events
E = {
    '1': Event('1', limit_func = g_x1, limit_grad = grad_x1),
    '2': Event('2', limit_func = g_x2, limit_grad = grad_x2),
#     '4': Event('4', limit_func = g_x4, limit_grad = grad_x4),
#     '5': Event('5', limit_func = g_x5, limit_grad = grad_x5),
};


