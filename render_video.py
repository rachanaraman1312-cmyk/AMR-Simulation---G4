def render_video(history: list, seconds: int = 10, fps: int = 30,
                 path: str = "render_video.mp4") -> str:
    """Render one run as an mp4 of the cells on the grid.

    Each frame draws every cell at its real position, coloured by resistance (0, 0.5, 1), with dead cells shown faded or hidden. 
    The run's steps are spread evenly across seconds * fps frames, so every video has the same length.

    Args:
        history: History from ONE run, with one entry per step holding each
            cell's position, alive state and resistance.
        seconds: Length of the video. Default 10.
        fps: Frames per second. Default 30, so 300 frames in total.
        path: File to save the mp4 to.

    Returns:
        Path of the saved mp4 file.
    """
pass
