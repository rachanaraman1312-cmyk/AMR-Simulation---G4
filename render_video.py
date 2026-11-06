def render_video.py(results: list, folder: str = "videos", seconds: int = 10, fps: int = 30) -> list:
    """Save one mp4 per run.

    Calls render_video on each run's history and names each file by run
    number and outcome, so runs are easy to tell apart.

    Args:
        results: List of run_simulation results from run_replicates.
        folder: Directory to save the videos in (created if missing).
        seconds: Length of each video.
        fps: Frames per second.

    Returns:
        List of the saved file paths, one per run.
    """
pass
