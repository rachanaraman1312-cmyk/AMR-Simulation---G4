class SimulationParams:
    """
    Attributes:
        tau (float): Size of one time step (e.g. hours).
        max_steps (int): Step limit for one run. A run that hits it
            without reaching the threshold is recorded as "max_steps".
        n_replicates (int): How many times each case is repeated.
        threshold (float): Resistant fraction of the living culture at
            which a run stops and counts as resistant. Default 0.9.
        capacity (int): Carrying capacity of the culture. Divisions are
            limited so the total does not exceed it.
    """


class Antibiotic:
    """Properties of one drug.

    Attributes:
        name (str): Name of the drug.
        drug_class (str): Pharmaceutical class.
        mic (float): Minimum inhibitory concentration from the literature,
            in the same units as the doses. Marked on output_3.
        high_dose_threshold (float): Dose above which moderately resistant
            cells die.
    """
    
class DosingSchedule:
    """How the antibiotic dose changes over time.
    Ideally, dosages should be compunded. 
    Attributes:
        initial_dose (float): Dose given first.
        pct_increase (float): Percentage added to the dose at each
            increase, e.g. 10 means each dose is 10% higher than the last.
        max (float): Optional upper limit on the dose.
    """

class Cell:
    """A single bacterial cell. Cells do not move.

    Attributes:
        alive (bool): False once the cell has died. Dead cells stay dead.
        resistance (float): 0.0 not resistant, 0.5 moderately resistant,
            1.0 resistant.
        mutation (Mutation): The cell's mutation, or None if it has none.
        position (tuple[int, int]): (x, y) pixel location on the grid.
    """


class Mutation:
    """A resistance-conferring mutation. A cell carries at most one.

    Attributes:
        origin (int): 0 for inherent, 1 for acquired.
        strength (float): Resistance the mutation gives (0.5 moderate,
            1.0 full).
        division_penalty (float): Fraction by which the mutation slows
            division. Equals params.cost_per_strength * strength, so
            stronger mutations are costlier.
    """

