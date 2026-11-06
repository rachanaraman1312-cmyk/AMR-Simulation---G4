def get_dose(step: int, schedule: DosingSchedule) -> float:
    """Return the antibiotic dose for the current step.

    Called once per step by run_simulation, and the result is passed to
    growth_step. Returns 0.0 if no dose is due.

    Args:
        step: Current simulation step.
        schedule: DosingSchedule holding the dose settings.

    Returns:
        Dose for this step as a float, in the same units as the MIC.
    """

pass
