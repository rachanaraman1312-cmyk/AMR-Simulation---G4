def output_1(results: list):
""" 
first output graph plots the number of resistant as a function of time for each independent run 

Each of the n independent runs is drawn as its own line, with the resistant population on a log-scaled y-axis against time. 
Runs end at different steps (when the culture reaches 90% resistant, goes extinct,
or hits max_steps), so each line stops where its run stopped. The step at which each run reached 90% resistance is marked on its line.
The figure is displayed and saved to path.

    Args:
        results: List of n run_simulation results. Each has the per-step
        history, the outcome, and the step at 90% resistance (None if never reached).
        path: File to save the figure to.

    Returns:
        None. The plot is shown and saved to path.
"""
pass
