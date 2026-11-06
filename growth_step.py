def growth_step(cells: list, dose: float, params):
   """Run one growth step of the simulation.

    Counts the living cells, then for each living cell:
        - Death: if dose > 0, the cell dies or survives by its resistance.
            - Not resistant (0): dies.
            - Moderately resistant (0.5): dies if dose exceeds the
              high-dose threshold.
            - Resistant (1): survives.
            - On the first dose, a random 5-10% of the colony survives
              regardless of resistance.
            - Dead cells stay dead.
        - Division: a living cell divides with a base division probability.
          It needs at least 1 px of free space, otherwise it cannot divide.
          A single cell divides, and two cells of the same type divide.
          The child is placed in a free neighbouring pixel and inherits the
          parent's mutation with a raised probability.

    Then calls count_update() and mutation_uptake().

    Args:
        cells: List of Cell objects.
        dose: Current antibiotic concentration.
        params: SimulationParams (high-dose threshold, survivor fraction,
            base division probability, inheritance boost, grid size).

    Returns:
        Updated list of Cell objects (dead cells marked, children added).
    """
pass
