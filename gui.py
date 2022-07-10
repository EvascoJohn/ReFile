import tkinter
import os
from tkinter import filedialog
from PIL import ImageTk, Image
import file_object

root = tkinter.Tk()
root.title("ReFile")
root.iconbitmap('refile_logo.ico')
files_list = []
extension_list = []
scan_path = ""
destination_path = ""
scanned_dir = tkinter.StringVar()
destination_dir = tkinter.StringVar()
scanned_dir.set(scan_path)

extensions_table = file_object.ExtensionsHashTable()

def set_scan_directroy_path():
   global scan_path, files_list, extension_list, extensions_table, scanning_directory
   scan_path = filedialog.askdirectory()
   scanned_dir.set(scan_path)
   if scan_path:
      files_list = file_object.scan(scan_path)
      extension_list = file_object.get_extensions(files_list)
      for extension in extension_list:
         extensions_table.add(extension, tkinter.IntVar())

def set_destination_path():
   global destination_path, destination_dir
   destination_path = filedialog.askdirectory()
   destination_dir.set(destination_path)

def select_extension():
   extensions_window = tkinter.Toplevel()
   extensions_window.title("Select Extensions")
   extensions_window.geometry("400x200")
   check_button_list = []
   tkinter.Label(extensions_window, text="Here are the existing file extensions in the directory provided:").pack()
   for extension in extensions_table.extensions:
      tkinter.Checkbutton(extensions_window, text=extension, variable=extensions_table.extensions[extension]).pack(anchor="w")

   ok_button = tkinter.Button(extensions_window, text="Okay", command=extensions_window.destroy)
   ok_button.pack(anchor="s")


def sort_files():
   exluded_list = []
   for extension in extensions_table.extensions:
      if extensions_table.extensions[extension].get() == 0:
         exluded_list.append(extension)

   if destination_path and scan_path:
      categorized_hashtable = file_object.categorize(extensions_table.extensions)
      file_object.arrange(categorized_hashtable, files_list, exluded_list)
      file_object.create_folders(categorized_hashtable, destination_path)
      file_object.move_files(categorized_hashtable, destination_path)


#Declares GUI
extensions_button = tkinter.Button(root, text="Select Extensions", command=select_extension, borderwidth=1)
scan_directory_button = tkinter.Button(root, text="Scan Directory", command=set_scan_directroy_path, borderwidth=1)
set_destination_button = tkinter.Button(root, text="Select Destination", command=set_destination_path, borderwidth=1)
sort_button = tkinter.Button(root, text="Sort Files", command=sort_files, borderwidth=1)
scanning_directory = tkinter.Entry(root, textvariable=scanned_dir)
destination_directory = tkinter.Entry(root, textvariable=destination_dir)

button_size = (1, 20)
directory_entry_size = (30, 40)

extensions_button["width"] = button_size[1]
extensions_button["height"] = button_size[0]

scan_directory_button["width"] = button_size[1]
scan_directory_button["height"] = button_size[0]

set_destination_button["width"] = button_size[1]
set_destination_button["height"] = button_size[0]

destination_directory["width"] = directory_entry_size[1]
sort_button["width"] = button_size[1]
sort_button["height"] = button_size[0]

scanning_directory["width"] = directory_entry_size[1]


scan_directory_button.grid(row=0, column=0)
scanning_directory.grid(row=0, column=1)
set_destination_button.grid(row=1, column=0)
destination_directory.grid(row=1, column=1)
extensions_button.grid(row=2, column=0)
sort_button.grid(row=3, column=0)

root.mainloop()