class Bin:
  """ group of bacteria with the same properties

      features:
      type: 0 -> sensitive, 1 -> resistant 
      cells: number of cells in the bin 
      MIC: how resistant the bin is 
  """

class SimulationParams:
  """
  parameters that need constant updation for growth simulation 
  
  features:
    tau           size of one time step
        max_steps     step limit for one run
        n_replicates  how many times each case is repeated
        threshold     resistant fraction that counts as "resistant" (0.9)
        capacity      carrying capacity of the culture
        mutation_prob chance a dividing sensitive cell becomes resistant
                      (fixed value from the literature review)
        max_kill      highest drug kill rate (Hill equation)
        h             steepness of the dose-response curve (Hill equation)
  """

class Antibiotic:
"""
  parameters of the drug 

  features:
    name: name of drug
    drug_class: pharmaceutical class
    max_kill: outcome of Hill equation 
    decay: see DosingSchedule class features 

  """
class DosingSchedule:
"""
The settings that define how the antibiotic dose changes over time.

    features:
        type: "fixed", "incremental" or "pulsed"
        level: the dose (fixed), or the full dose at each pulse (pulsed)
        start: starting dose (incremental only)
        increase: amount added per step (incremental only)
        max: upper limit on the dose (incremental only)
        interval: steps between pulses (pulsed only)
        decay: fraction of the dose left after each step (pulsed only)
  """
