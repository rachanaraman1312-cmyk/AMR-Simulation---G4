import random

def run_replicates(n: int, schedule: DosingSchedule,params: SimulationParams, antibiotic: Antibiotic) -> list:
    """Run run_simulation n times, each independent of the others.

    Every run builds its own starting colony from params and gets its own
    random seed, so runs differ and none can affect another. Runs stop at
    different steps, because each ends when resistant cells reach the
    threshold, the culture goes extinct, or max_steps is hit.

    Args:
        n: Number of independent runs.
        schedule: DosingSchedule giving the dose at each step.
        params: SimulationParams (starting colony size, threshold,
            max_steps, and growth and mutation settings).
        antibiotic: Antibiotic properties.

    Returns:
        List of n result objects, one per run.
    """

pass
