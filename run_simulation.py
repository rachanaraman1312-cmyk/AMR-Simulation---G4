def run_simulation(total_cells: int, resistant_fraction: float, schedule: DosingSchedule, params):
"""
this function runs one simulation from start to finish. 

steps:
  1. call create_bins() -> establishes initial population'
  2. until the population limit is reached, call these sequentially: get_dose(), growth_step():
     save these results: current step number, dose, sensitive and resistant count
  3. checkpoints:
      (i) total_cells_current >= population_limit -> STOP
      (ii) total_cells == 0 -> EDGE CASE, STOP
      (iii) is the population resistant? resistant_cells / total_cells_current >= threshold -> RESISTANT
  4. Build the snapshot, call render_video()

  Returns:
  1. history: list of outputs - step, dose, sensitive, resistant 
  2. outcome: based on checkpoints in step 3
  3. snapshot: visual depiction of culture at stopping step

"""
pass
