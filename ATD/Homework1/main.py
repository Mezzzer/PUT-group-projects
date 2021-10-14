import argparse
from src.prisoners import InfinitePrisoner, KnownPrisoner, UnknownPrisoner
from src.judge import Judge
import time

prisoner_a = None
prisoner_b = None
judge = Judge()


def perform_one_judge():
    response_a = prisoner_a.testify()
    response_b = prisoner_b.testify()
    sentence = judge.sentence(response_a, response_b)
    prisoner_a.serve_sentence(sentence['prisoner_a'])
    prisoner_b.serve_sentence(sentence['prisoner_b'])
    print('========')
    print('Sentence: prisoner_a = ', sentence["prisoner_a"], ' prisoner_b = ', sentence["prisoner_b"])
    print('========')
    time.sleep(0.5)


def main(infinite=False, known=False, number_of_iterations=5):
    number_of_iterations = int(number_of_iterations)
    global prisoner_a
    global prisoner_b

    if infinite:
        prisoner_a = InfinitePrisoner(name='prisoner_a', number_of_future_arrests='infinity')
        prisoner_b = InfinitePrisoner(name='prisoner_b', number_of_future_arrests='infinity')

        while True:
            perform_one_judge()

    elif known:
        prisoner_a = KnownPrisoner(name='prisoner_a', number_of_future_arrests=number_of_iterations)
        prisoner_b = KnownPrisoner(name='prisoner_b', number_of_future_arrests=number_of_iterations)

        for i in range(number_of_iterations):
            perform_one_judge()

    else:
        prisoner_a = UnknownPrisoner(name='prisoner_a', number_of_future_arrests=None)
        prisoner_b = UnknownPrisoner(name='prisoner_b', number_of_future_arrests=None)

        for i in range(number_of_iterations):
            perform_one_judge()


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--infinite', default=False, action='store_true',
                        help='if inifinite number of iterations')
    parser.add_argument('-k', '--known', default=False, action='store_true', help='if known number of iterations')
    parser.add_argument('-i', '--number_of_iterations', default=10, help='number of iteration')

    args = parser.parse_args()

    return args


if __name__ == "__main__":
    args = parse_arguments()
    main(**vars(args))
