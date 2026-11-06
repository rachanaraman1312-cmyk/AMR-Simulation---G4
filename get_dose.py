def get_dose(step: int, schedule: DosingSchedule) -> float:
     """Return the antibiotic dose for the current step.

    Called once per step by run_simulation, and the result is passed to growth_step. 
    The dose is initial_dose * (1 + pct_increase / 100) ** step, capped at schedule.max_dose if one is set.

    Args:
        step: Current simulation step (0 for the first).
        schedule: DosingSchedule holding the starting dose and percentage
            increase.

    Returns:
        Dose for this step as a float, in the same units as the MIC.
    """
pass
