from qgis.core import QgsNetworkAccessManager
from qgis.PyQt.QtCore import QUrl, QUrlQuery, QEventLoop
from qgis.PyQt.QtNetwork import QNetworkRequest, QNetworkReply
from qgis.PyQt.QtWidgets import QDialog
from .constants import NMT_SERVICE_URL
from . import PLUGIN_NAME, PLUGIN_VERSION

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
        if hasattr(QNetworkRequest, 'KnownHeaders'):
            ua_header = QNetworkRequest.KnownHeaders.UserAgentHeader
        else:
            ua_header = QNetworkRequest.UserAgentHeader
        request.setHeader(
             ua_header, f"QGIS-Plugin-{PLUGIN_NAME}"
        )
        
        manager = QgsNetworkAccessManager.instance()
        reply = manager.get(request)
        loop = QEventLoop()
        reply.finished.connect(loop.quit)
        loop.exec()
        error_val = reply.error()
        if hasattr(QNetworkReply, 'NetworkError'):
            no_err = QNetworkReply.NetworkError.NoError  # Qt6
        else:
            no_err = QNetworkReply.NoError  # Qt5
        if error_val == no_err:
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



