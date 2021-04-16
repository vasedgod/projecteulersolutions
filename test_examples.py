import pytest

from problem39 import Problem39


def test_problem39_example():
    print("not asserting yet")
    problem = Problem39()
    known_solutions = [[20, 48, 52], [24, 45, 51], [30, 40, 50]]
    print("not asserting yet")
    solved_solutions = problem.get_solutions_for_perimeter(120)
    for solution in solved_solutions:
        print("asserting now")
        assert problem.triplet_in_solutions(
            solution, known_solutions
        ), f"{solution} not in {known_solutions}"


if __name__ == "__main__":
    test_problem39_example()