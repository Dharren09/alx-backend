import csv
import math
from typing import List, Dict, Union

def index_range(length: int, page: int, page_size: int) -> tuple:
    """Calculate the start and end index based on the page and page size"""
    if page < 1:
        raise ValueError("Page number must be >= 1.")

    start_index = (page - 1) * page_size
    end_index = start_index + page_size - 1
    return start_index, end_index

class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retrieve the specified page of the dataset"""
        assert isinstance(page, int) and page > 0, "Page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, "Page size must be a positive integer"

        dataset = self.dataset()
        start_index, end_index = index_range(len(dataset), page, page_size)

        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Retrieve information about the dataset page"""

        dataset_page = self.get_page(page, page_size)
        dataset_length = len(self.dataset())

        start_index, end_index = index_range(dataset_length, page, page_size)
        total_pages = math.ceil(dataset_length / page_size)
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            "page_size": len(dataset_page),
            "page": page,
            "data": dataset_page,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
