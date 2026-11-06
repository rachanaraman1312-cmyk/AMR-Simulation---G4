import random
def mutation_uptake(dividing_cells: list, params: SimulationParams,
                    time_hours: float) -> int:
    """Let dividing cells without a mutation gain one.

    Only cells with no mutation draw (cell.mutation is None). 
    A cell that gains a mutation is locked into it and can never develop another.
    Each draw uses random.random() against the mutation's rate, raised during the early-phase window (params.early_phase_hours). 
    The mutation's strength is chosen once, at the moment it is gained.

    Args:
        dividing_cells: Cells that divided this step.
        params: SimulationParams (mutation rate, early-phase window).
        time_hours: Elapsed time, used for the early-phase check.

    Returns:
        Number of cells that gained a mutation this step.
    """
    return random.binomialvariate(dividing_sensitive, mutation_prob)
