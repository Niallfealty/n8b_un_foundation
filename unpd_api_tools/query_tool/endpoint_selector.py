""" A simple class definition to allow endpoint selecting
"""

class UrlFormattingException(ValueError):
    pass

class ApiEndpointSelector:
    """ A bit of code around some text formatting to cleanly
        generate api endpoint urls. We assume the api is fixed
        and allow for changes in the base url (which we append to)

        @base_url the url for the api
        @allow_http allow connections over http when connecting to api
    """
    def __init__(self, base_url, allow_http=False):
        self.base_url = self._format_base_url(base_url)
        self._allow_http = allow_http

    def _format_base_url(self, base_url):
        ''' Validate/correct formatting for base url
        '''
        if base_url.startswith("https://") or \
            (self._allow_http and base_url.startswith("http://")):
                return base_url[:-1] if base_url.endswith("/") else base_url
        else:
            raise UrlFormattingException("base_url is not properly formatted, protocol specifier required!")

    def _append(self, endpoint):
        ''' Append endpoint to base url ensuring we don't double count slashes
        '''
        endpoint_formatted = endpoint[1:] if endpoint.startswith("/") else endpoint
        return f"{self.base_url}/{endpoint}"

    @property
    def indicators(self):
        return self._append("Indicators")

def unit_test():
    test_api = "https://test.api.un.org"
    test_endpoint = "https://test.api.un.org/Indicators"
    selector = ApiEndpointSelector(test_api)
    result = "+" if selector.indicators == test_endpoint else "-"
    print(f"[{result}] {selector.indicators}")

if __name__ == "__main__":
    unit_test()
