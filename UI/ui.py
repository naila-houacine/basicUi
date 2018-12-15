from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import QtCore


import main
listperiod=["العصر العباسي", "العصر الاسلامي","العصر الجاهلي","العصر الاموي","العصر  الحديث"]
listgenre=["دين","سياسة","أدب"]

class MyFileBrowser(main.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self, maya=False):
        super(MyFileBrowser, self).__init__()
        self.setupUi(self)
        self.maya = maya
        self.treeView.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeView.customContextMenuRequested.connect(self.context_menu)
        self.populate()
        self.fill_choice_box_genre(listgenre)
        self.fill_choice_box_period(listperiod)
        #listener for combo box
        self.genre.currentTextChanged.connect(self.get_genre_selected)
        self.period.currentTextChanged.connect(self.get_period_selected)
        #text of word selected
        #self.wordtext.textChanged.connect(self.get_text_word)
        self.checkword.clicked.connect(self.get_text_word)
        self.insertmeaning.clicked.connect(self.insertintomeanings)
        self.insertexample.clicked.connect(self.insertintoexamples)

    def insertintoexamples(self):
        examplesadded=self.modifyexample.text()

        numRows = self.exampleslist.rowCount()
        self.exampleslist.insertRow(numRows)

        self.exampleslist.setItem(numRows, 0, QtWidgets.QTableWidgetItem("Modify"))
        self.exampleslist.setItem(numRows, 1, QtWidgets.QTableWidgetItem("SUPP"))
        self.exampleslist.setItem(numRows, 2, QtWidgets.QTableWidgetItem(str(examplesadded)))



    def insertintomeanings(self):
        meaningadded=self.editmeaning.text()
        print("meaning:added",meaningadded)


        numRows = self.listmeaning.rowCount()
        self.listmeaning.insertRow(numRows)

        self.listmeaning.setItem(numRows, 0, QtWidgets.QTableWidgetItem("Modify"))
        self.listmeaning.setItem(numRows, 1, QtWidgets.QTableWidgetItem("SUPP"))
        self.listmeaning.setItem(numRows, 2, QtWidgets.QTableWidgetItem(str(meaningadded)))
        #numRows = self.listmeaning.rowCount()


    def populate(self):
        path = r"/home/masterubunto/M2_gitprojects/historical_dictionary-/data/corpus"
        self.model = QtWidgets.QFileSystemModel()
        self.model.setRootPath((QtCore.QDir.rootPath()))
        self.treeView.setModel(self.model)
        self.treeView.setRootIndex(self.model.index(path))
        self.treeView.setSortingEnabled(True)

    def context_menu(self):
        menu = QtWidgets.QMenu()
        open = menu.addAction("عرض النص")
        open.triggered.connect(self.open_file)


        cursor = QtGui.QCursor()
        menu.exec_(cursor.pos())

    def open_file(self):
        index = self.treeView.currentIndex()
       
        file_path = self.model.filePath(index)

        entries = open(file_path,"r").readlines()

        model = QtGui.QStandardItemModel()
        self.listView.setModel(model)

        for i in range(0,len(entries)-1):
            item = QtGui.QStandardItem(entries[i])
            model.appendRow(item)

    def fill_choice_box_period(self,listp):

            self.period.addItems(listp)

    def fill_choice_box_genre(self, listg):
        self.genre.addItems(listg)

    def get_genre_selected(self):

        print("changed",self.genre.currentText())
        return self.genre.currentText()
    def get_period_selected(self):
        print("changed", self.period.currentText())
        return self.period.currentText()




    def lanch_search(self,word,genre,period):

        meanings=["blue","hi"]
        examples=["blueblack","la vie","est","belle"]
        #appell fonction de xmlmanagement

        numRows = 0
        self.listmeaning.setRowCount(0)
        #self.listmeaning.insertRow(numRows)
        self.listmeaning.setColumnCount(3)

        # Create a empty row at bottom of table


        for item in meanings:
            self.listmeaning.insertRow(numRows)
            self.listmeaning.setItem(numRows, 0, QtWidgets.QTableWidgetItem("Modify"))
            self.listmeaning.setItem(numRows, 1, QtWidgets.QTableWidgetItem("SUPP"))
            self.listmeaning.setItem(numRows, 2, QtWidgets.QTableWidgetItem(item))
            numRows = self.listmeaning.rowCount()



        #examples
       # numRows=0
        self.exampleslist.setRowCount(0);
        self.exampleslist.setColumnCount(3)

        # Create a empty row at bottom of table

        for item in examples:
            self.exampleslist.insertRow(numRows)
            self.exampleslist.setItem(numRows, 0, QtWidgets.QTableWidgetItem("Modify"))
            self.exampleslist.setItem(numRows, 1, QtWidgets.QTableWidgetItem("SUPP"))
            self.exampleslist.setItem(numRows, 2, QtWidgets.QTableWidgetItem(item))
            numRows = self.exampleslist.rowCount()


    def get_text_word(self):
        self.lanch_search(self.wordtext.toPlainText(),self.get_genre_selected(),self.get_period_selected())
        self.checkword.setChecked(0)
        return self.wordtext.toPlainText()



if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    fb = MyFileBrowser()
    fb.show()
app.exec_()