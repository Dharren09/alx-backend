import csv
import math
from typing import List, Dict

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
        self.__indexed_dataset = None
        self.__deleted_rows = set()

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Retrieve information about the dataset page based on index"""

        assert index is None or isinstance(index, int) and index >= 0, "Index must be a non-negative integer"
        assert isinstance(page_size, int) and page_size > 0, "Page size must be a positive integer"

        indexed_dataset = self.indexed_dataset()
        dataset_length = len(indexed_dataset)

        if index is None:
            index = 0
        elif index >= dataset_length:
            return {
                "index": index,
                "next_index": None,
                "page_size": page_size,
                "data": []
            }

        # Adjust the index based on the number of deleted rows
        adjusted_index = index
        for row_index in range(index, dataset_length):
            if row_index not in self.__deleted_rows:
                if adjusted_index != row_index:
                    break
                adjusted_index += 1

        next_index = adjusted_index + page_size

        if next_index >= dataset_length:
            next_index = None

        data = [indexed_dataset[i] for i in range(adjusted_index, min(adjusted_index + page_size, dataset_length))]

        return {
            "index": adjusted_index,
            "next_index": next_index,
            "page_size": page_size,
            "data": data
        }

    def delete_rows(self, rows: List[int]) -> None:
        """Delete rows from the dataset"""
        self.__deleted_rows.update(rows)
        for row_index in rows:
            if row_index in self.__indexed_dataset:
                del self.__indexed_dataset[row_index]
