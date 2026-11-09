def dose_sweep(doses: list, n: int, params: SimulationParams, antibiotic: Antibiotic) -> dict:
    """Run replicate simulations at each dose in a list.

    For each dose, builds a fixed DosingSchedule at that level and calls
    run_replicates, so the only thing that differs between cases is the
    dose.

    We need this to decide how to dose the population. 
    
    Args:
        doses: Dose values to test, in the same units as the MIC.
        n: Replicates per dose.
        params: SimulationParams.
        antibiotic: Antibiotic properties.

    Returns:
        Dict mapping each dose to its list of RunResult objects. This is
        what output_3 reads as dose_results.
    """

    #initialize the dictionary 
    results = {}

    #calculate the dose for each run and store it in the dictionary 
    for dose in doses:
        schedule = DosingSchedule(initial_dose = dose, pct_increase)
        results[dose] = run_replicates(n, schedule, params, antibiotic)
    return results 
    
