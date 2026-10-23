def growth_step(bins: list,dose: float, params)
""" runs the simulation for the growth once 
  add up cells in the bin to get the totsl cells during the nth run 
  calculate crowding parameter = total cells / capacity
    if crowding > 1: terminate the code 
  for bin in bins:
    kill rate = use hill equation (see references)
    calculate death probability 
    calculate division probability 

  call count_update()
  call mutation_uptake()
  call update_bins()
  
  Args:
    bins: list og Bin objects 
    dose: current antibiotic concentration 
    params: parameters needed 


  Returns:
    updated list of bins 

"""

pass
