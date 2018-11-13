# Pickle_compatible
For resolving the issue of pickle in different version of python

Usage of Picke_compatible:

    > $ python pickle_compatible.py source_filename
    
    > $ python pickle_compatible.py source_filename destination_filename
   
OR can be used the api in side your project:

Add pickle_compatible.py to your project and add following lines:

    > from pickle_compatible import make_pkl_compatible
    ...
    > make_pkl_compatible(filename)
    
    or
    
    > from pickle_compatible import make_pkl_compatible
    ...
    > make_pkl_compatible(src_file, dest_file)