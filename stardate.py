#!/usr/bin/python3
#Date: 
#Author: Nicolas Flandrois
#Description:

from sdview import View
from sdcompute import Compute

def main():
	"""main docstring"""
	View.menu(Compute.sdconvert, Compute.sdtranslate)

if __name__=='__main__':
	main()