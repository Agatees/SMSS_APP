# Title              : Service Management system
# Author             : Agateeswaran K
# Created on         : 14/08/2023
# Last Modified Date : 22/08/2023
# Reviewed by        :
# Reviewed on        :

import time
import sys
from fetch_property import fetch_property


class Animator:

    # 1. User-defined function to perform splitting-up a string to a list
    @staticmethod
    def string_split_up(string, delimiter):
        list1 = string.split(delimiter)
        return list1

    # 2. User-defined function for loading animations
    @staticmethod
    def loading_animation(case, word):
        if word is None:
            word = fetch_property('animation', 'WORD')

        # 10.5 seconds
        if case == 1:
            animation_chars1 = ["[                   ]", "[█                  ]", "[██                 ]",
                                "[███                ]", "[████               ]", "[█████              ]",
                                "[██████             ]", "[███████            ]", "[████████           ]",
                                "[█████████          ]", "[██████████         ]", "[███████████        ]",
                                "[████████████       ]", "[█████████████      ]", "[██████████████     ]",
                                "[███████████████    ]", "[████████████████   ]", "[█████████████████  ]",
                                "[██████████████████ ]", "[███████████████████]", "complete!"]
            for i in range(21):
                sys.stdout.write("\r" + word + " " + animation_chars1[i])
                sys.stdout.flush()
                time.sleep(0.5)
        # 6 seconds
        if case == 2:
            string1 = fetch_property('animation', 'ANIMATION_CHARS2')
            animation_chars2 = Animator.string_split_up(string1, ',')
            for i in range(9):
                sys.stdout.write("\r" + word + " " + animation_chars2[i])
                sys.stdout.flush()
                time.sleep(.25)
        # # 8 seconds
        # if case == 3:
        #     string1 = fetch_property('animation', 'animation_chars3')
        #     animation_chars3 = Animator.string_split_up(string1, ',')
        #     for i in range(8):
        #         sys.stdout.write("\r" + word + " " + animation_chars3[i])
        #         sys.stdout.flush()
        #         time.sleep(1)
        # # 13 seconds
        # if case == 4:
        #     string1 = fetch_property('animation', 'animation_chars4')
        #     animation_chars4 = Animator.string_split_up(string1, ',')
        #     for i in range(13):
        #         sys.stdout.write("\r" + word + " " + animation_chars4[i])
        #         sys.stdout.flush()
        #         time.sleep(1)
        # 10 seconds
        if case == 5:
            animation_chars5 = ['⌜ ', ' ⌝', ' ⌟', '⌞ ', "complete!"]  # 5
            for i in range(5):
                sys.stdout.write("\r" + word + " " + animation_chars5[i])
                sys.stdout.flush()
                time.sleep(1)
        print("\n")

# CLASSES   : 01, Animator
# FUNCTIONS : 02
