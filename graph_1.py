import matplotlib.pyplot as plt
def graph_1(results: list):
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
#creates 8 subplots 
fig, ax = plt.subplots(figsize = (8, 5))

for result in results:
    resistant = [record["resistant"] for record in result.history]
    steps = range(len(resistant))

    #this is being plotted on a logarithmic scale, which introduces some caveats
    #if at a time step, the resistant population drops to zero, log(zero) would be introduced (doesn't exist)
    #each zero value is replaced with NaN instead
    y = [r if r > 0 else float("nan") for r in resistant]

    #step_90 represents the step at which 90% resistance is achieved 
    step_90 = result.step_at_90
    if step_90 is not None: #if step at 90% resistance is actually recorded 
        ax.plot(step_90, resistant[step_90], marker = "*", markersize = 5, color = line.get_color,
                markeredgecolor = "red")

    #defininf a legend for the 90% marker for clarity 
    ax.plot([], [], marker = "*", linestyle = "", color = "white", 
    markeredgecolor = "red", label = "reached 90% resistance")

    ax.set_yscale("log")
    ax.set_xlabel("Step")
    ax.set_ylabel("Resistant cells (log)")
    ax.set_title("Resistant population per run")
    ax.legend(loc = "best")

#saving the file to a defined path 
#path needs to be entered as a separate argument 

fig.savefig(path, dpi = 200, bbox_inches = "tight")
plt.show()
