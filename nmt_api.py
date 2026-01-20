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
    def buildUrl(params):
        url = QUrl(NmtAPI.URL)
        query = QUrlQuery()
        for key, value in params.items():
            query.addQueryItem(str(key), str(value))
        url.setQuery(query)
        return url

    @staticmethod
    def buildRequest(url):
        request = QNetworkRequest(url)
        if hasattr(QNetworkRequest, 'KnownHeaders'):
            ua_header = QNetworkRequest.KnownHeaders.UserAgentHeader  # Qt6
        else:
            ua_header = QNetworkRequest.UserAgentHeader  # Qt5
        request.setHeader(
            ua_header, f"QGIS-Plugin-{PLUGIN_NAME}"
        )
        return request

    @staticmethod
    def sendRequest(request):
        manager = QgsNetworkAccessManager.instance()
        reply = manager.get(request)
        loop = QEventLoop()
        reply.finished.connect(loop.quit)
        loop.exec()
        return reply

    @staticmethod
    def isSuccess(reply):
        error_val = reply.error()
        if hasattr(QNetworkReply, 'NetworkError'):
            no_err = QNetworkReply.NetworkError.NoError  # Qt6
        else:
            no_err = QNetworkReply.NoError  # Qt5
        return error_val == no_err

    @staticmethod
    def readReply(reply):
        data = reply.readAll().data().decode("utf-8")
        reply.deleteLater()
        return data

    @staticmethod
    def getRequest(params):
        url = NmtAPI.buildUrl(params)
        request = NmtAPI.buildRequest(url)
        reply = NmtAPI.sendRequest(request)
        if NmtAPI.isSuccess(reply):
            return NmtAPI.readReply(reply)
        reply.deleteLater()
        return None

    @staticmethod
    def getHbyXY(x, y):
        params = {'request': "GetHbyXY", 'x': x, 'y': y}
        return NmtAPI.getRequest(params)