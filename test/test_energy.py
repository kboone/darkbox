from darkbox import energy

from numpy.testing import assert_equal

def test_energy():
    assert_equal(energy.abs_area([1, 2, 3]), 6)
