import heuristic
import bruteforce
import unittest
import branchAndBound
import decomposition_by_price
import fptas
import genetic_algorithm


tested_module = genetic_algorithm

class TestValues(unittest.TestCase):
    filenames=[("knap_4.inst", "knap_4.sol")]
            # ("knap_10.inst", "knap_10.sol"),
            # ("knap_15.inst", "knap_15.sol"),
            # ("knap_20.inst", "knap_20.sol"),
            # ("knap_22.inst", "knap_22.sol"),
            # ("knap_25.inst", "knap_25.sol"),
            # ("knap_27.inst", "knap_27.sol"),
            # ("knap_30.inst", "knap_30.sol"),
            # ("knap_32.inst", "knap_32.sol"),
            # ("knap_35.inst", "knap_35.sol"),
            # ("knap_37.inst", "knap_37.sol"),
            # ("knap_40.inst", "knap_40.sol")]


    def test_values(self):
        '''
        this function goes through all data in files specified in 'filenames',
        tries if 'compute' function gives expected result,
        prints ratio correct/all results (accuracy)
        '''
        correct_total, wrong_total = 0,0
        for filename in self.filenames:
            input_filename, output_filename = "inst/" + filename[0] + ".dat", "sol/" + filename[1] + ".dat"
            function_output=tested_module.compute(input_filename, False)
            correct_output=[]
            with open(output_filename, 'r') as file:
                for line in file:
                    correct_output.append(line.rstrip())
            for function_line, correct_line in zip(correct_output, function_output):
                if(function_line != correct_line):
                    wrong_total+=1
                    print(input_filename, ": ", function_line, " != ", correct_line)
                else:
                    correct_total+=1
        print('TOTAL: ', correct_total, '/', correct_total + wrong_total, ', ',
              correct_total / (correct_total + wrong_total) * 100, '%')


if __name__ == '__main__':
    unittest.main()