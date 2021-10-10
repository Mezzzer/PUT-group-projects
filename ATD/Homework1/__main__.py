import argparse
from prisoner import Prisoner
from judge import Judge
import time

def main(infinite=False, known=False, number_of_iterations=5):
    number_of_iterations=int(number_of_iterations)

    prisoner_A = Prisoner()
    prisoner_B = Prisoner()
    judge = Judge()

    if infinite:
        while True:
            response_A = prisoner_A.testify('infinite')
            response_B = prisoner_B.testify('infinite')
            sentence = judge.sentence(response_A, response_B)
            print('Sentence: prisoner_A=', sentence[0], ' prisoner_B=', sentence[1])
            time.sleep(1)
    elif known:
        for i in range(number_of_iterations):
            response_A = prisoner_A.testify(number_of_iterations)
            response_B = prisoner_B.testify(number_of_iterations)
            sentence = judge.sentence(response_A, response_B)
            print('Sentence: prisoner_A=', sentence[0], ' prisoner_B=', sentence[1])
            time.sleep(1)
    else:
        for i in range(number_of_iterations):
            response_A = prisoner_A.testify()
            response_B = prisoner_B.testify()
            sentence = judge.sentence(response_A, response_B)
            print('Sentence: prisoner_A=', sentence[0], ' prisoner_B=', sentence[1])
            time.sleep(1)


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--infinite', default=False, action='store_true', help='if inifinite number of iterations')
    parser.add_argument('-k', '--known', default=False, action='store_true', help='if known number of iterations')
    parser.add_argument('-i', '--number_of_iterations', default=5, help='number of iteration')

    args = parser.parse_args()
    
    return args

if __name__ == "__main__":
    args = parse_arguments()
    main(**vars(args))