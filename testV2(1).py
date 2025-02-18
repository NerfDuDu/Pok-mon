import json
from PySide6.QtWidgets import (QGraphicsView, QMainWindow, QWidget, QApplication, 
                               QHBoxLayout, QPushButton, QVBoxLayout, QLabel, 
                               QGraphicsScene, QGraphicsPixmapItem, QGraphicsRectItem)
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtCore import QUrl, Slot, QRandomGenerator, Signal,Qt
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkReply, QNetworkRequest

class Scene(QGraphicsScene):
    
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.fond=QGraphicsRectItem(0,0,0,0)
        self.addItem(self.fond)
        self.ajoute(self.imge())

    def imge(self):
        with open('pokedex.json', encoding="utf8") as f:
            contenu = json.load(f)
        pokemon = contenu[51]["image"]["thumbnail"]
        self.fond()
        return pokemon
        

    def ajoute(self,url: str):
        self.manager = QNetworkAccessManager()
        self.manager.finished.connect(self.chargement_fini)
        url = QUrl.fromUserInput(url)
        self.manager.get(QNetworkRequest(url))
        

    def get_type(self):
        with open('pokedex.json', encoding="utf8") as f:
            contenu = json.load(f)
        pokemon_type = contenu[51]["type"]
        return pokemon_type
    def get_nom(self):
        with open('pokedex.json', encoding="utf8") as f:
            contenu = json.load(f)
        nom_pokemon = contenu[51]["name"]["french"]
        return nom_pokemon
    
    def fond(self):
        type = Scene.get_type(self)
        for elemt in type:
            if elemt == "Grass" or elemt == "Bug":
                pixmap = QPixmap("images/pokemon-carte-herbe.png")
                pixmap_rezise = pixmap.scaled(300, 400,Qt.KeepAspectRatio)
            elif elemt == "Normal":
                pixmap = QPixmap("images/pokemon-carte-normale.png")
                pixmap_rezise = pixmap.scaled(300, 400,Qt.KeepAspectRatio)
            elif elemt == "Water":
                pixmap = QPixmap("images/pokemon-carte-eau.png")
                pixmap_rezise = pixmap.scaled(300, 400,Qt.KeepAspectRatio)
            elif elemt == "Fire":
                pixmap = QPixmap("imagespokemon-carte-feu.png")
                pixmap_rezise = pixmap.scaled(300, 400,Qt.KeepAspectRatio)
            elif elemt == "Electric":
                pixmap = QPixmap("images/pokemon-carte-elec.png")
                pixmap_rezise = pixmap.scaled(300, 400,Qt.KeepAspectRatio)
            elif elemt == "Psychic" or elemt == "Dark":
                pixmap = QPixmap("images/pokemon-carte-psy.png")
                pixmap_rezise = pixmap.scaled(300, 400,Qt.KeepAspectRatio)
            elif elemt == "Combat" or elemt == "Ground":
                pixmap = QPixmap("images/pokemon-carte-combat.png")
                pixmap_rezise = pixmap.scaled(300, 400,Qt.KeepAspectRatio)

        self.pixmap_item = QGraphicsPixmapItem(pixmap_rezise)
        self.scene.addItem(self.pixmap_item)
        self.view.setScene(self.scene)
        self.layoutView.addWidget(self.view)
        self.resize(pixmap.width(), pixmap.height())

    @Slot(QNetworkReply)
    def chargement_fini(self, reponse: QNetworkReply):
        image = QImage()
        image.loadFromData(reponse.readAll())
        pixmap = QPixmap.fromImage(image)
        pixmap_item = QGraphicsPixmapItem(pixmap)
        pixmap_item.setPos(80,60)
        self.addItem(pixmap_item)

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.menu()

    def menu(self):
        self.centraleWidget = QWidget()
        self.setCentralWidget(self.centraleWidget)

        self.layoutPrincipal = QVBoxLayout(self.centraleWidget)

        self.layoutView = QHBoxLayout()
        self.scene = Scene()
        self.view = QGraphicsView(self.scene)
    
        self.layoutButtons = QHBoxLayout()
        self.btn_deck = QPushButton("Deck")
        self.btn_inventaire = QPushButton("Inventaire")
        self.btn_ouvrir = QPushButton("Ouvrir")

        self.layoutButtons.addWidget(self.btn_deck)
        self.layoutButtons.addWidget(self.btn_ouvrir)
        self.layoutButtons.addWidget(self.btn_inventaire)

        
        self.layoutPrincipal.addLayout(self.layoutView)
        self.layoutPrincipal.addLayout(self.layoutButtons)
        self.resize(500,500)

        self.btn_inventaire.clicked.connect(self.inventaire)

       

    def inventaire(self):
        
        self.centraleWidget = QWidget()
        self.setCentralWidget(self.centraleWidget)

        self.layoutPrincipal = QVBoxLayout(self.centraleWidget)

        self.layoutView = QHBoxLayout()
        self.view = QGraphicsView()
        self.layoutView.addWidget(self.view)

        self.layoutButtons = QHBoxLayout()
        self.btn_menu = QPushButton("Menu")

        self.layoutButtons.addWidget(self.btn_menu)

        self.layoutPrincipal.addLayout(self.layoutView)
        self.layoutPrincipal.addLayout(self.layoutButtons)
        self.resize(500,500)


        self.btn_menu.clicked.connect(self.menu)



#for i in range(15):
#    print(contenu[i]["name"]["french"])

if __name__ == "__main__":
    app = QApplication([])
    win = MyWindow()
    win.show()
    win.resize(500, 500)
    app.exec()
