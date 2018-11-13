import pickle, sys

def pickle_from2(src_file, dest_file):
    if not dest_file:
        data = pickle.load(open(src_file, 'rb'))
        pickle.dump(data, open(src_file, 'wb'), protocol=2)
    else:
        data = pickle.load(open(src_file, 'rb'))
        pickle.dump(data, open(dest_file, 'wb'), protocol=2)


def pickle_from3(src_file, dest_file):
    if not dest_file:
        data = pickle.load(open(src_file, 'rb'), encoding='latin1')
        pickle.dump(data, open(src_file, 'wb'), protocol=2)
    else:
        data = pickle.load(open(src_file, 'rb'), encoding='latin1')
        pickle.dump(data, open(dest_file, 'wb'), protocol=2)

def make_pkl_compatible(src_file, dest_file=None):
    if sys.version_info[0] == 2:
        pickle_from2(src_file, dest_file)
    elif sys.version_info[0] == 3:
        pickle_from3(src_file, dest_file)
    else:
        print('Version to old: currently working on it')

if __name__=="__main__":
    if len(sys.argv) > 2 and len(sys.argv) < 3:
        print("Not a proper usage\n\tusage:\n\t\tpython make_pkl_compatible source_filename\n\t\tpython pickle_2to3 source_filename destination_filename")
        exit()

    if len(sys.argv) == 2:
        src_file = sys.argv[1]
        dest_file = None
    else:
        src_file = sys.argv[1]
        dest_file = sys.argv[2]

    make_pkl_compatible(src_file, dest_file)