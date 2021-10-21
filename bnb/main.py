import copy
import math

from job_table import JobTable
from node import Node
from stack import Stack


def dfs(table):
    stack = Stack()
    first_node = Node(table, "  start")
    stack.push(first_node)
    global_min = math.inf
    global_min_path = []

    while not stack.is_empty():
        for i in range(stack.size() - 1, 0 - 1, -1):
            print(
                stack.items[i].path,
                "| <lower_bound>:",
                stack.items[i].job_table.lower_bound,
            )
        print("--------- <global min>:", global_min)
        print()
        print()
        v = stack.pop()

        if v.job_table.is_step_end:
            if v.job_table.lower_bound < global_min:
                global_min = v.job_table.lower_bound
                global_min_path = v.job_table.path_list
            continue

        if math.isinf(v.job_table.lower_bound):
            continue

        if v.job_table.lower_bound > global_min:
            continue

        leftTable = copy.deepcopy(v.job_table)
        rightTable = copy.deepcopy(v.job_table)

        leftTable.step_select_max_regret()
        rightTable.step_not_select_max_regret()

        path = str(leftTable.path_list[-1])

        leftNode = Node(leftTable, " " + path)
        rightNode = Node(rightTable, "!" + path)

        stack.push(rightNode)
        stack.push(leftNode)

    path_map = []

    for path in global_min_path[: len(global_min_path) - 1]:

        is_first_job_contained = False
        is_second_job_contained = False
        for idx, piece in enumerate(path_map):
            if path[0] in piece:
                is_first_job_contained = True
                idx_piece_containing_first_job = idx
            if path[1] in piece:
                is_second_job_contained = True
                idx_piece_containing_second_job = idx
        if is_first_job_contained and is_second_job_contained:
            path_map[idx_piece_containing_first_job] = (
                path_map[idx_piece_containing_second_job]
                + path_map[idx_piece_containing_first_job]
            )
            del path_map[idx_piece_containing_second_job]
        elif is_first_job_contained:
            path_map[idx_piece_containing_first_job] = path_map[
                idx_piece_containing_first_job
            ] + [path[1]]
        elif is_second_job_contained:
            path_map[idx_piece_containing_second_job] = [path[0]] + path_map[
                idx_piece_containing_second_job
            ]
        else:
            path_map.append(path)

    print("<optimal path list>:", global_min_path)
    print("<optimal path>: ", end="")
    for idx, job in enumerate(path_map[0]):
        if idx != len(path_map[0]):
            print(job, end=" -> ")
    print(path_map[0][0])


if __name__ == "__main__":
    n_jobs = int(input("job의 수를 입력해주세요 > "))
    job_table = JobTable(n_jobs)
    dfs(job_table)
