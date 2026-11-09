class SimulationParams:
    """Settings that control one growth simulation.

    Attributes:
        t (float): Size of one time step.
        max_steps/population_limit (int/float): Step limit for one run.
        n_replicates (int): Repeats of each case.
        threshold (float): Fraction of living cells that must carry a
            mutation of full strength (1.0) for the run to stop. Default 0.9.
        grid_size (int): Width and height of the grid in pixels.
        initial_cells (int): Size of the starting colony.
        base_division_prob (float): Division probability of a cell with no
            mutation.
        cost_per_strength (float): Division penalty per unit of mutation
            strength. This decides how strongly weak mutants
            outcompete strong ones.
        mutation_rate (float): Probability that a dividing mutation-free
            cell gains a mutation.
        early_phase_hours (float): Window with a raised mutation rate.
        survivor_fraction (float): Share of the colony that survives the
            first dose by chance (0.05 to 0.10).
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
    def __init__(self, name, drug_class, mic, high_dose_threshold):
        self.name = name 
        self.drug_class = drug_class
        if mic <= 0:
            raise ValueError("MIC must be positive")
        if high_dose_threshold <= mic:
            raise ValueError("high dose threshold should exceed MIC")
        self.mic = mic
        self.high_dose_threshold = high_dose_threshold

    def inhibits_sensitive_cells(self, dose) 
     #checks if the current dose is above or below the MIC 
     #this should help guide division 
        return dose >= self.mic 

class DosingSchedule:
    """consider that the antibiotic dose rises over time.

    The dose is given at every step and grows by a fixed percentage each step, compounded.

    Attributes:
        initial_dose (float): Dose at step 0.
        pct_increase (float): Percentage added at each step. 10 means every
            dose is 10% higher than the one before.
        max_dose (float | None): Optional upper limit on the dose.
    """

    if initial_dose <= 0 :
        raise ValueError("Initial dose cannot be less than or equal to zero")
    if pct_increase < 0:
        raise ValueError("For this program, percentage increase has to be positive")
    if max_dose is not None and max_dose < initial_dose:
        raise ValueError("maximum dosage cannot be less than the initial dosage)
    self.initial_dose = initial_dose
    self.pct_increase = pct_increase
    self.max_dose = max_dose 
    
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

