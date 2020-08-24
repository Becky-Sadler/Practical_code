def cube(x):
    return x**3


def test_when_input_is_3():
	x = cube(3)
	assert x == 27
