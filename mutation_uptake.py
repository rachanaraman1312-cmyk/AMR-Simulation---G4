import random
def mutation_uptake(mutation_prob: float, dividing_sensitive: float):
  """Determines how many dividing sensitive cells acquire resistance this step.

    Package to use: random.binomialvariate (Python 3.12+)

    Args:
        mutation_prob: Fixed per-division mutation probability for the
            antibiotic-organism pair, taken from the literature.
        dividing_sensitive: Number of sensitive cells that are present and can divide 

    Returns:
        Number of cells that switch from sensitive to resistant state.
    """
    return random.binomialvariate(dividing_sensitive, mutation_prob)
