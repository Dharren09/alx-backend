#!/usr/bin/env python3
"""
function takes two int arg and returns a tuple
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """check if the arguments are valid"""
    assert isinstance(page, int) and page > 0
    assert isinstance(page_size, int) and page_size > 0

    """calculate the start index and the end index"""
    start_index = (page - 1) * page_size
    end_index = (start_index + page_size)

    """return the tuple of start index and end index"""
    return start_index, end_index
