from qgis._core import QgsMessageLog, Qgis
from qgis.PyQt.QtWidgets import QMessageBox
from qgis.PyQt.QtGui import QIcon

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
        QgsMessageLog.logMessage(message, tag=QgsTools.default_tag, level=Qgis.Info)

    @staticmethod
    def pushLogWarning(message: str) -> None:
        QgsMessageLog.logMessage(message, tag=QgsTools.default_tag, level=Qgis.Warning)

    @staticmethod
    def pushLogCritical(message: str) -> None:
        QgsMessageLog.logMessage(message, tag=QgsTools.default_tag, level=Qgis.Critical)


def isCompatibleQtVersion(cur_version, tar_version):
    return cur_version.startswith(QT_VER[tar_version])