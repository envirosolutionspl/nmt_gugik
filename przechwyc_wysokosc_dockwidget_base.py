# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'przechwyc_wysokosc_dockwidget_base.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PrzechwycWysokoscDockWidgetBase(object):
    def setupUi(self, PrzechwycWysokoscDockWidgetBase):
        PrzechwycWysokoscDockWidgetBase.setObjectName("PrzechwycWysokoscDockWidgetBase")
        PrzechwycWysokoscDockWidgetBase.resize(286, 383)
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.dockWidgetContents)
        self.gridLayout.setObjectName("gridLayout")
        self.heightEdit = QtWidgets.QLineEdit(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.heightEdit.setFont(font)
        self.heightEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.heightEdit.setObjectName("heightEdit")
        self.gridLayout.addWidget(self.heightEdit, 13, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 12, 0, 1, 1)
        self.captureButton = QtWidgets.QPushButton(self.dockWidgetContents)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/plugins/przechwyc_wysokosc/icons/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.captureButton.setIcon(icon)
        self.captureButton.setObjectName("captureButton")
        self.gridLayout.addWidget(self.captureButton, 16, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.dockWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.dockWidgetContents)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 14, 0, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.dockWidgetContents)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout.addWidget(self.line_3, 9, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 10, 0, 1, 1)
        self.line_4 = QtWidgets.QFrame(self.dockWidgetContents)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 0, 0, 1, 1)
        self.copyButton = QtWidgets.QPushButton(self.dockWidgetContents)
        self.copyButton.setObjectName("copyButton")
        self.gridLayout.addWidget(self.copyButton, 15, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 18, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.dockWidgetContents)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 20, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 0, 10, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_4.setMaximumSize(QtCore.QSize(40, 40))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/plugins/przechwyc_wysokosc/icons/icon_pw.svg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lbl_email = QtWidgets.QLabel(self.dockWidgetContents)
        self.lbl_email.setTextFormat(QtCore.Qt.RichText)
        self.lbl_email.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_email.setOpenExternalLinks(True)
        self.lbl_email.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.lbl_email.setObjectName("lbl_email")
        self.gridLayout_2.addWidget(self.lbl_email, 2, 1, 1, 1)
        self.lbl_copyrights = QtWidgets.QLabel(self.dockWidgetContents)
        self.lbl_copyrights.setTextFormat(QtCore.Qt.RichText)
        self.lbl_copyrights.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_copyrights.setOpenExternalLinks(True)
        self.lbl_copyrights.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.lbl_copyrights.setObjectName("lbl_copyrights")
        self.gridLayout_2.addWidget(self.lbl_copyrights, 1, 1, 1, 1)
        self.lbl_pluginVersion = QtWidgets.QLabel(self.dockWidgetContents)
        self.lbl_pluginVersion.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_pluginVersion.setObjectName("lbl_pluginVersion")
        self.gridLayout_2.addWidget(self.lbl_pluginVersion, 0, 1, 1, 1)
        self.horizontalLayout_3.addLayout(self.gridLayout_2)
        self.label_5 = QtWidgets.QLabel(self.dockWidgetContents)
        self.label_5.setMaximumSize(QtCore.QSize(40, 40))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/plugins/przechwyc_wysokosc/icons/logo.svg"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.gridLayout.addLayout(self.horizontalLayout_3, 21, 0, 1, 1)
        self.coordsEdit = QtWidgets.QLineEdit(self.dockWidgetContents)
        self.coordsEdit.setEnabled(True)
        self.coordsEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.coordsEdit.setObjectName("coordsEdit")
        self.gridLayout.addWidget(self.coordsEdit, 11, 0, 1, 1)
        PrzechwycWysokoscDockWidgetBase.setWidget(self.dockWidgetContents)

        self.retranslateUi(PrzechwycWysokoscDockWidgetBase)
        QtCore.QMetaObject.connectSlotsByName(PrzechwycWysokoscDockWidgetBase)

    def retranslateUi(self, PrzechwycWysokoscDockWidgetBase):
        _translate = QtCore.QCoreApplication.translate
        PrzechwycWysokoscDockWidgetBase.setWindowTitle(_translate("PrzechwycWysokoscDockWidgetBase", "Przechwyć Wysokość GUGiK NMT API"))
        self.label_3.setText(_translate("PrzechwycWysokoscDockWidgetBase", "Wysokość:"))
        self.captureButton.setText(_translate("PrzechwycWysokoscDockWidgetBase", "Przechwytuj"))
        self.label.setText(_translate("PrzechwycWysokoscDockWidgetBase", "<html><head/><body><p align=\"center\">Wtyczka pozwala<br/>na sprawdzenie wysokości terenu<br/>na podstawie API NMT<br/>udostępnianego przez GUGiK.</p></body></html>"))
        self.label_2.setText(_translate("PrzechwycWysokoscDockWidgetBase", "Współrzędne:"))
        self.copyButton.setText(_translate("PrzechwycWysokoscDockWidgetBase", "Kopiuj do schowka"))
        self.lbl_email.setText(_translate("PrzechwycWysokoscDockWidgetBase", "<html><head/><body><p><a href=\"mailto:office@envirosolutions.pl\"><span style=\" text-decoration: underline; color:#0000ff;\">ZAPRASZAMY DO WSPÓŁPRACY</span></a></p></body></html>"))
        self.lbl_copyrights.setText(_translate("PrzechwycWysokoscDockWidgetBase", "<html><head/><body><p>© 2024 <a href=\"http://www.envirosolutions.pl/\"><span style=\" text-decoration: underline; color:#0000ff;\">EnviroSolutions Sp. z o.o.</span></a></p></body></html>"))
        self.lbl_pluginVersion.setText(_translate("PrzechwycWysokoscDockWidgetBase", "Przechwyć Wysokość 1.0"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PrzechwycWysokoscDockWidgetBase = QtWidgets.QDockWidget()
    ui = Ui_PrzechwycWysokoscDockWidgetBase()
    ui.setupUi(PrzechwycWysokoscDockWidgetBase)
    PrzechwycWysokoscDockWidgetBase.show()
    sys.exit(app.exec_())
