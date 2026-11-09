import matplotlib.pyplot as plt
def graph_2(dose_results: list, mic: float, path: str = "output_2.png") -> None:
    """ Plot resistant fraction against dose, with the MIC marked.

    Each point is one dose from dose_sweep: the dose is on the x-axis and
    the resistant fraction of the culture is on the y-axis, averaged over
    that dose's replicates. A vertical line marks the MIC (minimum
    inhibitory concentration) for the antibiotic. The figure is displayed
    and saved to path.

    Args:
        dose_results: Output of dose_sweep, one entry per dose, each
            holding the dose and the resistant and total population counts
            from its replicates.
        mic: MIC for the antibiotic-organism pair, taken from the
            literature, in the same units as the doses.
        path: File to save the figure to.

    Returns:
        None. The plot is shown and saved to path.
    """
    
    doses = sorted(dose_results)

    #means stores the average resistant fraction for each dose
    #spreads stores the standard deviation of the resistant fractions (quantifies differences)
    means, spreads = [], []

    for dose in doses:
        fractions = []
        for result in dose_results[dose]:
            final = result.history[-1]
            # An extinct culture has no fraction, so it is excluded. 
            if final["total"] > 0:
                fractions.append(final["resistant"] / final["total"])

        if fractions:
            means.append(statistics.mean(fractions))
            spreads.append(statistics.stdev(fractions) if len(fractions) > 1 else 0.0)
        else:
            means.append(float("nan"))
            spreads.append(0.0)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.errorbar(doses, means, yerr=spreads, marker="*", capsize=3,
                label="Mean resistant fraction (± 1 SD)")
    ax.axvline(mic, color="red", linestyle="--", label=f"MIC = {mic:g}")

    ax.set_ylim(0, 1.05)
    ax.set_xlabel("Dose")
    ax.set_ylabel("Resistant fraction of culture")
    ax.set_title("Resistant fraction vs dose")
    ax.legend(loc="best")

    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.show()
