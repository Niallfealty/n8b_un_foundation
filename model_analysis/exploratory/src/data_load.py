""" Code for loading data from different sources

    Currently code makes assumption that data is located in ../data folder
    (will add a config later)
"""

from os import listdir
from os.path import isfile, isdir, join

class DataLoader:
    """ Loader for loading data from multiple different sources
    """

    def __init__(self,
            data_folder_root,
            unpd=False
            gbd=True,
            earth4all=False):

        self.data_folder_root = data_folder_root
        self.unpd = unpd, self.gbd = gbd, self.earth4all = earth4all

    def _load_gbd(self):
        ''' Parse the file contents and load selected data
        '''
        return

    def _parse_gbd_folder(self):
        ''' List files in the gbd data folder and bucket it them
            for loading the data
        '''
        data_folder = self._find_data(data_folder_root)
        filenames = [filename.lower() for ]
    
    def _find_data(self, data_root):
        ''' Work down file path to find at least one csv
        '''
        contained_files = listdir(data_root)
        if len(contained_files) == 1 and isdir(contained_files[0]):
            return self._find_data(join(data_root, contained_files[0]))
        elif any([p.lower().endswith(".csv") for p in contained_files]):
            return data_root
        elif len([d for d in contained files if (isdir(d) and self._find_data(d) is not None)]):
            return [d for d in contained files if (isdir(d) and self._find_data(d) is not None)][0]
        else:
            return None
