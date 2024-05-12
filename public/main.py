
import os
import subprocess as sy
import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):


        #setting main window
        MainWindow.setObjectName("MainWindow")
        

        # main window size
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.resize(800, 600)



        # LABEL FOR LANGUAGE files --"ENTER LANGUAGE"
        self.labelLANG = QtWidgets.QLabel(self.centralwidget)
        self.labelLANG.setObjectName("labelLANG")
        self.labelLANG.setGeometry(QtCore.QRect(70, 40, 210, 23))
        font = QtGui.QFont() 
        font.setFamily("Serif") # for font-family 
        font.setPointSize(14) #font-size
        self.labelLANG.setFont(font)



        # LABEL FOR COMPILER files --"ENTER COMPILER"
        self.labelCOMPI = QtWidgets.QLabel(self.centralwidget)
        self.labelCOMPI.setObjectName("labelCOMPI")     
        self.labelCOMPI.setGeometry(QtCore.QRect(80, 110, 117, 23))
        font = QtGui.QFont()
        font.setFamily("Serif") # for font-family 
        font.setPointSize(14) #font-size
        self.labelCOMPI.setFont(font)


        
        # first drop down box 
        self.comboBoxX = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxX.setObjectName("comboBoxX")
        self.comboBoxX.setGeometry(QtCore.QRect(320, 40, 271, 31))
        self.comboBoxX.addItem("C++")
        self.comboBoxX.addItem("Java")
        font = QtGui.QFont()
        font.setPointSize(14) #font-size
        self.comboBoxX.setFont(font)



        # second drop down box 
        self.comboBoxY = QtWidgets.QComboBox(self.centralwidget)
        self.comboBoxY.setObjectName("comboBoxY")
        self.comboBoxY.setGeometry(QtCore.QRect(320, 110, 271, 31))
        self.comboBoxY.addItem("GCC")  #first entry
        self.comboBoxY.addItem("G++")   #second entry
        font = QtGui.QFont()
        font.setPointSize(14)   #font-size
        self.comboBoxY.setFont(font)
        
        # to add more items in the combo box
        # use  ==  self.comboBoxX/y.addItem("item name")



        # label named label files --"ENTER TARGETTED FILES"
        self.labelFILES = QtWidgets.QLabel(self.centralwidget)
        self.labelFILES.setObjectName("labelFILES")
        self.labelFILES.setGeometry(QtCore.QRect(80, 180, 254, 23))
        font = QtGui.QFont()
        font.setPointSize(14)   #font size
        font.setFamily("Serif")     #font family
        self.labelFILES.setFont(font)



        # textbox for files --"FILES"
        self.TextEdit_FILE = QtWidgets.QTextEdit(self.centralwidget)
        self.TextEdit_FILE.setObjectName("TextEdit_FILE")
        self.TextEdit_FILE.setGeometry(QtCore.QRect(320, 180, 391, 70))
        font = QtGui.QFont()
        font.setPointSize(14)   #font size
        self.TextEdit_FILE.setFont(font)




        # textbox for code --"Code"
        self.TextEdiT_CODE = QtWidgets.QTextEdit(self.centralwidget)
        self.TextEdiT_CODE.setObjectName("TextEdiT_CODE")
        self.TextEdiT_CODE.setGeometry(QtCore.QRect(10, 320, 781, 331))
        font = QtGui.QFont()
        font.setPointSize(14)   #font size
        self.TextEdiT_CODE.setFont(font)



        # button for copy
        self.pushButton_COP = QtWidgets.QPushButton(self.centralwidget,clicked=self.copy)
        self.pushButton_COP.setObjectName("pushButton_COP")
        self.pushButton_COP.setGeometry(QtCore.QRect(10, 270, 351, 51))
        font = QtGui.QFont()
        font.setPointSize(18)  #font size
        self.pushButton_COP.setFont(font)




        # button for generate
        self.pushButton_GEN = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_GEN.setObjectName("pushButton_GEN")
        self.pushButton_GEN.setGeometry(QtCore.QRect(440, 270, 351, 51))
        font = QtGui.QFont()
        font.setPointSize(18)   #FONT SIZE
        self.pushButton_GEN.setFont(font)



        # setting status bar and other meta data
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.menuHOME = QtWidgets.QMenu(self.menubar)
        self.menuHOME.setObjectName("menuHOME")

        self.actionRESET=QtWidgets.QAction(MainWindow)
        self.actionRESET.setObjectName("actionRESET")
        self.menuHOME.addAction(self.actionRESET)
        self.menubar.addAction(self.menuHOME.menuAction())

        self.actionchange=QtWidgets.QAction(MainWindow)
        self.actionchange.setObjectName("actionchange")
        self.menuHOME.addAction(self.actionchange)
        self.menubar.addAction(self.menuHOME.menuAction())
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
       
       
       

        # to change the textbox on choosing compilers
        self.comboBoxY.activated[str].connect(self.onChanged)  # self.onchanged is a user defined function its code is on line 171

        # connecting buttons with functions (in brackets self.<function names>)
        
        # RESET BUTTON
        self.actionRESET.triggered.connect(self.resetclicked)


        # CHANGE DIRECTORY BUTTON
        self.actionchange.triggered.connect(self.change)

        # GENERATE BUTTON
        self.pushButton_GEN.clicked.connect(self.generate)
 
       
       


        # CONNECTING BELOW FUNCTION WITH MAIN WINDOW     
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate


        # main name
        MainWindow.setWindowTitle(_translate("MainWindow", "MAKEFILE"))
        


        # label and buttons content LIKE NAME SHOWING ON SCREEN
        self.labelLANG.setText(_translate("MainWindow", "SELECT LANGUAGE:"))
        self.labelCOMPI.setText(_translate("MainWindow", "COMPILER:"))
        self.labelFILES.setText(_translate("MainWindow", "ENTER TARGET FILES:"))
        self.pushButton_COP.setText(_translate("MainWindow", "COPY"))
        self.pushButton_GEN.setText(_translate("MainWindow", "GENERATE"))
        self.menuHOME.setTitle(_translate("MainWindow","HOME"))
        self.actionRESET.setText(_translate("MainWindow","RESET"))
        self.actionRESET.setShortcut(_translate("Mainwindow","Ctrl+r"))
        self.actionchange.setText(_translate("MainWindow","CHANGE DIR"))
        self.actionchange.setShortcut(_translate("Mainwindow","Ctrl+d"))


        # The text showing on the status bar on hovering over the items
        self.comboBoxX.setStatusTip(_translate("MainWindow", "selecting language"))
        self.comboBoxY.setStatusTip(_translate("MainWindow", "selecting compiler"))
        self.TextEdit_FILE.setStatusTip(_translate("MainWindow", "files name"))
        self.pushButton_COP.setStatusTip(_translate("MainWindow", "copy to clipboard"))
        self.pushButton_GEN.setStatusTip(_translate("MainWindow", "generate the code"))
        self.actionchange.setStatusTip(_translate("Mainwindow","To change current directory directory"))
    



    # FUNCTIONS
    def change(self):
        a=os.getcwd()
        div=QtWidgets.QMessageBox()
        div.setGeometry(QtCore.QRect(800,500,1000,1000))
        div.setIcon(QtWidgets.QMessageBox.Question)
        div.setText("DO YOU WANT TO CHANGE YOUR CURRENT DIRECTORY?")
        # div.informativeText("YOUR CURRENT DIRECTORY IS :")
        div.setInformativeText("click on show details to see your current directory")
        div.setDetailedText(a)
        # div.setPlainText("hello")
        div.setStandardButtons(QtWidgets.QMessageBox.Save | QtWidgets.QMessageBox.Discard | QtWidgets.QMessageBox.Cancel)
        div.setDefaultButton(QtWidgets.QMessageBox.Save)
        div.setWindowTitle("CHANGE DIRECTORY")
        ret=div.exec_()
        #   WORKING ON THIS SECTION
        # match (ret):
        #   case QtWidgets.QMessageBox::Save:
        #   case QtWidgets.QMessageBox::Discard:
        #   case QtWidgets.QMessageBox::Cancel:
            
    # for COPY  BUTTON 
        
    def copy(self):
        cb=QtWidgets.QApplication.clipboard()
        cb.clear(mode=cb.Clipboard)
        cb.setText(self.TextEdiT_CODE.toPlainText(),mode=cb.Clipboard)
        print(cb.text())
        mess=QtWidgets.QMessageBox()
        mess.setGeometry(QtCore.QRect(800,500,1000,1000))
        mess.setIcon(QtWidgets.QMessageBox.Information)
        # QtWidgets.QMessageBox.setText(cb.text())
        mess.setText(cb.text())
        mess.setWindowTitle("CLIPBOARD")
        retval=mess.exec_()
    # for RESET BUTTON
    def resetclicked(self):
        self.TextEdiT_CODE.setPlainText("")     # SETTING THE TEXT TO NOTHING
        self.TextEdit_FILE.setPlainText("")     # SETTING THE TEXT TO NOTHING

    # FOR CHANGING CODE BOX ON CHANGING COMPILER 
    def onChanged(self):    
        self.a=self.comboBoxY.currentText()
        if self.a=="GCC":
            self.code="gcc <file name> -o <output name>"    # CODE TO SHOW ON CODE BOX
            self.TextEdiT_CODE.setText(self.code)
        if self.a=="G++":
            self.code="g++ <file name> -o <output name>"     # CODE TO SHOW ON CODE BOX
            self.TextEdiT_CODE.setText(self.code)
    
    
    # FOR GENERATE BUTTON
    def generate(self):
        x=self.TextEdit_FILE.toPlainText()   # this will contain the string which is entered in file menu
        y=x.split()  # contains list of file names seperated with whitespaces
        self.stri=""
        for i in range(len(y)):
            self.stri+=y[i]+" "
        self.a=self.comboBoxY.currentText()
        if self.a=="GCC":       #not working correct on windows
            code=f"gcc {self.stri}-o a.exe"   # code to be run on terminal
            self.TextEdiT_CODE.setText(code)  # CHANGING THE TEXT ON TEXT BOX
            os.system(self.TextEdiT_CODE.toPlainText())
            
                      # os.system(self.code)
        if self.a=="G++":
            code=f"g++ {self.stri}-o a.exe"    # code to be run on terminal
            self.TextEdiT_CODE.setText(code)
            os.system(self.TextEdiT_CODE.toPlainText())
# NO NEED TO CHANGE ANYTHING BELOW THIS FOR MODIFICATION CHANGE ABOVE CODE
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

#PyQt5 and os module using pip install <module name>