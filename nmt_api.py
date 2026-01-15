from qgis.core import QgsNetworkAccessManager
from qgis.PyQt.QtCore import QUrl, QUrlQuery, QEventLoop
from qgis.PyQt.QtNetwork import QNetworkRequest, QNetworkReply
from qgis.PyQt.QtWidgets import QDialog
from .constants import NMT_SERVICE_URL

if not hasattr(QEventLoop, 'exec'):
    QEventLoop.exec = QEventLoop.exec_

if not hasattr(QDialog, 'exec'):
    QDialog.exec = QDialog.exec_

class NmtAPI:

    URL = NMT_SERVICE_URL

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
        loop.exec()

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



