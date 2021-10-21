from job_table import JobTable


class Node:
    def __init__(self, job_table: JobTable, path: str, left=None, right=None):
        self.job_table = job_table
        self.path = path
        self.left = left
        self.right = right
