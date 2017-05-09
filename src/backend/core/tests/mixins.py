class HTTPMethodStatusCodeTestMixin(object):
    def run_method_status_code_check(self, url, methods, status_code):
        """
        Ensure API call to :url: will return :status_code: to request with :methods:.
        """
        for method in methods:
            response = getattr(self.client, method)(url)
            self.assertEqual(response.status_code, status_code)
