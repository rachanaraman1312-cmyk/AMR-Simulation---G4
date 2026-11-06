import random
def mutation_uptake(dividing_cells: list, params: SimulationParams,
                    time_hours: float) -> int:
    """Let dividing cells gain resistance.

    Each dividing cell independently draws against its own mutation probability, using random.random(). 
    The probability is raised for cells with an inherent mutation, for stronger mutations. 
    Cells that succeed have their resistance and Mutation updated in place.

    Args:
        dividing_cells: Cells that divided this step.
        params: SimulationParams (mutation boosts, early-phase window).
        time_hours: Elapsed time, used for the early-phase check.

    Returns:
        Number of cells that gained a mutation this step.
    """

    return random.binomialvariate(dividing_sensitive, mutation_prob)
