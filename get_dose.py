def get_dose(step: int, schedule: DosingSchedule):
   """Return the antibiotic dose for the current step.

    Called once at every step of run_simulation, and the result is passed on to growth_step. 
    Looks the step up in the dosing schedule and returns 0.0 if no dose is due.

    Args:
        step: Current simulation step.
        schedule: DosingSchedule instance holding the type and
            characteristics of each dose (amount and timing).

    Returns:
        Dose for this step as a float, in the same units as the MIC.
    """

pass
