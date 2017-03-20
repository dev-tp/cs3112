import random


class Candidate(object):

    def __init__(self, index):
        self.index = index
        self.score = 0


def hire_assistant(candidates):
    permutate_by_sorting(candidates)

    best_candidate = candidates[0]

    for i in range(1, len(candidates)):
        interview(candidates[i])

        if candidates[i].score > best_candidate.score:
            best_candidate = candidates[i]
            hire(candidates[i])


def interview(candidate):
    candidate.score = random.randint(1, 100)


def hire(candidate):
    print '%d: %d' % (candidate.index, candidate.score)


def permutate_by_sorting(candidates):
    random.shuffle(candidates)


def main():
    candidates = [Candidate(i) for i in range(200)]

    hire_assistant(candidates)


if __name__ == '__main__':
    main()
