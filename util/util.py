#/usr/bin/env python
# -*- coding: utf-8 -*-

# import itertools
# import numpy as np
# from matplotlib import pyplot as plt
# import os
# import pandas as pd

def load_lr_data(fname):
    '''
    Load data for the language recognition problem
    '''
    # parse datafile
    snippets = []
    languages = []
    with open(fname) as f:
    # parse all lines in the data file
        for l in f:
            # ul = l.decode('utf-8')
            ul = l
            # get fields separated by commas
            txt, language = ul.split("@")
            # trim strings
            txt = txt.strip()
            language = language.strip()
            # build a snippet object for ease of access
            snippets.append(txt)
            languages.append(language)
    return snippets, languages
