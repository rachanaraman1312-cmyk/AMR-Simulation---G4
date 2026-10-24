def render_video.py(history: list, seconds: int = 10, fps: int = 30):
    """
    Turn last (limiting) run into a short mp4.

    Args:
        history: the history from ONE run (not the whole list of results).
                 One entry per step, holding the counts of both bins.
        seconds: length of the video. Default 10
        fps:     frames per second. Default 30, so 300 frames in total

    Output:
        an mp4 file. Dots are drawn at random positions (1 dot = k cells),
        so the video shows proportions, not real cell movement.
        Returns file path 
    """
