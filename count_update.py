import random
def count_update(n_sensitive: int, n_resistant: int, death_probs: tuple, divide_probs: tuple) -> dict:
    """Draw how many sensitive and resistant cells die and divide this step.

    Use random.binomialvariate for each group.

    Args:
        n_sensitive: Current number of sensitive cells.
        n_resistant: Current number of resistant cells.
        death_probs: (sensitive, resistant) probability of dying this step,
            set by the current dose.
        divide_probs: (sensitive, resistant) probability of dividing this
            step.

    Returns:
        Dict with the number of sensitive and resistant cells that died and
        that divided. The sensitive-divided count is passed to
        mutation_uptake.
    """


pass
