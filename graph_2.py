import matplotlib.pyplot as plt
def graph_2(dose_results: list, mic: float, path: str = "output_3.png") -> None:
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
pass
