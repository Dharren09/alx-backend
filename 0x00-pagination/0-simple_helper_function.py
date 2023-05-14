#!/usr/bin/env python3
"""
function takes two int arg and returns a tuple
"""


def index_range(page: int, page_size: int) -> tuple:
    # check if the page number is valid
    if page < 1:
        raise ValueError("Page number must be greater than or equal to 1.")

    # calculate the start index and the end index
    start_index = (page - 1) * page_size
    end_index = start_index + page_size - 1

    # return the tuple of start index and end index
    return start_index, end_index
