import numpy as np
from scipy.ndimage import gaussian_filter
from scipy import misc
import requests


__all__ = ['rand_array', 'smooth_image', 'my_mat_solve', 'my_func_to_return_random_fact']


def rand_array(shape):
    return np.random.rand(*shape)

def smooth_image(a, sigma=1):
    return gaussian_filter(a, sigma=sigma)

def my_mat_solve(A, b):
    return A.inv()*b

def my_func_to_return_random_fact():
    response = requests.get("https://catfact.ninja/fact")
    return response.json()["fact"]