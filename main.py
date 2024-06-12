import math
import sys
import random
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QPushButton, QVBoxLayout, QLabel, \
    QLineEdit, QHBoxLayout, QWidget, QMessageBox, QHeaderView, QLayout, QSizePolicy, QSpacerItem
from PyQt5.QtCore import Qt


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Línea de Espera")
        self.setGeometry(500, 50, 1700, 1250)  # Aumentamos el tamaño de la ventana
        self.inicial_iteraciones = "10"
        self.inicial_limpieza = "10"
        self.inicial_llegada_futbol = "10"
        self.inicial_llegada_hand_a = "10"
        self.inicial_llegada_hand_b = "14"
        self.inicial_llegada_basket_a = "6"
        self.inicial_llegada_basket_b = "10"
        self.inicial_ocupacion_futbol_a = "80"
        self.inicial_ocupacion_futbol_b = "100"
        self.inicial_ocupacion_hand_a = "60"
        self.inicial_ocupacion_hand_b = "100"
        self.inicial_ocupacion_basket_a = "70"
        self.inicial_ocupacion_basket_b = "130"
        self.inicial_cant_grupos = "5"
        self.inicial_filas_mostrar = "10"
        self.inicial_fila_desde = "10"
        # Declaro la variable cola acá para poder utilizarla en las funciones que quiera
        self.cola = []
        self.cant_partidos = 0
        self.bandera_retiro = False
        self.init_main_window()

        # Guarda los valores iniciales de los campos de entrada
        self.initial_values = {
            'iteraciones': '',
            'limpieza': '',
            'llegada_futbol': '',
            'llegada_hand_a': '',
            'llegada_hand_b': '',
            'ocupacion_futbol_a': '',
            'ocupacion_futbol_b': '',
            'ocupacion_hand_a': '',
            'ocupacion_hand_b': '',
            'ocupacion_basket_a': '',
            'ocupacion_basket_b': '',
            'cant_grupos': '',
            'filas_mostrar': '',
            'fila_desde': ''
        }

    def init_main_window(self):
        # Campos adicionales
        self.iteraciones, self.iteraciones_input, self.iteraciones_label = self.create_input_field("Número de iteraciones: ")
        self.limpieza, self.limpieza_input, self.limpieza_label = self.create_input_field("Tiempo de Limpieza en Minutos: ")
        self.llegada_futbol, self.llegada_futbol_input, self.llegada_futbol_label = self.create_input_field(
            "Tiempo de llegada fútbol: ")
        self.llegada_hand_a, self.llegada_hand_a_input, self.llegada_hand_a_label = self.create_input_field(
            "Tiempo de llegada handball A: ")
        self.llegada_hand_b, self.llegada_hand_b_input, self.llegada_hand_b_label = self.create_input_field(
            "Tiempo de llegada handball B: ")
        self.llegada_basket_a, self.llegada_basket_a_input, self.llegada_basket_a_label = self.create_input_field(
            "Tiempo de llegada basket A: ")
        self.llegada_basket_b, self.llegada_basket_b_input, self.llegada_basket_b_label = self.create_input_field(
            "Tiempo de llegada basket B: ")
        self.ocupacion_futbol_a, self.ocupacion_futbol_a_input, self.ocupacion_futbol_a_label = self.create_input_field(
            "Tiempo de ocupación fútbol A: ")
        self.ocupacion_futbol_b, self.ocupacion_futbol_b_input, self.ocupacion_futbol_b_label = self.create_input_field(
            "Tiempo de ocupación fútbol B: ")
        self.ocupacion_hand_a, self.ocupacion_hand_a_input, self.ocupacion_hand_a_label = self.create_input_field(
            "Tiempo de ocupación hand A: ")
        self.ocupacion_hand_b, self.ocupacion_hand_b_input, self.ocupacion_hand_b_label = self.create_input_field(
            "Tiempo de ocupación hand B: ")
        self.ocupacion_basket_a, self.ocupacion_basket_a_input, self.ocupacion_basket_a_label = self.create_input_field(
            "Tiempo de ocupación basket A: ")
        self.ocupacion_basket_b, self.ocupacion_basket_b_input, self.ocupacion_basket_b_label = self.create_input_field(
            "Tiempo de ocupación basket B: ")
        self.cant_grupos, self.cant_grupos_input, self.cant_grupos_label = self.create_input_field(
            "Cantidad de grupos: ")
        self.filas_mostrar, self.filas_mostrar_input, self.filas_mostrar_label = self.create_input_field(
            "Cantidad filas a mostrar: ")
        self.fila_desde, self.fila_desde_input, self.fila_desde_label = self.create_input_field(
            "Mostrar desde la hora: ")

        # Ajustar el tamaño de la letra para los campos de entrada
        font = QFont()
        font.setPointSize(11)  # Tamaño de la letra para los campos de entrada
        self.iteraciones_label.setFont(font)
        self.limpieza_label.setFont(font)
        self.llegada_futbol_label.setFont(font)
        self.llegada_hand_a_label.setFont(font)
        self.llegada_hand_b_label.setFont(font)
        self.llegada_basket_a_label.setFont(font)
        self.llegada_basket_b_label.setFont(font)
        self.ocupacion_futbol_a_label.setFont(font)
        self.ocupacion_futbol_b_label.setFont(font)
        self.ocupacion_hand_a_label.setFont(font)
        self.ocupacion_hand_b_label.setFont(font)
        self.ocupacion_basket_a_label.setFont(font)
        self.ocupacion_basket_b_label.setFont(font)
        self.cant_grupos_label.setFont(font)
        self.filas_mostrar_label.setFont(font)
        self.fila_desde_label.setFont(font)

        self.iteraciones_input.setFont(font)
        self.limpieza_input.setFont(font)
        self.llegada_futbol_input.setFont(font)
        self.llegada_hand_a_input.setFont(font)
        self.llegada_hand_b_input.setFont(font)
        self.llegada_basket_a_input.setFont(font)
        self.llegada_basket_b_input.setFont(font)
        self.ocupacion_futbol_a_input.setFont(font)
        self.ocupacion_futbol_b_input.setFont(font)
        self.ocupacion_hand_a_input.setFont(font)
        self.ocupacion_hand_b_input.setFont(font)
        self.ocupacion_basket_a_input.setFont(font)
        self.ocupacion_basket_b_input.setFont(font)
        self.cant_grupos_input.setFont(font)
        self.filas_mostrar_input.setFont(font)
        self.fila_desde_input.setFont(font)

        # Establecer el texto de los campos de entrada con los valores guardados
        self.iteraciones_input.setText(str(self.inicial_iteraciones))
        self.limpieza_input.setText(str(self.inicial_limpieza))
        self.llegada_futbol_input.setText(str(self.inicial_llegada_futbol))
        self.llegada_hand_a_input.setText(str(self.inicial_llegada_hand_a))
        self.llegada_hand_b_input.setText(str(self.inicial_llegada_hand_b))
        self.llegada_basket_a_input.setText(str(self.inicial_llegada_basket_a))
        self.llegada_basket_b_input.setText(str(self.inicial_llegada_basket_b))
        self.ocupacion_futbol_a_input.setText(str(self.inicial_ocupacion_futbol_a))
        self.ocupacion_futbol_b_input.setText(str(self.inicial_ocupacion_futbol_b))
        self.ocupacion_hand_a_input.setText(str(self.inicial_ocupacion_hand_a))
        self.ocupacion_hand_b_input.setText(str(self.inicial_ocupacion_hand_b))
        self.ocupacion_basket_a_input.setText(str(self.inicial_ocupacion_basket_a))
        self.ocupacion_basket_b_input.setText(str(self.inicial_ocupacion_basket_b))
        self.cant_grupos_input.setText(str(self.inicial_cant_grupos))
        self.filas_mostrar_input.setText(str(self.inicial_filas_mostrar))
        self.fila_desde_input.setText(str(self.inicial_fila_desde))

        # Botón para guardar los valores y mostrar la segunda página
        self.pushButton = QPushButton("Simular", self)
        self.pushButton.setGeometry(350, 540, 100, 30)  # Ajustamos la posición del botón
        self.pushButton.clicked.connect(self.show_second_page)

        # Botón para cancelar
        self.cancelButton = QPushButton("Cancelar", self)
        self.cancelButton.setGeometry(470, 540, 100, 30)  # Ajustamos la posición del botón
        self.cancelButton.clicked.connect(self.cancel_action)

        # Conectar el evento returnPressed de los campos de entrada a la función simular_action
        self.iteraciones_input.returnPressed.connect(self.simular_action)
        self.limpieza_input.returnPressed.connect(self.simular_action)
        self.llegada_futbol_input.returnPressed.connect(self.simular_action)
        self.llegada_hand_a_input.returnPressed.connect(self.simular_action)
        self.llegada_hand_b_input.returnPressed.connect(self.simular_action)
        self.llegada_basket_a_input.returnPressed.connect(self.simular_action)
        self.llegada_basket_b_input.returnPressed.connect(self.simular_action)
        self.ocupacion_futbol_a_input.returnPressed.connect(self.simular_action)
        self.ocupacion_futbol_b_input.returnPressed.connect(self.simular_action)
        self.ocupacion_hand_a_input.returnPressed.connect(self.simular_action)
        self.ocupacion_hand_b_input.returnPressed.connect(self.simular_action)
        self.ocupacion_basket_a_input.returnPressed.connect(self.simular_action)
        self.ocupacion_basket_b_input.returnPressed.connect(self.simular_action)
        self.cant_grupos_input.returnPressed.connect(self.simular_action)
        self.filas_mostrar_input.returnPressed.connect(self.simular_action)
        self.fila_desde_input.returnPressed.connect(self.simular_action)

        self.pushButton.setFont(font)
        self.cancelButton.setFont(font)
        # Crear un diseño vertical para organizar los diseños horizontales
        layout = QVBoxLayout()

        layout.setSizeConstraint(QLayout.SetMinAndMaxSize)

        # Agregar espaciador vertical para empujar los campos hacia arriba
        layout.addSpacing(100)

        # Agregar los diseños horizontales al diseño vertical
        row_layout_1 = QHBoxLayout()
        row_layout_1.addWidget(self.iteraciones_label)
        row_layout_1.addWidget(self.iteraciones_input)
        row_layout_1.addWidget(self.limpieza_label)
        row_layout_1.addWidget(self.limpieza_input)
        row_layout_1.addWidget(self.llegada_futbol_label)
        row_layout_1.addWidget(self.llegada_futbol_input)
        layout.addLayout(row_layout_1)

        layout.addSpacing(50)

        row_layout_2 = QHBoxLayout()
        row_layout_2.addWidget(self.llegada_hand_a_label)
        row_layout_2.addWidget(self.llegada_hand_a_input)
        row_layout_2.addWidget(self.llegada_hand_b_label)
        row_layout_2.addWidget(self.llegada_hand_b_input)
        layout.addLayout(row_layout_2)

        layout.addSpacing(50)

        row_layout_3 = QHBoxLayout()
        row_layout_3.addWidget(self.llegada_basket_a_label)
        row_layout_3.addWidget(self.llegada_basket_a_input)
        row_layout_3.addWidget(self.llegada_basket_b_label)
        row_layout_3.addWidget(self.llegada_basket_b_input)
        layout.addLayout(row_layout_3)

        layout.addSpacing(50)

        row_layout_4 = QHBoxLayout()
        row_layout_4.addWidget(self.ocupacion_futbol_a_label)
        row_layout_4.addWidget(self.ocupacion_futbol_a_input)
        row_layout_4.addWidget(self.ocupacion_futbol_b_label)
        row_layout_4.addWidget(self.ocupacion_futbol_b_input)
        layout.addLayout(row_layout_4)

        layout.addSpacing(50)

        row_layout_5 = QHBoxLayout()
        row_layout_5.addWidget(self.ocupacion_hand_a_label)
        row_layout_5.addWidget(self.ocupacion_hand_a_input)
        row_layout_5.addWidget(self.ocupacion_hand_b_label)
        row_layout_5.addWidget(self.ocupacion_hand_b_input)
        layout.addLayout(row_layout_5)

        layout.addSpacing(50)

        row_layout_6 = QHBoxLayout()
        row_layout_6.addWidget(self.ocupacion_basket_a_label)
        row_layout_6.addWidget(self.ocupacion_basket_a_input)
        row_layout_6.addWidget(self.ocupacion_basket_b_label)
        row_layout_6.addWidget(self.ocupacion_basket_b_input)
        layout.addLayout(row_layout_6)

        layout.addSpacing(50)

        row_layout_7 = QHBoxLayout()
        row_layout_7.addWidget(self.cant_grupos_label)
        row_layout_7.addWidget(self.cant_grupos_input)
        layout.addLayout(row_layout_7)

        layout.addSpacing(50)

        row_layout_8 = QHBoxLayout()
        row_layout_8.addWidget(self.filas_mostrar_label)
        row_layout_8.addWidget(self.filas_mostrar_input)
        row_layout_8.addWidget(self.fila_desde_label)
        row_layout_8.addWidget(self.fila_desde_input)
        layout.addLayout(row_layout_8)

        # Agregar el botón al diseño vertical
        layout.addSpacing(100)
        layout.addWidget(self.pushButton)
        layout.addSpacing(10)
        layout.addWidget(self.cancelButton)
        layout.addSpacing(50)

        self.central_widget = QWidget()  # Se agrega la variable central_widget
        self.central_widget.setLayout(layout)
        self.setCentralWidget(self.central_widget)

        # Inicializar los valores de los campos
        self.iteraciones = 0
        self.limpieza = 0
        self.llegada_futbol = 0
        self.llegada_hand_a = 0
        self.llegada_hand_b = 0
        self.llegada_basket_a = 0
        self.llegada_basket_b = 0
        self.ocupacion_futbol_a = 0
        self.ocupacion_futbol_b = 0
        self.ocupacion_hand_a = 0
        self.ocupacion_hand_b = 0
        self.ocupacion_basket_a = 0
        self.ocupacion_basket_b = 0
        self.cant_grupos = 0
        self.filas_mostrar = 0
        self.fila_desde = 0
        self.cola = []
        self.bandera_retiro = False
        self.cant_partidos = 0

    def cancel_action(self):
        self.close()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Up:
            self.focusPreviousChild()
        elif event.key() == Qt.Key_Down:
            self.focusNextChild()
        elif event.key() == Qt.Key_Left:
            self.focusPreviousChild()
        elif event.key() == Qt.Key_Right:
            self.focusNextChild()
        else:
            super().keyPressEvent(event)

    def focusNextChild(self):
        focusWidget = self.focusWidget()
        if focusWidget is not None:
            self.focusWidget().focusNextChild()
        else:
            super().focusNextChild()

    def focusPreviousChild(self):
        focusWidget = self.focusWidget()
        if focusWidget is not None:
            self.focusWidget().focusPreviousChild()
        else:
            super().focusPreviousChild()

    def simular_action(self):
        # Realizar la acción de simulación o cerrar la ventana, dependiendo del contexto
        self.show_second_page()

    def insertar_en_tabla(self, fila):
        # Obtiene el número de filas existentes en la tabla
        i = self.tableWidgetSecond.rowCount()
        # Inserta una nueva fila en la tabla en la posición 'i'
        self.tableWidgetSecond.insertRow(i)

        # Calcula el número necesario de columnas, considerando tanto los datos como los objetos
        num_columnas_necesarias = len(fila)

        # Ajusta el número de columnas de la tabla si es necesario
        while self.tableWidgetSecond.columnCount() < num_columnas_necesarias:
            self.tableWidgetSecond.insertColumn(self.tableWidgetSecond.columnCount())

        # Inicializa el índice de la columna a 0
        j = 0
        # Establece el índice de la columna inicial para los objetos
        column_index = 32

        # Contador para el número de objetos
        object_count = 0

        # Itera sobre cada elemento en la fila de datos
        for item in fila:
            # Verifica si el elemento es una lista (objeto)
            if isinstance(item, list):
                # Incrementa el contador de objetos
                object_count += 1
                # Inserta el objeto completo en la tabla en la fila 'i' y la columna correspondiente
                self.tableWidgetSecond.setItem(i, column_index, QTableWidgetItem(str(item)))
                # Verifica si es necesario añadir una nueva columna para el objeto
                if self.tableWidgetSecond.columnCount() <= column_index:
                    self.tableWidgetSecond.insertColumn(column_index)
                # Añadir título de la columna si no existe
                if self.tableWidgetSecond.horizontalHeaderItem(column_index) is None:
                    self.tableWidgetSecond.setHorizontalHeaderItem(column_index,
                                                                   QTableWidgetItem(f"Objeto {object_count}"))
                # Incrementa el índice de la columna para los próximos objetos
                column_index += 1
            else:
                # Si el elemento no es una lista, lo inserta directamente en la tabla en la fila 'i' y la columna 'j'
                # Formatea el número si es un float
                if isinstance(item, float):
                    item = f"{item:.2f}"
                # Crea un QTableWidgetItem para el dato
                item_widget = QTableWidgetItem(str(item))
                # Centra el texto en la columna
                item_widget.setTextAlignment(Qt.AlignCenter)
                self.tableWidgetSecond.setItem(i, j, item_widget)
                # Incrementa el índice de la columna
                j += 1

        # Ajusta el número de columnas para los objetos si es necesario
        while self.tableWidgetSecond.columnCount() < column_index:
            self.tableWidgetSecond.insertColumn(self.tableWidgetSecond.columnCount())

        for col in range(self.tableWidgetSecond.columnCount()):
            self.tableWidgetSecond.setColumnWidth(col, 500)

    def agregar_fila_flotante(self, vector_final):
        # Asegura que haya suficientes columnas para el vector final
        columnas_necesarias = max(29 + len(vector_final[1:4]), 31 + 1)
        while self.tableWidgetSecond.columnCount() < columnas_necesarias:
            self.tableWidgetSecond.insertColumn(self.tableWidgetSecond.columnCount())

        # Inserta una nueva fila al final para la fila flotante
        i = self.tableWidgetSecond.rowCount()
        self.tableWidgetSecond.insertRow(i)

        # Inserta las celdas correspondientes en la fila flotante
        item_widget = QTableWidgetItem(vector_final[0])
        item_widget.setTextAlignment(Qt.AlignCenter)
        self.tableWidgetSecond.setItem(i, 27, item_widget)

        for k in range(3):
            valor = vector_final[k + 1]
            if isinstance(valor, float):
                valor = f"{valor:.2f}"
            item_widget = QTableWidgetItem(str(valor))
            item_widget.setTextAlignment(Qt.AlignCenter)
            self.tableWidgetSecond.setItem(i, 28 + k, item_widget)

        item_widget = QTableWidgetItem(vector_final[4])
        item_widget.setTextAlignment(Qt.AlignCenter)
        self.tableWidgetSecond.setItem(i, 31, item_widget)

        valor = vector_final[5]
        if isinstance(valor, float):
            valor = f"{valor:.2f}"
        item_widget = QTableWidgetItem(str(valor))
        item_widget.setTextAlignment(Qt.AlignCenter)
        self.tableWidgetSecond.setItem(i, 32, item_widget)

    def create_input_field(self, text):
        layout = QHBoxLayout()
        label = QLabel(text)
        layout.addWidget(label)

        input_field = QLineEdit()
        layout.addWidget(input_field)

        return layout, input_field, label

    def show_second_page(self):
        iteraciones_text = self.iteraciones_input.text()
        self.inicial_iteraciones = iteraciones_text

        limpieza_text = self.limpieza_input.text()
        self.inicial_limpieza = limpieza_text

        llegada_futbol_text = self.llegada_futbol_input.text()
        self.inicial_llegada_futbol = llegada_futbol_text

        llegada_hand_a_text = self.llegada_hand_a_input.text()
        self.inicial_llegada_hand_a = llegada_hand_a_text

        llegada_hand_b_text = self.llegada_hand_b_input.text()
        self.inicial_llegada_hand_b = llegada_hand_b_text

        llegada_basket_a_text = self.llegada_basket_a_input.text()
        self.inicial_llegada_basket_a = llegada_basket_a_text

        llegada_basket_b_text = self.llegada_basket_b_input.text()
        self.inicial_llegada_basket_b = llegada_basket_b_text

        ocupacion_futbol_a_text = self.ocupacion_futbol_a_input.text()
        self.inicial_ocupacion_futbol_a = ocupacion_futbol_a_text

        ocupacion_futbol_b_text = self.ocupacion_futbol_b_input.text()
        self.inicial_ocupacion_futbol_b = ocupacion_futbol_b_text

        ocupacion_hand_a_text = self.ocupacion_hand_a_input.text()
        self.inicial_ocupacion_hand_a = ocupacion_hand_a_text

        ocupacion_hand_b_text = self.ocupacion_hand_b_input.text()
        self.inicial_ocupacion_hand_b = ocupacion_hand_b_text

        ocupacion_basket_a_text = self.ocupacion_basket_a_input.text()
        self.inicial_ocupacion_basket_a = ocupacion_basket_a_text

        ocupacion_basket_b_text = self.ocupacion_basket_b_input.text()
        self.inicial_ocupacion_basket_b = ocupacion_basket_b_text

        cant_grupos_text = self.cant_grupos_input.text()
        self.inicial_cant_grupos = cant_grupos_text

        filas_mostrar_text = self.filas_mostrar_input.text()
        self.inicial_filas_mostrar = filas_mostrar_text

        fila_desde_text = self.fila_desde_input.text()
        self.inicial_fila_desde = fila_desde_text

        # Validación de todos los campos para que todos sean completados
        #if dias_text.strip() == '' or ventas_text.strip() == '' or costo_ventas_text.strip() == '' \
        #       or costo_obrero_text.strip() == '' or filas_mostrar_text.strip() == '' or fila_desde_text.strip() == '':
        #   QMessageBox.warning(self, 'Campos vacíos', 'Por favor, complete todos los campos.')
        #   return

        iteraciones = int(iteraciones_text)
        limpieza = float(limpieza_text)
        llegada_futbol = float(llegada_futbol_text)
        llegada_hand_a = float(llegada_hand_a_text)
        llegada_hand_b = float(llegada_hand_b_text)
        llegada_basket_a = float(llegada_basket_a_text)
        llegada_basket_b = float(llegada_basket_b_text)
        ocupacion_futbol_a = float(ocupacion_futbol_a_text)
        ocupacion_futbol_b = float(ocupacion_futbol_b_text)
        ocupacion_hand_a = float(ocupacion_hand_a_text)
        ocupacion_hand_b = float(ocupacion_hand_b_text)
        ocupacion_basket_a = float(ocupacion_basket_a_text)
        ocupacion_basket_b = float(ocupacion_basket_b_text)
        cant_grupos = int(cant_grupos_text)
        filas_mostrar = int(filas_mostrar_text)
        fila_desde = int(fila_desde_text)
        self.init_second_page2(iteraciones, limpieza, llegada_futbol, llegada_hand_a, llegada_hand_b, llegada_basket_a,
                               llegada_basket_b, ocupacion_futbol_a, ocupacion_futbol_b, ocupacion_hand_a,
                               ocupacion_hand_b,ocupacion_basket_a, ocupacion_basket_b,cant_grupos, filas_mostrar, fila_desde)

    def init_second_page2(self, iteraciones, limpieza, llegada_futbol, llegada_hand_a, llegada_hand_b, llegada_basket_a,
                               llegada_basket_b, ocupacion_futbol_a, ocupacion_futbol_b, ocupacion_hand_a,
                               ocupacion_hand_b,ocupacion_basket_a, ocupacion_basket_b,cant_grupos, filas_mostrar, fila_desde):
        self.tableWidgetSecond = QTableWidget(self)
        self.tableWidgetSecond.setColumnCount(32)
        self.tableWidgetSecond.setHorizontalHeaderLabels(
            ["Evento", "Reloj", "Fútbol RND", "Fútbol Tiempo entre Llegadas", "Fútbol Próxima Llegada", "Hand RND",
             "Hand Tiempo entre Llegadas", "Hand Próxima Llegada", "Basket RND",
             "Basket Tiempo entre Llegadas", "Basket Próxima Llegada", "Cola Cancha", "Grupo Retirado", "Estado Cancha",
             "Fútbol RND", "Fútbol Tiempo de Ocupación", "Fútbol Fin Ocupación", "Hand RND", "Hand Tiempo de Ocupación",
             "Hand Fin Ocupación", "Basket RND", "Basket Tiempo de Ocupación",
             "Basket Fin Ocupación", "Tiempo de Limpieza", "Tiempo de Espera", "Cantidad Grupos Fútbol", "Cantidad Grupos Hand",
             "Cantidad Grupos Basket", "Fútbol Tiempo de espera acumulado", "Hand Tiempo de espera acumulado",
             "Basket Tiempo de espera acumulado", "Tiempo de limpieza acumulado"])
        #Ver dónde o cómo podría poner la tasa de limpieza y el promedio a calcular

        self.iniciar_simulacion(iteraciones, limpieza, llegada_futbol, llegada_hand_a, llegada_hand_b, llegada_basket_a,
                               llegada_basket_b, ocupacion_futbol_a, ocupacion_futbol_b, ocupacion_hand_a,
                               ocupacion_hand_b,ocupacion_basket_a, ocupacion_basket_b,cant_grupos, filas_mostrar, fila_desde)

        self.backButton = QPushButton("Volver", self)
        self.backButton.setGeometry(350, 540, 100, 30)
        self.backButton.clicked.connect(self.show_main_page)

        font = QFont()
        font.setPointSize(11)
        self.backButton.setFont(font)
        self.tableWidgetSecond.setFont(font)
        self.tableWidgetSecond.horizontalHeader().setFont(font)
        layout = QVBoxLayout()
        layout.addWidget(self.tableWidgetSecond)
        layout.addWidget(self.backButton)
        second_page_widget = QWidget()
        second_page_widget.setLayout(layout)
        self.setCentralWidget(second_page_widget)

    def show_main_page(self):
        self.init_main_window()

    # Aca empece a modificar
    
    
    def iniciar_simulacion(self, iteraciones, limpieza, llegada_futbol, llegada_hand_a, llegada_hand_b, llegada_basket_a,
                               llegada_basket_b, ocupacion_futbol_a, ocupacion_futbol_b, ocupacion_hand_a,
                               ocupacion_hand_b,ocupacion_basket_a, ocupacion_basket_b,cant_grupos, filas_mostrar, fila_desde):
        # Defini este vector estado con el excel, lo unico que en vez de hacer tantas columnas para calcular la llegada de los equipos hice una por equipo, al igual que la ocupacion
        # Para la ocupacion, solo muestro cuando se va a desocupar (en tiempo) y que equipo la esta ocupando, para ahorrar columnas, porque solo un equipo ocupa la cancha a la vez
        tiempo_llegada_futbol, rnd_futbol_llegada = self.calcularProxLlegadaFutbol(0, llegada_futbol)
        tiempo_llegada_hand, rnd_hand_llegada = self.calcularProxLlegadaHandball(0, llegada_hand_a, llegada_hand_b)
        tiempo_llegada_basket, rnd_basket_llegada = self.calcularProxLlegadaBasketball(0, llegada_basket_a, llegada_basket_b)
                        #EVENTO  #RELOJ #RND #TIEMPO ENTRE LLEGADAS #LLEGADA
        vectorEstado = ["Inicio", 0, rnd_futbol_llegada, 0, tiempo_llegada_futbol, rnd_hand_llegada, 0, tiempo_llegada_hand,
                        rnd_basket_llegada, 0, tiempo_llegada_basket, 0, "", "Libre", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        print(vectorEstado)

        # Si fila_desde es 0, incluir el estado inicial en la tabla
        if fila_desde == 0:
            self.insertar_en_tabla(vectorEstado)

        # Variables para controlar la iteración desde fila_desde
        se_alcanzo_fila_desde = False
        primera_iteracion_fila_desde = None

        limpieza = limpieza / 60

        # Todo esto iria en un for o en un while que vaya iterando en el tiempo
        # después en 5 debería ir la variable iteraciones
        for i in range(iteraciones):
            prox_reloj, nombre_proxEvento = self.proximoEvento(vectorEstado)
            print(self.cola)
            # Asignamos el valor de prox_reloj al reloj actual y tambien el nombre del evento
            vectorEstado[0] = nombre_proxEvento
            vectorEstado[1] = prox_reloj
            # Acá voy viendo el tamaño que tiene el vector cola, en la primera iteración 0 va a dar bien y va a
            # a estar en 0, luego para actualizar este contador en fin ocupación y descontarlo también
            # lo actualicé en esos casos
            vectorEstado[11] = len(self.cola)

            # Verifico que el vector cola sea mayor a 2 ya que no puedo ejecutar la función porque es solo
            # para la prioridad en el caso de que basketball se encuentre en la posición 1 del vector
            if len(self.cola) > 2:
                # La función me va a devolver por ejemplo: si tengo el vector cola como
                # cola = ["futbol", "basketball", "handball"]
                # me va a devolver: cola = ["futbol", "handball", "basketball"]
                self.verificar_prioridad_cola()

            if i > 2:
                # Esto hace lo mismo que arriba pero en el caso de los vectores de los objetos
                # Lo que hago es decir, si tengo ["basketball", "en cola", 1] ["handball", "en cola", 2]
                # Esto lo que va a hacer es cambiar las posiciones ["basketball", "en cola", 2] ["handball", "en cola", 1]
                # También después verifica en el caso de que el vector que siga después de basketball ya esté en
                # estado "en cancha", en ese caso sigue de largo y busca al que si esté en cola
                self.verificar_prioridad_objeto(vectorEstado)

            if i == 0:
                if (nombre_proxEvento == "Llegada futbol"):
                    # Aca iria la logica si llega un equipo de futbol
                    # Primero calculamos la proxima llegada de un equipo de futbol

                    vectorEstado[3], vectorEstado[2] = self.calcularProxLlegadaFutbol(vectorEstado[1], llegada_futbol)

                    vectorEstado[4] = vectorEstado[3] + prox_reloj

                    vectorEstado[13] = "Ocupado"

                    #luego calculo cuanto tiempo va a ocupar la cancha pero me falta el if que si no esta ocupada la cancha
                    vectorEstado[15], vectorEstado[14] = self.calcularFinOcupacionFutbol(vectorEstado[1], ocupacion_futbol_a, ocupacion_futbol_b)
                    vectorEstado[16] = vectorEstado[15] + prox_reloj
                    vectorEstado[23] = vectorEstado[16] + limpieza

                    
                    objeto = ["futbol", "en cancha", vectorEstado[11], prox_reloj]
                    vectorEstado.append(objeto)
                    # Voy agregando los nombres al vector cola
                    self.cola.append(objeto[0])
                    vectorEstado[25] += 1
                    print(vectorEstado)
                elif (nombre_proxEvento == "Llegada handball"):
                    # Aca iria la logica si llega handball

                    vectorEstado[6], vectorEstado[5] = self.calcularProxLlegadaHandball(vectorEstado[1], llegada_hand_a, llegada_hand_b)

                    vectorEstado[7] = vectorEstado[6] + prox_reloj

                    vectorEstado[13] = "Ocupado"

                    #luego calculo cuanto tiempo va a ocupar la cancha
                    vectorEstado[18], vectorEstado[17] = self.calcularFinOcupacionHandball(vectorEstado[1], ocupacion_hand_a, ocupacion_hand_b)
                    vectorEstado[19] = vectorEstado[18] + prox_reloj
                    vectorEstado[23] = vectorEstado[19] + limpieza

                    
                    objeto = ["handball", "en cancha", vectorEstado[11], prox_reloj]
                    vectorEstado.append(objeto)
                    # Voy agregando los nombres al vector cola
                    self.cola.append(objeto[0])
                    vectorEstado[26] += 1
                    print(vectorEstado)

                elif(nombre_proxEvento == "Llegada basketball"):
                    # Aca iria la logica si llega un equipo de basketball

                    vectorEstado[9], vectorEstado[8] = self.calcularProxLlegadaBasketball(vectorEstado[1], llegada_basket_a, llegada_basket_b)

                    vectorEstado[10] = vectorEstado[9] + prox_reloj

                    vectorEstado[13] = "Ocupado"

                    #luego calculo cuanto tiempo va a ocupar la cancha
                    vectorEstado[21], vectorEstado[20] = self.calcularFinOcupacionHandball(vectorEstado[1], ocupacion_basket_a, ocupacion_basket_b)
                    vectorEstado[22] = vectorEstado[21] + prox_reloj
                    vectorEstado[23] = vectorEstado[22] + limpieza

                    
                    objeto = ["basketball", "en cancha", vectorEstado[11], prox_reloj]
                    vectorEstado.append(objeto)
                    # Voy agregando los nombres al vector cola
                    self.cola.append(objeto[0])
                    vectorEstado[27] += 1
                    print(vectorEstado)

            elif i > 0:
                retiro = self.verificar_grupo_retirado(cant_grupos)

                if (nombre_proxEvento == "Llegada futbol"):
                    if retiro == False:
                        vectorEstado[3], vectorEstado[2] = self.calcularProxLlegadaFutbol(vectorEstado[1], llegada_futbol)

                        vectorEstado[4] = vectorEstado[3] + prox_reloj

                        objeto = ["futbol", "en cola", vectorEstado[11], prox_reloj]
                        vectorEstado.append(objeto)
                        # Voy agregando los nombres al vector cola
                        self.cola.append(objeto[0])
                        vectorEstado[25] += 1

                    else:
                        vectorEstado[3], vectorEstado[2] = self.calcularProxLlegadaFutbol(vectorEstado[1],
                                                                                          llegada_futbol)

                        vectorEstado[4] = vectorEstado[3] + prox_reloj
                        objeto = ["futbol", "retirado", -1, prox_reloj]
                        vectorEstado.append(objeto)
                        vectorEstado[12] = "SI"


                    print(vectorEstado)
                elif (nombre_proxEvento == "Llegada handball"):
                    if retiro == False:
                        vectorEstado[6], vectorEstado[5] = self.calcularProxLlegadaHandball(vectorEstado[1], llegada_hand_a, llegada_hand_b)

                        vectorEstado[7] = vectorEstado[6] + prox_reloj

                        objeto = ["handball", "en cola", vectorEstado[11], prox_reloj]
                        vectorEstado.append(objeto)
                        # Voy agregando los nombres al vector cola
                        self.cola.append(objeto[0])
                        vectorEstado[26] += 1

                    else:
                        vectorEstado[6], vectorEstado[5] = self.calcularProxLlegadaHandball(vectorEstado[1],
                                                                                            llegada_hand_a,
                                                                                            llegada_hand_b)

                        vectorEstado[7] = vectorEstado[6] + prox_reloj
                        objeto = ["handball", "retirado", -1, prox_reloj]
                        vectorEstado.append(objeto)
                        vectorEstado[12] = "SI"


                    print(vectorEstado)

                elif (nombre_proxEvento == "Llegada basketball"):
                    if retiro == False:
                        vectorEstado[9], vectorEstado[8] = self.calcularProxLlegadaBasketball(vectorEstado[1], llegada_basket_a, llegada_basket_b)

                        vectorEstado[10] = vectorEstado[9] + prox_reloj

                        objeto = ["basketball", "en cola", vectorEstado[11], prox_reloj]
                        vectorEstado.append(objeto)
                        # Voy agregando los nombres al vector cola
                        self.cola.append(objeto[0])
                        vectorEstado[27] += 1

                    else:
                        vectorEstado[9], vectorEstado[8] = self.calcularProxLlegadaBasketball(vectorEstado[1],
                                                                                              llegada_basket_a,
                                                                                              llegada_basket_b)

                        vectorEstado[10] = vectorEstado[9] + prox_reloj
                        objeto = ["basketball", "retirado", -1, prox_reloj]
                        vectorEstado.append(objeto)
                        vectorEstado[12] = "SI"


                    print(vectorEstado)

                elif (nombre_proxEvento == "Fin Ocupacion futbol") or (nombre_proxEvento == "Fin Ocupacion handball") or (nombre_proxEvento == "Fin Ocupacion basketball"):
                    # Acá lo que hago es verificar qué equipo está en posición 1 en la cola para poder calcular
                    # el tiempo de ocupación de ese equipo en la misma fila que apareció el evento Fin Ocupación
                    # del equipo que estaba en posición 0
                    if self.cola[1] == "futbol":
                        vectorEstado[15], vectorEstado[14] = self.calcularFinOcupacionFutbol(vectorEstado[1], ocupacion_futbol_a, ocupacion_futbol_b)
                        vectorEstado[16] = vectorEstado[15] + prox_reloj
                        vectorEstado[23] = vectorEstado[16] + limpieza
                        vectorEstado[31] += limpieza
                        # Acá llamo a esta función ya que si llegó este evento de fin ocupación debo pasar el equipo
                        # que termino de ocupar a destruido y el que estaba en posición 1 a que esté en cancha
                        # y además actualizar las posiciones de los demás objetos en cola
                        self.actualizar_vectores(vectorEstado)

                        tiempo_espera_futbol = vectorEstado[24]
                        print(tiempo_espera_futbol)
                        vectorEstado[28] += tiempo_espera_futbol
                        # borro en el vector cola el equipo en posición 0 ya que termino de ocupar la cancha
                        self.cola.pop(0)
                        # actualizo el contador cola porque uno que estaba en fila entro a la cancha
                        vectorEstado[11] = len(self.cola) - 1

                        self.cant_partidos += 1
                        print(vectorEstado)

                    elif self.cola[1] == "handball":
                        vectorEstado[18], vectorEstado[17] = self.calcularFinOcupacionHandball(vectorEstado[1], ocupacion_hand_a, ocupacion_hand_b)
                        vectorEstado[19] = vectorEstado[18] + prox_reloj
                        vectorEstado[23] = vectorEstado[19] + limpieza
                        vectorEstado[31] += limpieza
                        self.actualizar_vectores(vectorEstado)

                        tiempo_espera_handball = vectorEstado[24]
                        vectorEstado[29] += tiempo_espera_handball
                        self.cola.pop(0)
                        vectorEstado[11] = len(self.cola) - 1
                        self.cant_partidos += 1
                        print(vectorEstado)

                    elif self.cola[1] == "basketball":
                        vectorEstado[21], vectorEstado[20] = self.calcularFinOcupacionHandball(vectorEstado[1], ocupacion_hand_a, ocupacion_hand_b)
                        vectorEstado[22] = vectorEstado[21] + prox_reloj
                        vectorEstado[23] = vectorEstado[22] + limpieza
                        vectorEstado[31] += limpieza
                        self.actualizar_vectores(vectorEstado)

                        tiempo_espera_basket = vectorEstado[24]
                        vectorEstado[30] += tiempo_espera_basket
                        self.cola.pop(0)
                        vectorEstado[11] = len(self.cola) - 1
                        self.cant_partidos += 1
                        print(vectorEstado)

            # Verificar si se alcanzó la fila desde
            if prox_reloj >= fila_desde and not se_alcanzo_fila_desde:
                se_alcanzo_fila_desde = True
                primera_iteracion_fila_desde = i

            # Verificar si estamos dentro del rango de filas a mostrar
            if se_alcanzo_fila_desde and (i >= primera_iteracion_fila_desde and i <= filas_mostrar) or i == iteraciones - 1:
                self.insertar_en_tabla(vectorEstado)

                if i == iteraciones - 1:
                    vectorCalculo = self.fila_calculo(vectorEstado)
                    self.agregar_fila_flotante(vectorCalculo)

    def proximoEvento(self, vectorEstado):
        proximoRelojLlegada = [vectorEstado[4], vectorEstado[7], vectorEstado[10], vectorEstado[23]]

        # Todo este if lo unico que hace es no devolver como primer evento el fin de ocupacion, cuando vale 0 en la primer "fila" de la tabla
        # en el evento de "Inicio"
        if vectorEstado[23] > 0:
            # Encontrar el índice del valor mínimo en proximoRelojLlegada
            indice_minimo = proximoRelojLlegada.index(min(proximoRelojLlegada))

            nombres_reloj = ["Llegada futbol", "Llegada handball", "Llegada basketball", "Fin Ocupacion"]

            # Acá lo que hago es que si llegue al evento Fin Ocupación debo saber cuál de todos los equipos
            # terminó de desocupar la cancha por eso concateno la string que está en la posición 0 en el vector cola
            if len(self.cola) > 0:
                # Añadir la primera palabra del subvector a "Fin Ocupacion"
                nombres_reloj[3] += " " + self.cola[0]

            nombre_reloj_minimo = nombres_reloj[indice_minimo]

            # Devolver el número de reloj y el nombre del próximo evento
        else:
            # Encontrar el índice del valor mínimo en proximoRelojLlegada
            indice_minimo = proximoRelojLlegada.index(min(proximoRelojLlegada[0], proximoRelojLlegada[1], proximoRelojLlegada[2]))

            # Asignar nombres de reloj según el índice
            nombres_reloj = ["Llegada futbol", "Llegada handball", "Llegada basketball"]
            nombre_reloj_minimo = nombres_reloj[indice_minimo]

            # Devolver el número de reloj y el nombre del próximo evento
        return proximoRelojLlegada[indice_minimo], nombre_reloj_minimo


    def actualizar_vectores(self, vector_estado):
        # Buscar el vector en la posición "en cancha"
        indice_en_cancha = None
        for i, vector in enumerate(vector_estado):
            if isinstance(vector, list) and vector[1] == "en cancha":
                indice_en_cancha = i
                break

        if indice_en_cancha is not None:
            # Cambiar el estado del equipo en cancha a "destruido"
            vector_estado[indice_en_cancha][1] = "destruido"
            vector_estado[indice_en_cancha][2] = -1

            # Verificar si no hay equipo en posición 0 y en cancha
            if all(vector[1] != "en cancha" for vector in vector_estado if isinstance(vector, list) and vector[2] == 1):
                # Buscar el siguiente equipo en cola con la posición más baja
                indice_en_cola = None
                posicion_en_cola_minima = float('inf')  # Inicializar con un valor grande
                for i, vector in enumerate(vector_estado):
                    if isinstance(vector, list) and vector[1] == "en cola" and vector[2] < posicion_en_cola_minima:
                        indice_en_cola = i
                        posicion_en_cola_minima = vector[2]

                # Mover el equipo en cola con la posición más baja a la cancha
                if indice_en_cola is not None:
                    vector_estado[indice_en_cola][1] = "en cancha"
                    vector_estado[indice_en_cola][2] = 0

                    # calculo el tiempo de espera del objeto que va a entrar en cancha
                    tiempo_entro_cola = vector_estado[indice_en_cola][3]
                    tiempo_entro_jugar = vector_estado[1]
                    tiempo_espera = tiempo_entro_jugar - tiempo_entro_cola

                    # muestro en el vector estado el tiempo de espera que tuvo ese objeto
                    vector_estado[24] = tiempo_espera
                # Ajustar las posiciones de los equipos restantes en cola
                for vector in vector_estado:
                    if isinstance(vector, list) and vector[1] == "en cola" and vector[2] > 0:
                        vector[2] -= 1

        return vector_estado

    def verificar_prioridad_cola(self):
        # Verificar si el equipo en posición 1 es basketball y en la posición 2 está futbol o handball
        if self.cola[1] == "basketball" and self.cola[2] in ["futbol", "handball"]:
            # Intercambiar las posiciones de basketball y el equipo siguiente en el vector cola
            self.cola[1], self.cola[2] = self.cola[2], self.cola[1]

    def verificar_prioridad_objeto(self, vector_estado):
        indice_en_cola = self.obtener_indice_en_cola(vector_estado)
        if indice_en_cola is not None:
            # Verificar si el equipo en posición 1 es basketball y en la posición 2 está futbol o handball
            if vector_estado[indice_en_cola][0] == "basketball" and \
                    vector_estado[min(indice_en_cola + 1, len(vector_estado) - 1)][0] in ["futbol", "handball"]:
                vector_estado[indice_en_cola][2] = 2

                # Esto lo debo hacer ya que al quedar el vector objeto de basketball antes que los que empiezan a
                # entrar en cancha me ponía como ["handball", "en cancha", 1], entonces, lo que hice es si después
                # se encuentra este tipo de casos que siga de largo y me busque al que esté en cola y lo cambie
                # de posición 2 a 1

                siguiente_indice = min(indice_en_cola + 1, len(vector_estado) - 1)
                while siguiente_indice < len(vector_estado):
                    if vector_estado[siguiente_indice][1] == "en cola":
                        vector_estado[siguiente_indice][2] = 1
                        break
                    siguiente_indice += 1
        return vector_estado

    # Esto da lo mismo si está adentro de la otra función o no, lo separé porque antes la anterior función
    # la había querido combinar con la prioridad cola y bueno quedó así separado
    def obtener_indice_en_cola(self, vector_estado):
        # Buscar el siguiente equipo en cola
        indice_en_cola = None
        for i, vector in enumerate(vector_estado):
            if isinstance(vector, list) and vector[1] == "en cola" and vector[2] == 1:
                indice_en_cola = i
                break
        return indice_en_cola

    def verificar_grupo_retirado(self, cant_grupos):
        bandera = False
        if len(self.cola) > cant_grupos:
            bandera = True

        return bandera


    def fila_calculo(self, vectorEstado):
        vector_final = ["PROMEDIO DE ESPERA", 0, 0, 0, "TASA DE LIMPIEZA", 0]

        vector_final[1] = vectorEstado[28]/vectorEstado[25]
        vector_final[2] = vectorEstado[29]/vectorEstado[26]
        vector_final[3] = vectorEstado[30]/vectorEstado[27]
        valor = (vectorEstado[31] / self.cant_partidos) * 100
        print(self.cant_partidos)
        vector_final[5] = f"{valor:.2f}%"

        return vector_final

    # Acá quise aplicar string y después pasarlo a float para usar los números pero no se puede al pasarlo a float
    # sigue mostrando una cantidad de decimales gigantes así que directamente aplicar el format en el frontend de la
    # tabla
    def redondear_a_2_decimales(self, numero):
        return round(numero, 2)
    
    def calcularProxLlegadaFutbol(self, relojActual, llegada_futbol):
        #Esta funcion calcula y devuelve en que momento va a llegar el proximo equipo de futbol

        #Coloqué este while ya que si da 1 me da error en el logaritmo
        while True:
            rnd = random.random()
            rnd_redondeado = self.redondear_a_2_decimales(rnd)
            # Check to avoid 0 and 1
            if 0 < rnd_redondeado < 1:
                break

        rnd_exponencial = rnd_redondeado

        rnd_exp = self.redondear_a_2_decimales(-(llegada_futbol) * math.log(1 - rnd_exponencial))
        return relojActual + rnd_exp, rnd_exponencial
    
    def calcularProxLlegadaHandball(self, relojActual, llegada_hand_a, llegada_hand_b):
        #Esta funcion calcula la proxima llegada de un equipo de handball
        rnd = random.random()
        rnd_redondeado = self.redondear_a_2_decimales(rnd)
        rnd_unif = llegada_hand_a + rnd_redondeado * (llegada_hand_b - llegada_hand_a)
        return self.redondear_a_2_decimales(relojActual + rnd_unif), rnd_redondeado
    
    def calcularProxLlegadaBasketball(self, relojActual, llegada_basket_a, llegada_basket_b):
        #Esta funcion calcula la proxima llegada de un equipo de basketball
        rnd = random.random()
        rnd_redondeado = self.redondear_a_2_decimales(rnd)
        rnd_unif = llegada_basket_a + rnd_redondeado * (llegada_basket_b - llegada_basket_a)
        return self.redondear_a_2_decimales(relojActual + rnd_unif), rnd_redondeado
    
    def calcularFinOcupacionFutbol(self, relojActual, ocupacion_futbol_a, ocupacion_futbol_b):
        rnd = random.random()
        rnd_redondeado = self.redondear_a_2_decimales(rnd)
        ocupacion_futbol_a = ocupacion_futbol_a / 60
        ocupacion_futbol_b = ocupacion_futbol_b / 60
        rnd_unif = ocupacion_futbol_a + rnd_redondeado * (ocupacion_futbol_b - ocupacion_futbol_a)
        return self.redondear_a_2_decimales(relojActual + rnd_unif), rnd_redondeado
    
    def calcularFinOcupacionHandball(self, relojActual, ocupacion_hand_a, ocupacion_hand_b):
        rnd = random.random()
        rnd_redondeado = self.redondear_a_2_decimales(rnd)
        ocupacion_hand_a = ocupacion_hand_a / 60
        ocupacion_hand_b = ocupacion_hand_b / 60
        rnd_unif = ocupacion_hand_a + rnd_redondeado * (ocupacion_hand_b - ocupacion_hand_a)
        return self.redondear_a_2_decimales(relojActual + rnd_unif), rnd_redondeado
    
    def calcularFinOcupacionBasketball(self, relojActual, ocupacion_basket_a, ocupacion_basket_b):
        rnd = random.random()
        rnd_redondeado = self.redondear_a_2_decimales(rnd)
        ocupacion_basket_a = ocupacion_basket_a / 60
        ocupacion_basket_b = ocupacion_basket_b / 60
        rnd_unif = ocupacion_basket_a + rnd * (ocupacion_basket_b - ocupacion_basket_a)
        return self.redondear_a_2_decimales(relojActual + rnd_unif), rnd_redondeado


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
    
