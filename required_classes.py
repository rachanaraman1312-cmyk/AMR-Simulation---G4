from dataclasses import dataclass
import random
import math

@dataclass
class SimulationParams:
    """Settings that control one growth simulation.

    Attributes:
        t (float): Size of one time step, in hours.
        max_steps (int): Step limit for one run.
        population_limit (float): Run stops once the colony is this big.
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
        early_multiplier (float): How much the mutation rate is raised by
            during the early phase.
        survivor_fraction (float): Share of the cells a dose can kill that
            survive it by chance (0.05 to 0.10).
        first_dose_hours (float): Time of first dose.
        dose_interval_hours (float): Time between doses.
    """
    # one shared set of parameters for every cell in a run

    # time and stopping
    t: float = 1.0                     # hours per step
    max_steps: int = 500               # stop after this many steps
    population_limit: float = 10**19   # effectively no limit
    n_replicates: int = 10             # runs per set of settings
    threshold: float = 0.9             # stop at 90% full-strength cells

    # grid
    grid_size: int = 100               # 100 x 100 grid
    initial_cells: int = 20            # cells at the start

    # growth
    base_division_prob: float = 0.5    # chance per step for a normal cell
    cost_per_strength: float = 0.2     # full strength: 0.5 * (1 - 0.2) = 0.4

    # mutation
    mutation_rate: float = 0.001       # chance a daughter mutates
    early_phase_hours: float = 10.0    # first 10 hours...
    early_multiplier: float = 5.0      # ...mutate 5x more often

    # antibiotic timing (how strong each dose is lives in DosingSchedule)
    survivor_fraction: float = 0.07    # 7% of killable cells survive a dose
    first_dose_hours: float = 30.0     # first dose at hour 30
    dose_interval_hours: float = 24.0  # then one dose every 24 hours

    def __post_init__(self):
        # runs automatically right after __init__ has set all the fields
        # probabilities have to be between 0 and 1
        check_range("threshold", self.threshold, 0, 1)
        check_range("base_division_prob", self.base_division_prob, 0, 1)
        check_range("mutation_rate", self.mutation_rate, 0, 1)
        check_range("survivor_fraction", self.survivor_fraction, 0, 1)


def check_range(name, value, min, max):
    # Error check: raises an error if value is outside [low, high]
    # name is only used to make the error message readable
    if value < min or value > max:
        raise ValueError(name + " must be between " + str(min) + " and " + str(max))





@dataclass
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

    def inhibits_sensitive_cells(self, dose): 
     #checks if the current dose is above or below the MIC 
     #this should help guide division 
        return dose >= self.mic 

@dataclass
class DosingSchedule:
    """consider that the antibiotic dose rises over time.

    The dose is given at every step and grows by a fixed percentage each step, compounded.

    Attributes:
        initial_dose (float): Dose at step 0.
        pct_increase (float): Percentage added at each step. 10 means every
            dose is 10% higher than the one before.
        max_dose (float | None): Optional upper limit on the dose.
    """
    initial_dose:float = 0.0
    pct_increase: float = 10.0
    max_dose: float = 0.0


    def __init__(initial_dose, pct_increase, max_dose):
    #intitial checkpoints 
        if initial_dose <= 0 :
            raise ValueError("Initial dose cannot be less than or equal to zero")
        if pct_increase < 0:
            raise ValueError("For this program, percentage increase has to be positive")
        if max_dose is not None and max_dose < initial_dose:
            raise ValueError("maximum dosage cannot be less than the initial dosage")
                             
    #initializing the attributes 
        self.initial_dose = initial_dose
        self.pct_increase = pct_increase
        self.max_dose = max_dose 

    def dose_at(self, step):
        #calculates dose at a given step 
        if step < 0:
            raise ValueError("step cannot be negative")
        dose = self.initial_dose * (1 + (self.pct_increase / 100)) * step
        #if the calculated dose is greater than max_dose (if given), we need to select max_dose 
        if self.max_dose is not None:
            dose = min(dose, self.max_dose)
        return dose 

    def doses(self, n_steps):
        #list of all doses for n steps 
        return [self.dose_at(step) for step in range(n_steps)]

@dataclass
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
    name: str
    origin: int
    strength: float
    division_penalty: float


@dataclass      
class Cell:
    """A single bacterial cell. Cells do not move.

    Attributes:
        alive (bool): False once the cell has died. Dead cells stay dead.
        resistance (float): 0.0 not resistant, 0.5 moderately resistant,
            1.0 resistant.
        mutation (Mutation): The cell's mutation, or None if it has none.
        position (tuple[int, int]): (x, y) pixel location on the grid.
    """

# each cell has its own values (unlike SimulationParams)
    alive: bool = True
    resistance: float = 0.0
    mutation: Mutation | None = None
    position: tuple[int, int] = (0, 0)

    def division_prob(self, params):
        # chance this cell divides in one step
        if self.mutation is None:
            return params.base_division_prob
        # a mutation slows division by its penalty fraction
        return params.base_division_prob * (1 - self.mutation.division_penalty)

    def is_full_strength(self):
        # True if the cell is fully resistant
        # >= 0.999 instead of == 1.0 because of float rounding
        return self.resistance >= 0.999

    def can_grow(self, dose, antibiotic):
        # True if this cell can divide at the current dose
        if self.is_full_strength():
            return True  # fully resistant, the drug never stops it
        if self.resistance > 0:
            return not antibiotic.inhibits_moderate_cells(dose)
        return not antibiotic.inhibits_sensitive_cells(dose)

