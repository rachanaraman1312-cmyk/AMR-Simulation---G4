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
    """
    Attributes:
        name (str): Name of the drug.
        drug_class (str): Pharmaceutical class.
        mic (float): Minimum inhibitory concentration from the literature,
            in the same units as the doses. Marked on output_3.
        mutation_prob (float): Chance that a dividing sensitive cell
            becomes resistant. Fixed value for this antibiotic-organism
            pair, from the literature review.
        max_kill (float): Highest kill rate the drug can reach (Hill
            equation).
        h (float): Steepness of the dose-response curve (Hill equation).
        ec50 (float): Dose giving half of max_kill (Hill equation).
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

class 
