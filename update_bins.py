def update_bins(bins: list, dying: list dividing: list, mutated: int):
"""
 new_sensitive = current_sensitive - dying + dividing - mutated 
 new_resistant = current_resistant - dying + dividing + mutated

  if new_sensitive or new_resistant == 0:
    exit 

  Args:
  bins: list of objects with cell counts prior to updating 
  dying: number of dead cells in each bin from count_update()
  dividing: number of dividing cells in each bin from count_update()
  mutated: number of mutating cells in each bin from mutation_uptake()

  Returns:
  updated bins with new cell counts 

"""

pass
