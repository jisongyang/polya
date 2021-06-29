from sys import exit,argv
import sys, os
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QFont,QPixmap
from mainwindow import *
from polya import Polyhedron



class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.calculate.clicked.connect(self.start_calculate)
        self.r_num.setFont(QFont("Calibri", 12))
        self.b_num.setFont(QFont("Calibri", 12))
        self.w_num.setFont(QFont("Calibri", 12))
        self.color_num.setFont(QFont("Calibri", 12))
        self.result.setFont(QFont("Calibri", 12))
        self.member.setToolTip('yangjisong')
        self.function_descrip.setToolTip('模式一：红蓝白三种颜色之和应该等于染色目标的个数。红色和蓝色必须有值，白色可以缺省。\n'
                                         '模式二：总颜色数表示可以用的颜色数，每一次染色不一定用完所有颜色。')
        self.develop_info.setToolTip('基于python的pyqt、sympy包开发')
        self.radioButton.setChecked(True)

        self.name_select.addItems(['正四面体','正六面体','正八面体'])
        self.name_select.setStyleSheet('QComboBox QAbstractItemView::item {height:50px;}')
        self.name_select.currentTextChanged.connect(self.show_attr)

        self.aim_select.addItems(['顶点','棱','面'])
        self.aim_select.setStyleSheet('QComboBox QAbstractItemView::item {height:50px;}')
        self.aim_select.currentTextChanged.connect(self.set_color_info)

        self.show_attr()
        self.set_color_info()

    def show_attr(self):
        self.name=self.name_select.currentText()
        self.aim=self.aim_select.currentText()
        self.polyhedrom=Polyhedron(self.name,self.aim)
        self.info=self.polyhedrom.get_info()

        picture='picture\\tetrahedro.jpg'
        if(self.name_select.currentText()=='正四面体'):
            picture='picture\\tetrahedro.jpg'
        if(self.name_select.currentText()=='正六面体'):
            picture='picture\\hexahedro.jpg'
        if(self.name_select.currentText()=='正八面体'):
            picture='picture\\octahedro.jpg'
        self.show_hexahedro(picture)

        self.vertice_num.setText(str(self.info[0])+'个顶点')
        self.edge_num.setText(str(self.info[1]) + '条棱')
        self.surface_num.setText(str(self.info[2]) + '个面')

    def show_hexahedro(self,picture):
        pix=QPixmap(picture)
        self.picture.setPixmap(pix)
        self.picture.setScaledContents(True)

    def set_color_info(self):
        self.name=self.name_select.currentText()
        self.aim=self.aim_select.currentText()
        self.polyhedrom=Polyhedron(self.name,self.aim)
        self.info=self.polyhedrom.get_info()
        self.vertice_num.setStyleSheet('border: 1px solid rgba(0,0,0,0.5);background-color: rgba(202,255,112,0);')
        self.edge_num.setStyleSheet('border: 1px solid rgba(0,0,0,0.5);background-color: rgba(202,255,112,0);')
        self.surface_num.setStyleSheet('border: 1px solid rgba(0,0,0,0.5);background-color: rgba(202,255,112,0);')
        if(self.aim_select.currentText()=='顶点'):
            self.vertice_num.setStyleSheet('border: 4px solid rgba(0,0,0,0.5);background-color: rgba(202,255,112,0);')
        if(self.aim_select.currentText()=='棱'):
            self.edge_num.setStyleSheet('border: 4px solid rgba(0,0,0,0.5);background-color: rgba(202,255,112,0);')
        if(self.aim_select.currentText()=='面'):
            self.surface_num.setStyleSheet('border: 4px solid rgba(0,0,0,0.5);background-color: rgba(202,255,112,0);')





    def start_calculate(self):
        if(self.radioButton.isChecked()):
            r = self.r_num.toPlainText()
            b = self.b_num.toPlainText()
            w = self.w_num.toPlainText()
            if (r != '' and b != '' and r.isdigit() and b.isdigit()):
                if (w == ''):
                    w = self.polyhedrom.object_num - int(r) - int(b)
                    result = self.polyhedrom.get_rbw_kinds(int(r), int(b))
                    self.result.setText('红（{}）蓝（{}）白（{}）的染色数：'.format(r, b, w) + str(result))
                elif (w != '' and self.polyhedrom.object_num==int(r)+int(b)+int(w)):
                    result = self.polyhedrom.get_rbw_kinds(int(r), int(b), int(w))
                    self.result.setText('红（{}）蓝（{}）白（{}）的染色数：'.format(r, b, w) + str(result))
                else:
                    self.result.setText('参数错误：三种颜色之和不正确')
            else:
                self.result.setText('参数错误：检查模式和颜色设置')

        if(self.radioButton_2.isChecked()):
            color = self.color_num.toPlainText()
            if(color!='' and color.isdigit()):
                result=self.polyhedrom.get_all_kinds_by_color(int(color))
                self.result.setText('使用{}种颜色的染色数：'.format(color)+str(result))
            else:
                self.result.setText('参数错误：检查模式和颜色设置')





if __name__ == '__main__':

    app = QApplication(argv)
    myWin = MyWindow()
    myWin.setWindowTitle('多面体染色计数')
    myWin.show()
    exit(app.exec_())