def run_replicates(n: int, initial: tuple, schedule, params):

"""Run run_simulation n times, each independent of the others.

    Every run starts from the same initial state and uses its own random
    draws, so results differ between runs. Runs stop at different steps
    because each ends when the culture is at least 90% resistant (or goes
    extinct, or hits max_steps).

    Args:
        n: Number of independent runs.
        initial: Starting state as (starting population, initial resistant
            fraction). Not modified by the runs.
        schedule: DosingSchedule giving the dose at each step.
        params: SimulationParams (simulation settings).

    Returns:
        List of n run_simulation results, one per run, with differing
        lengths.
    """
pass

