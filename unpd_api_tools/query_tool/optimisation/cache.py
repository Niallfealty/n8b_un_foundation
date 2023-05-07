""" Cache recently downloaded results
"""

import os

class Cache:
    """ Builds and maintains a cache for downloaded data
    """

    def __init__(self, cache_location: str, expiry: float=7, overwrite: bool=False):
        ''' @cache_location -> filepath for the cache
            @expiry -> how many days before we invalidate cache
            @overwrite -> if set then force overwriting current cache data
                regardless of expiry
        '''
        self.cache_loc = cache_location
        self.ovwrt = overwrite # set for forced overwriting of cache
        self.expiry = expiry # invalidation duration in days

    def _create_cache_dir(self, force: bool=False):
        ''' create the directory for cache if not present
            throw error if already present and contains files
            unless @force is set

            runs as follows:

            try and create the dir - if it's not there we create it
            if there and empty we leave it, if not empty and not force
            we re-raise the exception
        '''
        try:
            os.mkdir(self.cache_loc)
        except FileExistsError:
            contains_files = len(os.listdir(self.cache_loc)) > 0
            if not force and contains_files:
                raise
