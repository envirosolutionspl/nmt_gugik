from qgis.PyQt.QtCore import QUrl, QUrlQuery, QEventLoop
from qgis.PyQt.QtWidgets import QDialog

from .constants import NMT_SERVICE_URL
from . import PLUGIN_NAME, PLUGIN_VERSION
from .utils import QgisNetworkClient

if not hasattr(QEventLoop, 'exec'):
    QEventLoop.exec = QEventLoop.exec_

if not hasattr(QDialog, 'exec'):
    QDialog.exec = QDialog.exec_

class NmtAPI:

    URL = NMT_SERVICE_URL

    @staticmethod
    def getHbyXY(x, y, network_client: QgisNetworkClient) -> str or None:
        params = {'request': "GetHbyXY", 'x': x, 'y': y}
        return network_client.getRequest(NmtAPI.URL, params)