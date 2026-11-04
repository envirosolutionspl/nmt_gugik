import os

from qgis.core import QgsApplication, QgsMessageLog, Qgis, QgsNetworkAccessManager
from qgis.PyQt.QtWidgets import QMessageBox, QWidget
from qgis.PyQt.QtGui import QIcon, QPalette, QPixmap
from qgis.PyQt.QtCore import QUrl, QUrlQuery, QEventLoop, Qt
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
            QMessageBox.Icon.Information,
            'Informacja',
            message,
            QMessageBox.StandardButton.Ok
        )
        msg_box.setWindowIcon(QIcon(self.plugin_icon))
        msg_box.exec()

    def pushQuestionBox(self, question) -> QMessageBox.StandardButton:
        msg_box = QMessageBox(
            QMessageBox.Icon.Question,
            'Uwaga',
            question,
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        msg_box.setWindowIcon(QIcon(self.plugin_icon))
        reply = msg_box.exec()
        return reply

    def pushMessage(self, message: str) -> None:
        self.iface.messageBar().pushMessage(
            'Informacja',
            message,
            level=Qgis.MessageLevel.Info,
            duration=10
        )

    def pushWarning(self, message: str) -> None:
        self.iface.messageBar().pushMessage(
            'Ostrzeżenie',
            message,
            level=Qgis.MessageLevel.Warning,
            duration=10
        )

    def pushCritical(self, message: str) -> None:
        self.iface.messageBar().pushMessage(
            'Błąd',
            message,
            level=Qgis.MessageLevel.Critical,
            duration=10
        )

    @staticmethod
    def pushLogInfo(message: str) -> None:
        QgsMessageLog.logMessage(message, tag=PLUGIN_NAME, level=Qgis.MessageLevel.Info)

    @staticmethod
    def pushLogWarning(message: str) -> None:
        QgsMessageLog.logMessage(message, tag=PLUGIN_NAME, level=Qgis.MessageLevel.Warning)

    @staticmethod
    def pushLogCritical(message: str) -> None:
        QgsMessageLog.logMessage(message, tag=PLUGIN_NAME, level=Qgis.MessageLevel.Critical)


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
        request.setHeader(
            QNetworkRequest.KnownHeaders.UserAgentHeader,
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
        return reply.error() == QNetworkReply.NetworkError.NoError

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


class MessageUtils:

    @staticmethod
    def pushLogWarning(message: str) -> None:
        QgsMessageLog.logMessage(
            message,
            tag=PLUGIN_NAME,
            level=Qgis.MessageLevel.Warning
        )

    @staticmethod
    def pushLogCritical(message: str) -> None:
        QgsMessageLog.logMessage(
            message,
            tag=PLUGIN_NAME,
            level=Qgis.MessageLevel.Critical
        )


class ThemeUtils:
    """Wspólne dla okien wtyczki (dock, okno wyboru branży QGIS Feed): motyw jasny/ciemny i logo."""

    PLUGIN_DIR = os.path.dirname(__file__)

    @staticmethod
    def isDarkTheme():
        """Ciemny motyw QGIS (np. Night Mapping) albo ciemna paleta systemu."""
        name = ''
        try:
            theme_name = (QgsApplication.themeName() or '').lower()
            if theme_name:
                name = theme_name
        except AttributeError as e:
            MessageUtils.pushLogCritical(f"Atrybut motywu jest niedostępny (AttributeError): {e}")
        except RuntimeError as e:
            MessageUtils.pushLogCritical(f"Aplikacja QGIS nie jest w pełni zainicjalizowana (RuntimeError): {e}")
        except TypeError as e:
            MessageUtils.pushLogCritical(f"Nieoczekiwany typ danych przy pobieraniu motywu (TypeError): {e}")
        except Exception as e:
            MessageUtils.pushLogCritical(f"Nieoczekiwany błąd: {e}")

        if 'night' in name or 'dark' in name:
            return True
        return QgsApplication.palette().color(QPalette.ColorRole.Window).lightness() < 128

    @staticmethod
    def repolishAll(window):
        """Pełne przeliczenie stylu okna i wszystkich jego widgetów (po zmianie właściwości "theme")."""
        for widget in [window] + window.findChildren(QWidget):
            widget.style().unpolish(widget)
            widget.style().polish(widget)
            widget.update()

    @staticmethod
    def setLogo(label, filename, height):
        """Wstawia logo z images/ do etykiety, w skali ekranu (bez rozpikselowania przy 125-150%)."""
        pix = QPixmap(os.path.join(ThemeUtils.PLUGIN_DIR, 'images', filename))
        if pix.isNull():
            return
        dpr = label.devicePixelRatioF()
        pix = pix.scaledToHeight(int(height * dpr), Qt.TransformationMode.SmoothTransformation)
        pix.setDevicePixelRatio(dpr)
        label.setScaledContents(False)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setPixmap(pix)
