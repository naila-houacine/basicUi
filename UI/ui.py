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

        meanings=["blue","hi","honey","cool","k"]
        examples=["la vie","est","belle"]
        #appell fonction de xmlmanagement
        model = QtGui.QStandardItemModel()
        self.listmeaning.setModel(model)

        for i in meanings:
            item = QtGui.QStandardItem(i)
            model.appendRow(item)

        model = QtGui.QStandardItemModel()
        self.tableView.setModel(model)

        for i in examples:
            item = QtGui.QStandardItem(i)
            model.appendRow(item)

    def get_text_word(self):
        self.lanch_search(self.wordtext.toPlainText(),self.get_genre_selected(),self.get_period_selected())
        self.checkword.setChecked(0)
        return self.wordtext.toPlainText()



if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    fb = MyFileBrowser()
    fb.show()
app.exec_()