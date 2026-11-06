def run_simulation(initial: tuple, schedule, params) -> dict:
    """Run one simulation until the culture is mostly resistant (proposed threshold: 90% of cells are resistant).

    Steps through growth until resistant cells make up at least
    params.resistant_threshold (default 0.9) of the living culture. Stops
    early if the culture goes extinct (no cells remain), or at params.max_steps.

    Args:
        initial: Starting state as (starting population, initial resistant
            fraction).
        schedule: DosingSchedule giving the dose at each step.
        params: SimulationParams (resistant_threshold, max_steps, and the
            growth and mutation settings).

    Returns:
        Dict with the per-step history, the step at which the threshold was
        reached (None if it never was), and the stop reason: "threshold",
        "extinct", or "max_steps".
    """
pass
