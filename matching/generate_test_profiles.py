import pickle

import numpy as np

test_profiles = np.random.random_integers(low=0, high=100, size=(100, 8))

print test_profiles

pickle.dump(test_profiles, 'profiles.dat')
