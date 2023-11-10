
from time import time, sleep

# Imports print functions that check the lab
# from print_functions_for_lab_checks import *

# Imports functions created for this program
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
# from classify_images import classify_images
# from adjust_results4_isadog import adjust_results4_isadog
# from calculates_results_stats import calculates_results_stats
# from print_results import print_results

# Main program function defined below


def main():
    start_time = time()

    in_arg = get_input_args()

    # check_command_line_arguments(in_arg)

    results = get_pet_labels(None)

    # Function that checks Pet Images in the results Dictionary using results
    # check_creating_pet_image_labels(results)

    # classify_images(None, results, None)

    # Function that checks Results Dictionary using results
    # check_classifying_images(results)

    # adjust_results4_isadog(results, None)

    # Function that checks Results Dictionary for is-a-dog adjustment using results
    # check_classifying_labels_as_dogs(results)

    # results_stats = calculates_results_stats(results)

    # Function that checks Results Statistics Dictionary using results_stats
    # check_calculating_results(results, results_stats)

    # print_results(results, results_stats, None, True, True)

    end_time = time()

    # calculate difference between end time and start time
    tot_time = end_time - start_time
    print("\n** Total Elapsed Runtime:",
          str(int((tot_time/3600)))+":"+str(int((tot_time % 3600)/60))+":"
          + str(int((tot_time % 3600) % 60)))


# Call to main function to run the program
if __name__ == "__main__":
    main()
