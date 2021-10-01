from typing import Tuple
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import*
import sys
import os 


class blocnotas(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Bloc de notas"
        self.setWindowTitle(self.title)
        self.x = 100
        self.y = 100
        self.ancho = 1000
        self.alto = 600
        self.setGeometry(self.x, self.y, self.ancho, self.alto)


        #------------------------Contenedor con campo de texto------------------------
        contVertical = QVBoxLayout()



        self.campodetexto = QPlainTextEdit()

        
        
    
        contVertical.addWidget(self.campodetexto)
        
        



        self.campodetexto.textChanged.connect(self.contadorletras)
        

        self.campodetexto.textChanged.connect(self.vercopiar)


        
     
      

        


       
    
        #------------------------------Barra de estado------------------------------
        self.barraestado = self.statusBar()
        self.contador = 0
        self.textadicional = "Cantidad de caracteres: "
        self.letrasconteo = self.textadicional + str(self.contador)

        self.contletras = QLabel(self.letrasconteo)
        #Boton Claro/Oscuro
        botonclaro = QPushButton("Modo Claro")
        botonclaro.setStyleSheet("background-color: white; color:rgb(0, 0, 0)")
        botonclaro.clicked.connect(self.mod_blanquito)

        botonoscuro = QPushButton("Modo Oscuro")
        botonoscuro.setStyleSheet("background-color: black; color:rgb(255, 255, 255)")
        botonoscuro.clicked.connect(self.mod_oscurito)
        
        self.statusBar().addPermanentWidget(self.contletras)

        self.statusBar().addPermanentWidget(botonclaro)
        self.statusBar().addPermanentWidget(botonoscuro)




        #------------------Menu#------------------
        menu = self.menuBar()
        #----------------------------Archivo----------------------------
        menu_archivo = menu.addMenu("&Archivo")
        menu_archivo.setStatusTip("Archivo")

        #----------------------------Botones Archivo----------------------------
        #Abrir
        botonabrir = QAction(QIcon(), "Abrir",self)
        botonabrir.setShortcut("Ctrl+O")
        botonabrir.setStatusTip("Abrir")
        botonabrir.triggered.connect(self.menuAbrir)
        menu_archivo.addAction(botonabrir)

        #Guardar
        botonguardar= QAction("Guardar", self)
        botonguardar.setShortcut("Ctrl+G")
        botonguardar.setStatusTip("Guardar")
        botonguardar.triggered.connect(self.menuGuardar)
        menu_archivo.addAction(botonguardar)

        #GuardarComo
        botonguardarComo= QAction("Guardar Como", self)
        botonguardarComo.setShortcut("Ctrl+F")
        botonguardarComo.setStatusTip("Guardar")
        botonguardarComo.triggered.connect(self.menuGuardarComo)
        menu_archivo.addAction(botonguardarComo)


        #Borrar
        botonborrar= QAction("Borrar", self)
        botonborrar.setShortcut("Ctrl+j")
        botonborrar.setStatusTip("Borrar")
        botonborrar.triggered.connect(self.borrartext)
        menu_archivo.addAction(botonborrar)

        #Salir
        botonSalir= QAction("Salir", self)
        botonSalir.setShortcut("Ctrl+W")
        botonSalir.setStatusTip("Salir")
        botonSalir.triggered.connect(self.menuSalir)
        menu_archivo.addAction(botonSalir)


        


        #----------------------------Editar----------------------------
        menu_editar = menu.addMenu("&Editar")
        menu_editar.setStatusTip("Editar")

        #----------------------------Botones Editar----------------------------

        #Copiar
        self.buttoncopiar= QAction("Copiar", self)
        self.buttoncopiar.setShortcut("Ctrl+C")
        self.buttoncopiar.setStatusTip("Copíar")
        self.buttoncopiar.triggered.connect(self.campodetexto.copy)
        self.buttoncopiar.setEnabled(False)
        menu_editar.addAction(self.buttoncopiar)


        
        #Pegar
        self.buttonpegar= QAction("Pegar", self)
        self.buttonpegar.setShortcut("Ctrl+P")
        self.buttonpegar.setStatusTip("Pegar")
        self.buttonpegar.triggered.connect(self.campodetexto.paste)
        menu_editar.addAction(self.buttonpegar)

        #Deshacer
        deshacer= QAction("Deshacer", self)
        deshacer.setShortcut("Ctrl+Z")
        deshacer.setStatusTip("Deshacer")
        deshacer.triggered.connect(self.campodetexto.undo)
        menu_editar.addAction(deshacer)

        #--------------------Rehacer--------------------
        rehacer = QAction("Rehacer", self)
        rehacer.setShortcut("Ctrl+Y")
        rehacer.setStatusTip("Rehacer")
        rehacer.triggered.connect(self.campodetexto.redo)
        menu_editar.addAction(rehacer)

        #----------------------------------------
        seleccionartodo = QAction("Seleccionar todo", self)
        seleccionartodo.setShortcut("Ctrl+E")
        seleccionartodo.setStatusTip("Seleccionar todo")
        seleccionartodo.triggered.connect(self.campodetexto.selectAll)
        menu_editar.addAction(seleccionartodo)


        #---------------------Modo Oscuro---------------------
        menu_vista = menu.addMenu("&Vista")
        modooscuro = QAction("Modo oscuro", self)
        modooscuro.setShortcut("Ctrl+B")
        modooscuro.setStatusTip("Modo oscuro")
        modooscuro.triggered.connect(self.mod_oscurito)
        
        menu_vista.addAction(modooscuro)

        #---------------------Modo Claro---------------------
        modoblanco = QAction("Modo claro", self)
        modoblanco.setShortcut("Ctrl+M")
        modoblanco.setStatusTip("Modo claro")
        modoblanco.triggered.connect(self.mod_blanquito)
        
        menu_vista.addAction(modoblanco)






        
        #Archivos
        self.archivos = None

#---------------------Principal Widget---------------------

        widgetPrincipal = QWidget()
        widgetPrincipal.setLayout(contVertical)
        self.setCentralWidget(widgetPrincipal)
    

    def contadorletras(self):
        

        self.contador = len(self.campodetexto.toPlainText())
        
        self.contador = str(self.contador)
        self.letras = self.contador
        self.textadicional = "Cantidad de caracteres: "
        self.letrasconteo = self.textadicional + self.contador

        self.contletras.setText(self.letrasconteo)


        


    def menuAbrir(self, e): 

        archivo, l = QFileDialog.getOpenFileName(self, "Open file", "", "Documentos de texto(*.txt)")        
        if (os.path.exists(archivo) == True):     
            with open(archivo, 'r') as f:                   
                    text = f.read() 

            self.campodetexto.setPlainText(text) 
      
    def menuGuardar(self):

        if self.archivos is None: 
            return self.menuGuardarComo()     
        self.evaluarGuardar(self.archivos) 


    def menuGuardarComo(self):  

        archivo = QFileDialog.getSaveFileName(self, "Guardar Archivo", "", "Documentos de texto(*.txt)")
        if not archivo[0]: 
            return
        self.evaluarGuardar(archivo)
        

    def evaluarGuardar(self, archivo):
        
        textooo = self.campodetexto.toPlainText()   
        with open(archivo[0], 'w') as s: 
                s.write(textooo)     
        self.archivos = archivo


    def borrartext(self, e):
        self.campodetexto.clear()


    def menuSalir(self, e):
        exit()

    #Funcoines de Editar
    def vercopiar(self):

        nombre = self.campodetexto.toPlainText()
        if(nombre == ""):
            self.buttoncopiar.setEnabled(False)
        else:
            self.buttoncopiar.setEnabled(True)

    def mod_oscurito(self, e):
        self.campodetexto.setStyleSheet("background-color: black; color:rgb(255, 255, 255)")
        

    def mod_blanquito(self, e):
        self.campodetexto.setStyleSheet("background-color: white; color:rgb(0, 0, 0)")

    

    


app = QApplication(sys.argv)
ventana = blocnotas()
ventana.show()
app.exec()
