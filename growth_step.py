def growth_step(cells: list, dose: float, params):
    """Runs one growth step of the simulation.

    Counts the living cells, then for each living cell:
        - Calculates the kill rate from the dose using the Hill equation
          (see references), scaled by the cell's resistance.
        - Calculates the death probability from the kill rate.
        - Calculates the division probability. A cell divides only if it has
          at least 1 px of free space; the child is placed in a free
          neighbouring pixel and inherits the parent's mutation with a
          raised probability.

    Then calls count_update() and mutation_uptake().

    Args:
        cells: List of Cell objects.
        dose: Current antibiotic concentration.
        params: SimulationParams (Hill parameters, inheritance boost,
            grid size).

    Returns:
        Updated list of Cell objects (dead cells marked, children added).
    """
