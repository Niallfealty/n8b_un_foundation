""" Code for loading data from different sources

    Currently code makes assumption that data is located in ../data folder
    (will add a config later)
"""

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
