#!/usr/bin/python3
# Date: Mon 24 Jun 2019 17:36:52 CEST
# Author: Nicolas Flandrois
# Description: Running Stardate

from sdview import View
from sdcompute import Compute


def main():
    """main docstring"""
    View.menu(Compute.sdconvert, Compute.sdtranslate)

if __name__ == '__main__':
    main()
