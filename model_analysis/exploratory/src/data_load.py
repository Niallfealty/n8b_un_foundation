""" Code for loading data from different sources

    Currently code makes assumption that data is located in ../data folder
    (will add a config later)
"""

from os import listdir
from os.path import isfile, isdir, join
from re import compile as re_compile

class DataLoader:
    """ Loader for loading data from multiple different sources
    """
    FORECAST_NAME = re_compile(r"ihme_pop_\d{4}_\d{4}")
    END_CODE = re_compile(r"_([a-z0-9]*).csv$|_([a-z0-9]*)$")

    def __init__(self,
            data_folder_root,
            unpd=False,
            gbd=True,
            earth4all=False):

        self.data_folder_root = data_folder_root
        self.unpd, self.gbd, self.earth4all = unpd, gbd, earth4all

    def _load_gbd(self):
        ''' Parse the file contents and load selected data
        '''
        return

    def _parse_gbd_folder(self):
        ''' List files in the gbd data folder and bucket it them
            for loading the data
        '''
        data_folder = self._find_data(self.data_folder_root)
        filenames = {".".join(filename.lower().split(".")[:-1]): join(data_folder, filename) for filename in listdir(data_folder)}
    
    def _find_data(self, data_root):
        ''' Work down file path to find at least one csv
        '''
        contained_files = listdir(data_root)
        if len(contained_files) == 1 and isdir(contained_files[0]):
            return self._find_data(join(data_root, contained_files[0]))
        elif any([p.lower().endswith(".csv") for p in contained_files]):
            return data_root
        elif len([d for d in contained_files if (isdir(d) and self._find_data(d) is not None)]):
            return [d for d in contained_files if (isdir(d) and self._find_data(d) is not None)][0]
        else:
            return None

    def _parse_naming_convention(self, fname):
        fname_no_ext = fname.split(".")[0] # assume no other '.'s
        forecast_name = FORECAST_NAME.findall(fname)[0]
        end_code = END_CODE.findall(fname)[0]
        scenario = fname_no_ext[len(forecast_name)+1:-(len(end_code)+1)]
        return forecast_name, scenario, end_code

    def _read_data(self, filepath, scenario, forecast_name):
        df = read_csv(filepath)
        df["scenario"] = scenario
        df["forecast_name"] = forecast_name
        return df
