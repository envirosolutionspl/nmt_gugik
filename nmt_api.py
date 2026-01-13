from qgis.core import QgsNetworkAccessManager
from PyQt5.QtCore import QUrl, QUrlQuery, QEventLoop
from PyQt5.QtNetwork import QNetworkRequest, QNetworkReply


class NmtAPI:

    URL = "http://services.gugik.gov.pl/nmt/"

    @staticmethod
    def getRequest(PARAMS):
        url = QUrl(NmtAPI.URL)
        query = QUrlQuery()

        for key, value in PARAMS.items():
            query.addQueryItem(str(key), str(value))

        url.setQuery(query)
        request = QNetworkRequest(url)
        manager = QgsNetworkAccessManager.instance()
        reply = manager.get(request)
        loop = QEventLoop()
        reply.finished.connect(loop.quit)
        loop.exec_()

        if reply.error() == QNetworkReply.NoError:
            data = reply.readAll().data().decode("utf-8")
            reply.deleteLater()
            return data
        else:
            reply.deleteLater()
            return None

    @staticmethod
    def getHbyXY(x, y):
        PARAMS = {'request': "GetHbyXY", 'x': x, 'y': y}
        return NmtAPI.getRequest(PARAMS)



