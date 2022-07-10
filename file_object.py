import os
import shutil
import tkinter

class ExtensionsHashTable:

	def __init__(self):
		self.extensions = {}
		self.intvar = None

	def add(self, extension_name, int_var):
		self.intvar = int_var
		self.extensions[extension_name] = self.intvar
	

# appends a file to the list of the key based on its exentention.
def arrange(category_dictionary, file_list, exclude):
	for file in file_list:
		file_extension = os.path.splitext(file)[1].strip(".")
		if file_extension not in exclude:
			category_dictionary[file_extension.title()].append(file)


def categorize(extension_list):
	categories = {}
	for category in extension_list:
		categories[category.title()] = []
	return categories


def get_extensions(files):
	""" 
		returns all the common file extensions found on the array.
		'files': list/array of File class (array of filenames with extensions)
		return value: set (returns a set data type)
	"""

	return list(set([os.path.splitext(file_ext)[1].strip(".") for file_ext in files]))



def scan(path):
	""" 
		Returns the files that are inside the given path.
		'path': list
		'return value': list
	"""
	os.chdir(path)
	return [listed for listed in os.listdir(path) if os.path.isfile(listed) and not os.path.splitext(listed)[1] == ""]



def create_folders(categ, path):
	"""
		creates a folder provided by the key values found on the 'categ'.
		'categ': dictionary
		'path': string
	"""
	print(path)
	os.chdir(path)
	for key in categ.keys():
		if categ[key] != []:
			if os.path.exists(os.path.abspath(key.title())):
				pass
			else:
				os.mkdir(key.title())


def move_files(categ, path):
	"""
		moves the files to a folder that is named from the 'categ' keys.

		'categ': dictionary
		'path': string
	"""
	for extension_name in categ.keys():
		for value in categ[extension_name]:
			shutil.move(value, extension_name.title())


def exclude(exclude_names, files_list):
	difference = set(files_list) - set(exclude_names)
	return list(difference)
