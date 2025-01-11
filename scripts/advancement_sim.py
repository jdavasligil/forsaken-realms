"""Advancement Simulator

This script simulates player character advancement from levels 1 through 10
in order to obtain the distribution of MAW save scores expected.
"""

import matplotlib.pyplot as plt
import numpy as np

from scipy.stats import qmc


# Returns a vector of level 1 character attribute scores (3d6 drop lowest).
def sample_attributes(sampler, pow2=3):
    sample = 1.0 + np.floor(6.0 * sampler.random(n=1 << pow2))
    return np.sum(sample, axis=1) - np.amin(sample, axis=1)


def roll_to_advance(sampler, attr_sample, pow2=3, levels=1):
    for i in range(levels):
        rolls = 1.0 + np.floor(20 * sampler.random(n=1 << pow2))
        is_higher = rolls.flatten() > attr_sample
        attr_sample += is_higher.astype(np.float32)
    attr_sample = np.minimum(attr_sample, ATTR_MAX)
    return attr_sample


SAMPLE_POW2 = 18

ATTR_MAX = np.ones(1 << SAMPLE_POW2) * 18

attribute_sampler = qmc.Sobol(d=3)
rng_sampler = qmc.Sobol(d=1)

# List of samples of attributes having advanced i levels, in ascending order.
attribute_samples = [
        roll_to_advance(
            rng_sampler,
            sample_attributes(attribute_sampler, SAMPLE_POW2),
            SAMPLE_POW2,
            i
        )
        for i in range(10)]


labels = [f'Level {i + 1}' for i in range(10)]
bins = [2 + i for i in range(17)]
plt.hist(attribute_samples, bins=bins, label=labels, density=True)
plt.legend(loc='upper right')

plt.show()
