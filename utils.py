from qgis._core import QgsMessageLog, Qgis, QgsNetworkAccessManager
from qgis.PyQt.QtWidgets import QMessageBox
from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtCore import QUrl, QUrlQuery, QEventLoop
from qgis.PyQt.QtNetwork import QNetworkRequest, QNetworkReply

from .constants import PLUGIN_ICON, QT_VER
from . import PLUGIN_NAME

class QgsTools:

    default_tag = PLUGIN_NAME
    plugin_icon = PLUGIN_ICON

    def __init__(self, iface):
        self.iface = iface

    def pushMessageBox(self, message):
        msg_box = QMessageBox(
            QMessageBox.Information,
            'Informacja',
            message,
            QMessageBox.StandardButton.Ok
        )
        msg_box.setWindowIcon(QIcon(self.plugin_icon))
        msg_box.exec()

    def pushQuestionBox(self, question) -> QMessageBox.StandardButton:
        msg_box = QMessageBox(
            QMessageBox.Question,
            'Uwaga',
            question,
            QMessageBox.Yes or QMessageBox.No
        )
        msg_box.setWindowIcon(QIcon(self.plugin_icon))
        reply = msg_box.exec()
        return reply
    
    def pushMessage(self, message: str) -> None:
        self.iface.messageBar().pushMessage(
            'Informacja',
            message,
            level=Qgis.Info,
            duration=10
        )

    def pushWarning(self, message: str) -> None:
        self.iface.messageBar().pushMessage(
            'Ostrzeżenie',
            message,
            level=Qgis.Warning,
            duration=10
        )

    def pushCritical(self, message: str) -> None:
        self.iface.messageBar().pushMessage(
            'Błąd',
            message,
            level=Qgis.Critical,
            duration=10
        )
    @staticmethod
    def pushLogInfo(message: str) -> None:
        QgsMessageLog.logMessage(message, tag=PLUGIN_NAME, level=Qgis.Info)

    @staticmethod
    def pushLogWarning(message: str) -> None:
        QgsMessageLog.logMessage(message, tag=PLUGIN_NAME, level=Qgis.Warning)

    @staticmethod
    def pushLogCritical(message: str) -> None:
        QgsMessageLog.logMessage(message, tag=PLUGIN_NAME, level=Qgis.Critical)

class QgisNetworkClient:
    """
    Klasa pomocnicza do obsługi zapytań HTTP w środowisku QGIS / Qt.
    Niezależna od konkretnego API.
    """
    def __init__(self):
        self.manager = QgsNetworkAccessManager.instance()

    def buildUrl(self, base_url: str, params: dict) -> QUrl:
        url = QUrl(base_url)
        query = QUrlQuery()
        for key, value in params.items():
            query.addQueryItem(str(key), str(value))
        url.setQuery(query)
        return url

    def buildRequest(self, url: QUrl) -> QNetworkRequest:
        request = QNetworkRequest(url)
        if hasattr(QNetworkRequest, 'KnownHeaders'):
            ua_header = QNetworkRequest.KnownHeaders.UserAgentHeader  # Qt6
        else:
            ua_header = QNetworkRequest.UserAgentHeader  # Qt5
        request.setHeader(
            ua_header, 
            f"QGIS-Plugin-{PLUGIN_NAME}"
        )
        return request

    def sendRequest(self, request: QNetworkRequest) -> QNetworkReply:
        reply = self.manager.get(request)
        loop = QEventLoop()
        reply.finished.connect(loop.quit)
        loop.exec()
        return reply

    def isSuccess(self, reply: QNetworkReply) -> bool:
        if hasattr(QNetworkReply, 'NetworkError'):
            no_err = QNetworkReply.NetworkError.NoError  # Qt6
        else:
            no_err = QNetworkReply.NoError  # Qt5
        return reply.error() == no_err

    def readReply(self, reply: QNetworkReply) -> str:
        data = reply.readAll().data().decode("utf-8")
        reply.deleteLater()
        return data
    
    def getRequest(self, base_url: str, params: dict) -> str or None:
        url = self.buildUrl(base_url, params)
        request = self.buildRequest(url)
        reply = self.sendRequest(request)
        if self.isSuccess(reply):
            return self.readReply(reply)
        reply.deleteLater()
        return None

def isCompatibleQtVersion(cur_version, tar_version):
    return cur_version.startswith(QT_VER[tar_version])