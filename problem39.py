from itertools import permutations


class Problem39:
    def triplet_in_solutions(self, triplet, solutions):
        triplet_options = permutations(triplet, 3)
        return any(list(option) in solutions for option in triplet_options)

    def triplet_is_valid_right_triangle(self, triplet: tuple):
        return (
            (triplet[0] ** 2 == triplet[1] ** 2 + triplet[2] ** 2)
            or (triplet[1] ** 2 == triplet[0] ** 2 + triplet[2] ** 2)
            or (triplet[2] ** 2 == triplet[0] ** 2 + triplet[1] ** 2)
        )

    def get_solutions_for_perimeter(self, p):
        solutions = []
        for triplet in self.get_triplets_of_side_lengths_for_perimeter(p):
            # print("Checking ", triplet)
            if not self.triplet_in_solutions(
                triplet, solutions
            ) and self.triplet_is_valid_right_triangle(triplet):
                # print(triplet, " is a valid right triangle.")
                solutions.append(triplet)
        return solutions

    def get_triplets_of_side_lengths_for_perimeter(self, p):
        triplets = []

        first_guess_choices = list(range(1, p // 3))
        for i in first_guess_choices:
            second_guess_choices = [el for el in range(1, p - i)]
            for j in second_guess_choices:
                triplets.append([i, j, p - i - j])

        return triplets

    def get_triangle_solutions_up_to(self, pmax):
        solutions = {}
        for p in range(pmax):
            solutions[p] = self.get_solutions_for_perimeter(p)
            print("Checking {}/{}".format(p, pmax), end="\r")

        print("valid solutions are ", solutions)
        return solutions


if __name__ == "__main__":
    problem = Problem39()
    solutions = problem.get_triangle_solutions_up_to(1000)

    perim_with_most_sols = max(solutions, key=lambda x: len(solutions[x]))

    print(
        f"{perim_with_most_sols} has {len(solutions[perim_with_most_sols])} \
            solutions! The max for perimeters up to 1000."
    )
