from functions import Functions
from methods import GoldenRatio, PassiveSearch, findSection
import os
import sys

os.system('''pyside6-rcc res.qrc -o res_rc.py
pyside6-uic MainWindow.ui > ui_mainwindow.py'''.replace('\n', '&'))

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtGui import QPixmap

from ui_mainwindow import Ui_MainWindow

# def findSection(x0, h, funcNum):
#     Function = Functions(funcNum)
#     k = 1
#     a, b = 0, 0
#     Fx_k_1 = Function(x0)
#     Fx_k = Function(x0+h)
#     if Fx_k_1 > Fx_k:
#         a = x0
#         # k = 2
#         while Fx_k_1 > Fx_k:
#             k += 1
#             Fx_k_1 = Fx_k
#             Fx_k = Function(x0 + 2**(k-1)*h)
            
#         if h > 0: 
#             b = x0 + 2**(k-1)*h
#         else:
#             a = x0 + 2**(k-1)*h

#     else:
#         Fx_k = Function(x0-h)
#         Fx_k_1 = Function(x0)
#         if Fx_k >= Fx_k_1:
#             a = x0-h
#             b = x0+h
#             return a,b
#         else:
#             b = x0
#             Fx_k = Function(x0-h)
            
#             h = -h

#     return a, b


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.sectionBtn.setEnabled(False)
        self.ui.solveGolden.setEnabled(False)
        self.ui.solvePassiveSearch.setEnabled(False)

        self.ui.sectionBtn.clicked.connect(self.findSectionLine)
        self.ui.solveGolden.clicked.connect(self.solveWithGolden)
        self.ui.solvePassiveSearch.clicked.connect(self.seolveWithPassive)

        self.sectionvalue1 = ''
        self.ui.sectionLine.textChanged.connect(self.lineIsChanged)
        self.ui.Nvalue.valueChanged.connect(self.lineIsChanged)
        self.ui.epsValue.valueChanged.connect(self.lineIsChanged)



        self.examples = [self.ui.Example1,self.ui.Example2,self.ui.Example3,self.ui.Example4,self.ui.Example5,self.ui.Example6]
        for el in self.examples:
            el.clicked.connect(self.defineCheckedButton)
        self.neededPng = 0
        self.globalA = 0
        self.globalB = 0 

        # code
        self.show()

    def lineIsChanged(self):
        print('adqwd')
        if self.ui.Nvalue.value() != 0 and self.ui.sectionLine.text() != '':
            self.ui.solvePassiveSearch.setEnabled(True)
        else:
            self.ui.solvePassiveSearch.setEnabled(False)
        
        if self.ui.epsValue.value() != 0 and self.ui.sectionLine.text() != '':
            self.ui.solveGolden.setEnabled(True)
        else:
            self.ui.solveGolden.setEnabled(False)

    def defineCheckedButton(self):
        for el in self.examples:
            if el.isChecked():
                self.neededPng = el.text()[0]
                self.ui.ExamplePicture.setPixmap(QPixmap(os.getcwd()+f"\src\{self.neededPng}.jpg"))
                self.ui.sectionBtn.setEnabled(True)
                return

    def findSectionLine(self):
        self.globalA, self.globalB = findSection(self.ui.XNull.value(), self.ui.Step.value(), int(self.neededPng))
        if self.globalA == 'bad' and self.globalB == 'param':
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Warning)
            msgBox.setText("Недопустимое значение аргумента")
            msgBox.setWindowTitle("Ошибка данных")
            msgBox.setStandardButtons(QMessageBox.Ok)
            self.ui.sectionLine.setText("")
            returnValue = msgBox.exec()

            return
        self.ui.sectionLine.setText(f"[{self.globalA};{self.globalB}]")

        # Если изменены N и e
        # self.ui.solveGolden.setEnabled(True)
        # self.ui.solvePassiveSearch.setEnabled(True)
        # print(a, b)

    def seolveWithPassive(self):
        N = self.ui.Nvalue.value()
        # GoldenRatio(self.globalA, self.globalB, e, func)
        x = PassiveSearch(self.globalA, self.globalB, N, Functions(int(self.neededPng)))
        print(x)
        self.ui.xPassive.setText(str(round(x,4)))
        pass

    def solveWithGolden(self):
        eps = self.ui.epsValue.value()
        x = GoldenRatio(self.globalA, self.globalB, eps, Functions(int(self.neededPng)))
        print(round(x, 4))
        self.ui.xGolden.setText(str(round(x, 4)))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec())
