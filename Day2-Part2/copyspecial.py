#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import subprocess

"""Copy Special exercise
"""
def copy_to_dir(paths , dir):
	if not os.path.exists(dir):
		os.mkdir(dir)

	for path in paths:
		shutil.copy(path , dir)
	return

def copy_to_zip(paths , zip):
	cmd = "zip -j "+zip 
	for path in paths:
		cmd += " " + path
	print("Going to run:",cmd)
	os.system(cmd)
	return

def list_special_files(dir):
	if not os.path.exists(dir):
		print ("dir:",dir,"doesn't exist")
		return []

	pat = re.compile('_\w+_')
	abs_paths = []
	filenames = os.listdir(dir)
	for name in filenames:
		if pat.search(name) is not None:
			abs_paths.append(os.path.abspath(os.path.join(dir , name)))
	return abs_paths

# +++your code here+++
# Write functions and modify main() to call them



def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print ("usage: [--todir dir][--tozip zipfile] dir [dir ...]")
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args and args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print ("error: must specify one or more dirs")
    sys.exit(1)

  spl_file = []
  for d in args:
  	spl_file += list_special_files(d)

  # Call your functions
  if todir != '':
  	copy_to_dir(spl_file , todir)

  if tozip != '':
  	copy_to_zip(spl_file , tozip)

  if todir == '' and tozip == '':
  	for file in spl_file:
  		print (file)

  
if __name__ == "__main__":
  main()
