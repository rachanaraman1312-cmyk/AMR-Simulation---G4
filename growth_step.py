def growth_step(cells: list, dose: float, params: SimulationParams,
                antibiotic: Antibiotic, first_dose: bool) -> list:
    """Run one growth step: death, then division.

    Death, for each living cell if dose > 0:
        - No mutation (resistance 0): dies.
        - Moderate mutation (0.5): dies if dose exceeds
          antibiotic.high_dose_threshold.
        - Full mutation (1.0): survives.
        - On the first dose, a random 5 to 10% of the colony survives
          regardless (params.survivor_fraction).
        - Dead cells stay dead.

    Division, for each surviving cell:
        - Needs at least 1 px of free space, otherwise it cannot divide.
        - Divides with probability
          params.base_division_prob * (1 - mutation.division_penalty),
          so mutation-free cells divide fastest and strong mutants slowest.
        - The child is placed in a free neighbouring pixel and inherits the
          parent's mutation (or lack of one) in full, since a cell is locked
          into one mutation for life.

    Then calls count_update and mutation_uptake.

    Args:
        cells: List of Cell objects; modified in place.
        dose: Antibiotic dose for this step.
        params: SimulationParams.
        antibiotic: Antibiotic properties (high-dose threshold).
        first_dose: True only for the first dose of the run.

    Returns:
        Updated list of Cell objects.
    """
pass
