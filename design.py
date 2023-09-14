# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(784, 663)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAutoFillBackground(True)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.input_text = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.input_text.setMinimumSize(QtCore.QSize(500, 0))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.input_text.setFont(font)
        self.input_text.setStyleSheet("")
        self.input_text.setObjectName("input_text")
        self.verticalLayout.addWidget(self.input_text)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.phrases = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.phrases.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(10)
        self.phrases.setFont(font)
        self.phrases.setObjectName("phrases")
        self.verticalLayout_2.addWidget(self.phrases)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.restults = QtWidgets.QLabel(self.centralwidget)
        self.restults.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.restults.setFont(font)
        self.restults.setObjectName("restults")
        self.verticalLayout_3.addWidget(self.restults)
        self.btn_go = QtWidgets.QPushButton(self.centralwidget)
        self.btn_go.setObjectName("btn_go")
        self.verticalLayout_3.addWidget(self.btn_go)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Input text"))
        self.input_text.setPlainText(_translate("MainWindow", "In today\'s meeting, we discussed a variety of issues affecting our department. The weather was unusually sunny, a pleasant backdrop to our serious discussions. We came to the consensus that we need to do better in terms of performance. Sally brought doughnuts, which lightened the mood. It\'s important to make good use of what we have at our disposal. During the coffee break, we talked about the upcoming company picnic. We should aim to be more efficient and look for ways to be more creative in our daily tasks. Growth is essential for our future, but equally important is building strong relationships with our team members. As a reminder, the annual staff survey is due next Friday. Lastly, we agreed that we must take time to look over our plans carefully and consider all angles before moving forward. On a side note, David mentioned that his cat is recovering well from surgery."))
        self.label_2.setText(_translate("MainWindow", "Add phrase"))
        self.phrases.setPlainText(_translate("MainWindow", "Optimal performance\n"
"Utilize resources\n"
"Enhance productivity\n"
"Conduct an analysis\n"
"Maintain a high standard\n"
"Implement best practices\n"
"Ensure compliance\n"
"Streamline operations\n"
"Foster innovation\n"
"Drive growth\n"
"Leverage synergies\n"
"Demonstrate leadership\n"
"Exercise due diligence\n"
"Maximize stakeholder value\n"
"Prioritise tasks\n"
"Facilitate collaboration\n"
"Monitor performance metrics\n"
"Execute strategies\n"
"Gauge effectiveness\n"
"Champion change"))
        self.restults.setText(_translate("MainWindow", "Results"))
        self.btn_go.setText(_translate("MainWindow", "Go"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
