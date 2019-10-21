import requests


class NmtAPI:

    URL = "http://services.gugik.gov.pl/nmt/"

    def getRequest(PARAMS):
        try:
            r = requests.get(url=NmtAPI.URL, params=PARAMS)
        except requests.exceptions.ConnectionError:
            return None
        r_txt = r.text
        if r.status_code == 200:
            return r_txt
        else:
            return None

    def getHbyXY(x, y):
        PARAMS = {'request': "GetHbyXY", 'x': x, 'y': y}
        return NmtAPI.getRequest(PARAMS)



