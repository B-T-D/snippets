
def random_sequence(length, seed):
    """Returns a list of Park-Miller pseudorandom numbers.

    Args:
        length (int): Number of pseudorandom numbers to generate
        seed (int): The initial seed

    Returns:
        (list): List of Park-Miller pseudorandom numbers containing
        the specified number of elements, in the interval [0, 1).
    """

    r = seed
    m = 2 ** 31 - 1
    a = 16807
    rand_list = []
    for index in range(length):
        r = lehmer(r, m, a)
        rand_list.append(r / m)
    return rand_list

def lehmer(r, m, a):
    """Computes the next pseudorandom number using a Lehmer PRNG.

    Args:
        r (int): Seed or previous pseudorandom number
        m (int): A prime number
        a (int): An integer between 1 and m - 1

    Returns:
        (int): Next pseudorandom number in the sequence.
    """

    return (a * r) % m


list = random_sequence(100, 3)
print(list)
