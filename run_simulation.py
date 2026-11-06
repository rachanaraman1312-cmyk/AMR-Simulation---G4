def run_simulation(schedule: DosingSchedule, params: SimulationParams, antibiotic: Antibiotic) -> RunResult:
    """Run one simulation until the culture is mostly resistant.

    Builds a single starting colony, randomising inherent vs acquired
    mutation for each cell. Then, at every step: get the dose, call
    growth_step, and check the stop rule. Stops when resistant cells are at
    least params.threshold (0.9) of the living cells, when no cells are
    alive, or at params.max_steps.
    This max_step limit can be capped on the basis of population. 

    Args:
        schedule: DosingSchedule giving the dose at each step.
        params: SimulationParams.
        antibiotic: Antibiotic properties.

    Returns:
        RunResult with the per-step history (counts and cell positions),
        the outcome ("threshold", "extinct" or "max_steps"), and the step
        at which the threshold was reached (None if never).
    """
pass
