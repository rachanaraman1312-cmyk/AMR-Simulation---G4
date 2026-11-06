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
    """
    Attributes:
        type (str): "fixed", "incremental" or "pulsed".
        level (float): The dose (fixed), or the full dose at each pulse
            (pulsed).
        start (float): Starting dose (incremental only).
        increase (float): Amount added per step (incremental only).
        max (float): Upper limit on the dose (incremental only).
        interval (int): Steps between pulses (pulsed only).
        decay (float): Fraction of the dose left after each step (pulsed
            only).
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
    """A resistance-conferring mutation carried by a cell.

    Attributes:
        origin (int): 0 for inherent, 1 for acquired. Inherent mutations
            raise the cell's probability of developing further mutations.
        strength (float): How much resistance the mutation adds. Stronger
            mutations are more likely to develop in cells that already
            carry one.
        rate (float): Probability that a dividing cell acquires this
            mutation, from the literature review.
    """
