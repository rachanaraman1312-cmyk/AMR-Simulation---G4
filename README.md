# AMR-Simulation---G4

# Antibiotic Resistance Evolution Simulator

> **Status: in development.** The design below is final for this checkpoint, but the functions are not implemented yet. Everything under "Planned" describes intended behavior.

A simulation of how a bacterial population develops resistance under antibiotic treatment where each cell is tracked as its own object. 
A run alternates antibiotic doses with growth steps; and survival and mutation are resolved cell by cell.

We are starting with two organisms:

- *Staphylococcus aureus*: beta-lactams, fluoroquinolones and tetracyclines
- *Mycobacterium tuberculosis*: beta-lactams, fluoroquinolones and tetracyclines

## Questions

- How do the populations of alive and resistant cells change over time?
- How does the probability of developing resistance and the resistant fraction change with dose?

## Model scope

This is a simplified, parameter-driven model. It is not mechanistically accurate at the genetic level.

- Each drug uses 2-3 well-studied resistance mutations with literature-based acquisition probabilities.
- Some cells are randomly assigned a higher mutation probability.
- Randomized persister-like cells can survive the first dose.
- Only acquired resistance is modeled. Intrinsic resistance is excluded/randomized.

Results should be read as comparisons under these assumptions, not as clinical predictions.

## Planned design

### Classes

| Class | Represents |
| --- | --- |
| `Cell` | One bacterial cell |
| `Mutation` | One resistance mutation and its acquisition probability |
| `Antibiotic` | One antibiotic |
| `DosingSchedule` | The doses applied during a run |
| `SimulationParameters` | The settings for a run |

### Main functions

Subroutines are not listed.

| Function | Purpose |
| --- | --- |
| `run_replicates` | Simulates n runs of the experiment |
| `run_simulation` | Performs one run, starting by building the colony |
| `get_dose` | Applies an antibiotic dose and determines survival by the model's rules |
| `growth_step` | Simulates one growth step, including division after dosing |
| `count_update` | Updates cell counts after each dose and growth step |
| `mutation_uptake` | Allocates mutations to individual cells |
| `dose_sweep` | Takes a list of doses and returns one set of results |
| `graph_1` | Plots alive and resistant cell populations over time |
| `graph_2` | Plots `dose_sweep` results: probability of resistance or resistant fraction against dose |
| `render_video` | Generates the animation for one run |

### Planned outputs

1. Alive and resistant populations over time (`graph_1`)
2. Probability of resistance or resistant fraction against dose (`graph_2`)
3. An animation of one run (`render_video`)

## Installation and usage

Not available yet.

## Testing

Each function will have its own test datasets.

## Team

- Ashna Surana
- Rachana Raman

## Data

- **Comprehensive Antibiotic Resistance Database (CARD):** https://card.mcmaster.ca [TO DO: state the version and which entries were used, or remove this if CARD is no longer used]

## References

1. Alcock BP, et al. CARD 2023: expanded curation, support for machine learning, and resistome prediction at the Comprehensive Antibiotic Resistance Database. *Nucleic Acids Research*. 2023;51(D1):D690-D699. https://doi.org/10.1093/nar/gkac920
2. Baym M, et al. Spatiotemporal microbial evolution on antibiotic landscapes. *Science*. 2016;353(6304):1147-1151. https://doi.org/10.1126/science.aag0822
3. Gil J, Polański A. Application of Gillespie algorithm for simulating evolution of fitness of microbial population. Applied Computer Science. 2022;18(4):5-15. https://doi.org/10.35784/acs-2022-25
4. Lee J, Blumberg S. abx_amr_simulator: A simulation environment for antibiotic prescribing policy optimization under antimicrobial resistance. SoftwareX. 2026;35:102872. https://doi.org/10.1016/j.softx.2026.102872
5. Pineda-Krch M. GillespieSSA: Implementing the Gillespie Stochastic Simulation Algorithm in R. Journal of Statistical Software. 2008;25(12):1-18. https://doi.org/10.18637/jss.v025.i12
6. Field Day Lab. Antibiotic Resistance. Vault Learning Games Library. https://vaultlearninggames.org/antibiotic-resistance
7. Cairns N. Antibiotic Resistance Simulation. Science Simulations. https://sciencesimulations.com/en/simulations/life-sciences/antibiotic-resistance
