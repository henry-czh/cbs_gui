# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connect_me.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
#导入程序运行必须模块
import sys
#PyQt5中使用的基本控件都在PyQt5.QtWidgets模块中
#from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
#导入designer工具生成的login模块
from cbs_release import Ui_MainWindow
#import genDesignTree
from xml2tree import genDesignTree


class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        #self.pushButton.clicked.connect(self.click_success)
        self.mdiArea.addSubWindow(self.Benchmark)
        self.mdiArea.addSubWindow(self.Configuration)
        #self.Configuration.show()
        #self.actionConfiguration.triggered.connect(self.mdiArea.showNormal)
        self.designTree=genDesignTree()
        def showDesignTree(self):
            self.design_tree.show()

        self.model=QStandardItemModel(2,0,self)
        #self.model.setHorizontalHeaderLabels(0,QStandardItem('Unit'))
        #self.model.setHorizontalHeaderLabels(1,QStandardItem('Unit'))
        self.model.setHorizontalHeaderItem(0,QStandardItem('S5000'))
        #self.model.setHorizontalHeaderItem(1,QStandardItem('Comment'))
        #self.tableView.setModel(self.model)
        self.design_tree.setModel(self.model)

        top_item=QStandardItem('S5000')

        self.pushButton_4.clicked.connect(self.click_display)
        #self.textBrowser.setText("%d" % self.design_tree.setCurrentIndex)
        #self.design_tree.on_treeview_clicked()

        def build_design_tree(item,dt_dict):
            for i in dt_dict.keys():
                sub_item = QStandardItem(i)
                sub_item.setIcon(QIcon("./device_and_hardware.ico"))
                sub_item.setData("D")
                sub_item.setCheckable(Qt.Checked)
                item.appendRow(sub_item)
                #item.appendColumn(item,sub_item)
                #item.setChild(0,1,QStandardItem(i))
                if dt_dict[i]=={}:
                    print (dt_dict[i])
                    continue
                else:
                    print (dt_dict[i])
                    if type(dt_dict[i])==dict:
                        build_design_tree(sub_item,dt_dict[i])
            return item
        self.model.setItem(0,0,build_design_tree(top_item,self.designTree))

    def click_display(self):
        self.currentIndex=self.design_tree.currentIndex()
        self.currentItem=self.model.itemFromIndex(self.currentIndex)
        self.currentItem.setForeground(QBrush(Qt.red))
        text = self.currentItem.text()
        data = self.currentItem.data()
        print (data)
        print (self.currentIndex)
        print (self.currentItem)
        self.textBrowser.setText(text+data)
        self.statusbar.showMessage(text+" : "+data)

    def click_success(self):
        print ("hello world!!!")
        self.textBrowser.setText("hello world!!!")
        QMessageBox.information(self,"Error","hello world!!!")

if __name__ == "__main__":
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)

    #固定的，PyQt5程序都需要QApplication对象。sys.argv是命令行参数列表，确保程序可以双击运行
    app = QApplication(sys.argv)
    #初始化
    myWin = MyMainForm()
    #将窗口控件显示在屏幕上
    myWin.show()
    #程序运行，sys.exit方法确保程序完整退出。
    sys.exit(app.exec_())
