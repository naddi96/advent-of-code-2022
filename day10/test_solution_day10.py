import sys
import solution_day10 as solution



def test_parse():
    assert solution.parse_input("noop\naddx 3\naddx -5\n")==[('noop', 0), ('addx', 3), ('addx', -5)]

def test_part_1():
    k=solution.parse_input(t1)
    assert solution.part_1(k)==14780
def test_part_2():
    k=solution.parse_input(t1)
    assert solution.part_2(k)==sol_part1



t1='addx 1\nnoop\naddx 2\naddx 11\naddx -4\nnoop\nnoop\nnoop\nnoop\naddx 3\naddx -3\naddx 10\naddx 1\nnoop\naddx 12\naddx -8\naddx 5\nnoop\nnoop\naddx 1\naddx 4\naddx -12\nnoop\naddx -25\naddx 14\naddx -7\nnoop\naddx 11\nnoop\naddx -6\naddx 3\nnoop\naddx 2\naddx 22\naddx -12\naddx -17\naddx 15\naddx 2\naddx 10\naddx -9\nnoop\nnoop\nnoop\naddx 5\naddx 2\naddx -33\nnoop\nnoop\nnoop\nnoop\naddx 12\naddx -9\naddx 7\nnoop\nnoop\naddx 3\naddx -2\naddx 2\naddx 26\naddx -31\naddx 14\naddx 3\nnoop\naddx 13\naddx -1\nnoop\naddx -5\naddx -13\naddx 14\nnoop\naddx -20\naddx -15\nnoop\naddx 7\nnoop\naddx 31\nnoop\naddx -26\nnoop\nnoop\nnoop\naddx 5\naddx 20\naddx -11\naddx -3\naddx 9\naddx -5\naddx 2\nnoop\naddx 4\nnoop\naddx 4\nnoop\nnoop\naddx -7\naddx -30\nnoop\naddx 7\nnoop\nnoop\naddx -2\naddx -4\naddx 11\naddx 14\naddx -9\naddx -2\nnoop\naddx 7\nnoop\naddx -11\naddx -5\naddx 19\naddx 5\naddx 2\naddx 5\nnoop\nnoop\naddx -2\naddx -27\naddx -6\naddx 1\nnoop\nnoop\naddx 4\naddx 1\naddx 4\naddx 5\nnoop\nnoop\nnoop\naddx 1\nnoop\naddx 4\naddx 1\nnoop\nnoop\naddx 5\nnoop\nnoop\naddx 4\naddx 1\nnoop\naddx 4\naddx 1\nnoop\nnoop\nnoop\nnoop\n'

sol_part1='████ █    ███  █    ████  ██  ████ █    \n█    █    █  █ █       █ █  █    █ █    \n███  █    █  █ █      █  █      █  █    \n█    █    ███  █     █   █ ██  █   █    \n█    █    █    █    █    █  █ █    █    \n████ ████ █    ████ ████  ███ ████ ████ \n'

