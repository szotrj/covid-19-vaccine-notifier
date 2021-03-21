import urllib3

class HttpRequest:
    user_agent = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36 Edg/89.0.774.48"
    }

    @classmethod
    def get(cls, url, headers={}):
        headers.update(cls.user_agent)
        http = urllib3.PoolManager()
        resp = http.request('GET', url, headers=headers)

        return resp

    @classmethod
    def post(cls, url, headers={}, body=''):
        headers.update(cls.user_agent)
        http = urllib3.PoolManager()
        resp = http.post('POST', url, headers=headers, body=body)

        return resp