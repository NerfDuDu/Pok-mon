import json
from PySide6.QtWidgets import (QGraphicsView, QMainWindow, QWidget, QApplication, 
                               QHBoxLayout, QPushButton, QVBoxLayout, QLabel, QGridLayout)
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import QUrl, Slot
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkReply, QNetworkRequest

class Label_image(QLabel):
    def __init__(self, url: str, parent=None):
        super().__init__(parent)
        self.manager = QNetworkAccessManager()
        self.manager.finished.connect(self.chargement_fini)
        url = QUrl.fromUserInput(url)
        self.manager.get(QNetworkRequest(url))

    @Slot(QNetworkReply)
    def chargement_fini(self, reponse: QNetworkReply):
        image = QImage()
        image.loadFromData(reponse.readAll())
        pixmap = QPixmap.fromImage(image)
        self.setPixmap(pixmap)

class MENUS(QWidget):
    def __init__(self):
        super().__init__()

        self.layoutPrincipal = QVBoxLayout(self)

        self.layoutView = QHBoxLayout()
        self.view = QGraphicsView()
        self.layoutView.addWidget(self.view)

        self.layoutButtons = QHBoxLayout()
        self.btn_deck = QPushButton("Deck")
        self.btn_inventaire = QPushButton("Inventaire")
        self.btn_ouvrir = QPushButton("Ouvrir")

        self.layoutButtons.addWidget(self.btn_deck)
        self.layoutButtons.addWidget(self.btn_ouvrir)
        self.layoutButtons.addWidget(self.btn_inventaire)

        
        self.layoutPrincipal.addLayout(self.layoutView)
        self.layoutPrincipal.addLayout(self.layoutButtons)

class SAKA_DHO(QWidget):
    def __init__(self):
        super().__init__()

        self.layoutsakado = QVBoxLayout(self)

        #Vue
        self.vue = QWidget()
        self.gridlayout = QGridLayout()
        self.vue.setLayout(self.gridlayout)
    
        self.gridlayout.addWidget(QLabel("0,0"), 0, 0) 
        self.gridlayout.addWidget(QLabel("0,1"), 0, 1)  
        self.gridlayout.addWidget(QLabel("1,1"), 1, 1)

        self.layoutsakado.addWidget(self.vue)

        #Menu
        self.menu = QWidget()
        self.menu.setFixedHeight(40)
        self.layoutButtons = QHBoxLayout()
        self.menu.setLayout(self.layoutButtons)

        self.btn_menu = QPushButton("Menu")
        self.layoutButtons.addWidget(self.btn_menu)
        self.btn_prec = QPushButton("<")
        self.layoutButtons.addWidget(self.btn_prec)
        self.btn_suiv = QPushButton(">")
        self.layoutButtons.addWidget(self.btn_suiv)

         
        self.layoutsakado.addWidget(self.menu)  

        #self.layoutsakado.addLayout(self.layoutView)
        #self.layoutsakado.addLayout(self.layoutButtons)


        

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.menu()
    
    def menu(self):
        self.centralWidget = MENUS()
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.btn_inventaire.clicked.connect(self.inventaire)
    
    def inventaire(self):
        self.centralWidget = SAKA_DHO()
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.btn_menu.clicked.connect(self.menu)



#with open('pokedex.json', encoding="utf8") as f:
#    contenu = json.load(f)
#for i in range(15):
#    print(contenu[i]["name"]["french"])

if __name__ == "__main__":
    app = QApplication([])
    win = MyWindow()
    win.show()
    #win.resize(700, 700)
    app.exec()

#addWidget ( widget , ligne , colonne , rowSpan , columnSpan [ , alignement=Qt.Alignment() ] )
