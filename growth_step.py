def growth_step(cells: list, dose: float, params: SimulationParams, antibiotic: Antibiotic, first_dose: bool) -> list:
    """Run one growth step: death, then division.

    Death, applied to each living cell if dose > 0:
        - Not resistant (0): dies.
        - Moderately resistant (0.5): dies if dose exceeds
          antibiotic.high_dose_threshold.
        - Resistant (1): survives.
        - On the first dose, a random 5-10% of the colony
          (params.survivor_fraction) survives regardless of resistance.
        - Dead cells stay dead.

    Division, for each surviving cell:
        - A single cell divides, and two cells of the same type divide.
        - A cell needs at least 1 px of free space, otherwise it cannot
          divide.
        - The child is placed in a free neighbouring pixel and inherits the
          parent's mutation with a raised probability
          (params.inheritance_boost).

    Then calls count_update and mutation_uptake.

    Args:
        cells: List of Cell objects; modified in place.
        dose: Antibiotic dose for this step.
        params: SimulationParams (survivor fraction, inheritance boost,
            grid size).
        antibiotic: Antibiotic properties (high-dose threshold).
        first_dose: True only for the first dose of the run.

    Returns:
        Updated list of Cell objects (dead cells marked, children added).
    """

pass
