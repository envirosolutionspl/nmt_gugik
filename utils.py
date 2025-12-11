from .constants import QT_VER


def isCompatibleQtVersion(cur_version, tar_version):
    return cur_version.startswith(QT_VER[tar_version])