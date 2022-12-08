#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats.py
#
# PROGRAMMER: Abhijith Ganesh
# DATE CREATED:28 November

# TODO 5: Define calculates_results_stats function below, please be certain to replace None


def calculates_results_stats(results_dic) -> dict:

    # Initializing empty dict
    results_stats_dict: dict = {
        'n_dogs_img': 0,
        'n_notdogs_img': 0,
        'n_images': len(results_dic),
        'n_match': 0,
        'n_correct_dogs': 0,
        'n_correct_breed': 0,
        'n_correct_notdogs': 0,
        'pct_correct_notdogs': 0.0,
        'pct_correct_dogs': 0.0,
        'pct_correct_breed': 0.0,
    }

    for key, val in results_dic.items():

        if val[2]:
            results_stats_dict['n_match'] += 1

        if val[3]:
            results_stats_dict['n_dogs_img'] += 1

        else:
            '''This code segment checks for images that are not dogs'''
            if val[4] == 0:
                results_stats_dict['n_correct_notdogs'] += 1

        if val[4]:
            results_stats_dict['n_correct_dogs'] += 1
            if val[0] in val[1]:
                results_stats_dict['n_correct_breed'] += 1

    results_stats_dict['n_notdogs_img'] = (results_stats_dict['n_images'] -
                                           results_stats_dict['n_dogs_img'])

    results_stats_dict['pct_match'] = 100 * results_stats_dict[
        'n_match'] / results_stats_dict['n_images']

    results_stats_dict['pct_correct_dogs'] = 100 * results_stats_dict[
        'n_correct_breed'] / results_stats_dict['n_dogs_img']

    results_stats_dict['pct_correct_breed'] = round(
        100 * (results_stats_dict['n_correct_breed'] /
               results_stats_dict['n_correct_dogs']), 2)

    if results_stats_dict['n_notdogs_img'] > 0:
        results_stats_dict['pct_correct_notdogs'] = (
            results_stats_dict['n_correct_notdogs'] /
            results_stats_dict['n_notdogs_img']) * 100.0
    else:
        results_stats_dict['pct_correct_notdogs'] = 0.0

    return results_stats_dict
