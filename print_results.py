#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
#
# PROGRAMMER: Abhijith Ganesh
# DATE CREATED: 28 November
# REVISED DATE:
# PURPOSE: Create a function print_results that prints the results statistics
#          from the results statistics dictionary (results_stats_dic). It
#          should also allow the user to be able to print out cases of misclassified
#          dogs and cases of misclassified breeds of dog using the Results
#          dictionary (results_dic).
#         This function inputs:
#            -The results dictionary as results_dic within print_results
#             function and results for the function call within main.
#            -The results statistics dictionary as results_stats_dic within
#             print_results function and results_stats for the function call within main.
#            -The CNN model architecture as model wihtin print_results function
#             and in_arg.arch for the function call within main.
#            -Prints Incorrectly Classified Dogs as print_incorrect_dogs within
#             print_results function and set as either boolean value True or
#             False in the function call within main (defaults to False)
#            -Prints Incorrectly Classified Breeds as print_incorrect_breed within
#             print_results function and set as either boolean value True or
#             False in the function call within main (defaults to False)
#         This function does not output anything other than printing a summary
#         of the final results.
##
# TODO 6: Define print_results function below, specifically replace the None
#       below by the function definition of the print_results function.
#       Notice that this function doesn't to return anything because it
#       prints a summary of the results using results_dic and results_stats_dic
#

from classify_images import classify_images
from get_pet_labels import get_pet_labels
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats


def print_results(results_dic,
                  results_stats_dic,
                  model,
                  print_incorrect_dogs=False,
                  print_incorrect_breed=False) -> None:
    print(
        f"*** Results Summary for CNN Model Architecture : { model.upper()} ***"
    )

    print("{:20}: {:3d}".format('N Images', results_stats_dic['n_images']))
    print("{:20}: {:3d}".format('N Dog Images',
                                results_stats_dic['n_dogs_img']))
    print("{:20}: {:3d}".format('N Not Dog Images',
                                results_stats_dic['n_notdogs_img']))

    print(
        f"*** Summary Statistics for CNN Model Architecture : {model.upper()} ***"
    )

    print(f"Number of matching labels: {results_stats_dict['n_match']}")

    print(
        f"Number of dogs matching breeds: {results_stats_dict['n_correct_breed']}"
    )

    print(f"Percentage of matching labels: {results_stats_dict['pct_match']}")
    print(
        f"Percentage of correct breed: {results_stats_dict['pct_correct_breed']}"
    )

    if (print_incorrect_dogs):

        print(
            f"Number of incorrect dogs: {results_stats_dict['n_dogs_img']-results_stats_dict['n_correct_dogs']}"
        )
        print(
            f"Percentage of incorrect dogs: {100-results_stats_dict['pct_correct_dogs']}"
        )
        
    if (print_incorrect_breed):
        print(
            f"Number of incorrect breeds: {results_stats_dict['n_dogs_img']-results_stats_dict['n_correct_breed']}"
        )
        print(
            f"Percentage of incorrect breed: {100-results_stats_dict['pct_correct_vreed']}"
        )


results_dict = get_pet_labels('pet_images/')
classify_images('pet_images/', results_dict, 'vgg')
adjust_results4_isadog(results_dict, "dognames.txt")
results_stats_dict = calculates_results_stats(results_dict)

print_results(results_dict, results_stats_dict, 'VGG', False, False)