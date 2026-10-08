"""Application settings read from the environment."""

import os

DEFAULT_PAGE_SIZE = 50


def get_page_size() -> int:
    """Return the number of todos to show per page.

    Returns:
        The page size from the ``PAGE_SIZE`` environment variable, or the
        default if it is unset.
    """
    return int(os.environ.get("PAGE_SIZE", DEFAULT_PAGE_SIZE))
