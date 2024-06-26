import math
import sys
import random

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QPushButton, QVBoxLayout, QLabel, \
    QLineEdit, QHBoxLayout, QWidget, QMessageBox, QHeaderView, QLayout, QSizePolicy, QSpacerItem
from PyQt5.QtCore import Qt
from runge_kutta import RungeKuttaWindow


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Línea de Espera")
        self.setGeometry(500, 50, 1700, 1250)  # Aumentamos el tamaño de la ventana
        self.inicial_iteraciones = "100"

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
        self.inicial_filas_mostrar = "100"
        self.inicial_fila_desde = "0"
        self.inicial_valor_t = "3"
        self.inicial_valor_m = "0.05"
        self.inicial_uniforme_a = "1"
        self.inicial_uniforme_b = "3"
        self.inicial_h = "0.1"
        # Declaro la variable cola acá para poder utilizarla en las funciones que quiera
        self.cola = []
        self.cant_partidos = 0
        self.bandera_retiro = False
        self.bandera_tiempo_ocupacion = False
        self.primeros_valores = []
        self.siguiente_valores = []
        self.tiempo_espera = []
        self.obj_en_sim = []
        self.no_borrar = False
        self.window = RungeKuttaWindow()
        self.init_main_window()

        # Guarda los valores iniciales de los campos de entrada
        self.initial_values = {
            'iteraciones': '',

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
            'fila_desde': '',
            'valor_t': '',
            'valor_m': '',
            'uniforme_a': '',
            'uniforme_b': '',
            'h': ''
        }

    def init_main_window(self):

        # Configurar fuentes
        font_title = QFont()
        font_title.setPointSize(14)
        font_title.setUnderline(True)  # Subrayado para los títulos

        # Sección SIMULACIÓN
        label_simulacion = QLabel("SIMULACIÓN")
        label_simulacion.setFont(font_title)

        # Campos adicionales
        self.iteraciones, self.iteraciones_input, self.iteraciones_label = self.create_input_field(
            "Número de iteraciones: ")
        
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

        # Campos de entrada para RUNGE KUTTA
        self.valor_t, self.valor_t_input, self.valor_t_label = self.create_input_field("Valor de t: ")
        self.valor_m, self.valor_m_input, self.valor_m_label = self.create_input_field("Valor de M: ")
        self.uniforme_a, self.uniforme_a_input, self.uniforme_a_label = self.create_input_field("Uniforme A: ")
        self.uniforme_b, self.uniforme_b_input, self.uniforme_b_label = self.create_input_field("Uniforme B: ")
        self.h, self.h_input, self.h_label = self.create_input_field("h: ")

        # Ajustar el tamaño de la letra para los campos de entrada
        font = QFont()
        font.setPointSize(11)  # Tamaño de la letra para los campos de entrada
        self.iteraciones_label.setFont(font)
        
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
        self.valor_t_label.setFont(font)
        self.valor_m_label.setFont(font)
        self.uniforme_a_label.setFont(font)
        self.uniforme_b_label.setFont(font)
        self.h_label.setFont(font)

        self.iteraciones_input.setFont(font)
      
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
        self.valor_t_input.setFont(font)
        self.valor_m_input.setFont(font)
        self.uniforme_a_input.setFont(font)
        self.uniforme_b_input.setFont(font)
        self.h_input.setFont(font)

        # Establecer el texto de los campos de entrada con los valores guardados
        self.iteraciones_input.setText(str(self.inicial_iteraciones))
        
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
        self.fila_desde_input.setText(str(self.inicial_fila_desde))
        self.valor_t_input.setText(str(self.inicial_valor_t))
        self.valor_m_input.setText(str(self.inicial_valor_m))
        self.uniforme_a_input.setText(str(self.inicial_uniforme_a))
        self.uniforme_b_input.setText(str(self.inicial_uniforme_b))
        self.h_input.setText(str(self.inicial_h))


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
        self.valor_t_input.returnPressed.connect(self.simular_action)
        self.valor_m_input.returnPressed.connect(self.simular_action)
        self.uniforme_a_input.returnPressed.connect(self.simular_action)
        self.uniforme_b_input.returnPressed.connect(self.simular_action)
        self.h_input.returnPressed.connect(self.simular_action)

        self.pushButton.setFont(font)
        self.cancelButton.setFont(font)
        # Crear un diseño vertical para organizar los diseños horizontales
        layout = QVBoxLayout()

        layout.setSizeConstraint(QLayout.SetMinAndMaxSize)

        layout.addWidget(label_simulacion)

        # Agregar espaciador vertical para empujar los campos hacia arriba
        layout.addSpacing(30)

        # Agregar los diseños horizontales al diseño vertical
        row_layout_1 = QHBoxLayout()
        row_layout_1.addWidget(self.iteraciones_label)
        row_layout_1.addWidget(self.iteraciones_input)
        

        row_layout_1.addWidget(self.llegada_futbol_label)
        row_layout_1.addWidget(self.llegada_futbol_input)
        layout.addLayout(row_layout_1)

        layout.addSpacing(30)

        row_layout_2 = QHBoxLayout()
        row_layout_2.addWidget(self.llegada_hand_a_label)
        row_layout_2.addWidget(self.llegada_hand_a_input)
        row_layout_2.addWidget(self.llegada_hand_b_label)
        row_layout_2.addWidget(self.llegada_hand_b_input)
        layout.addLayout(row_layout_2)

        layout.addSpacing(30)

        row_layout_3 = QHBoxLayout()
        row_layout_3.addWidget(self.llegada_basket_a_label)
        row_layout_3.addWidget(self.llegada_basket_a_input)
        row_layout_3.addWidget(self.llegada_basket_b_label)
        row_layout_3.addWidget(self.llegada_basket_b_input)
        layout.addLayout(row_layout_3)

        layout.addSpacing(30)

        row_layout_4 = QHBoxLayout()
        row_layout_4.addWidget(self.ocupacion_futbol_a_label)
        row_layout_4.addWidget(self.ocupacion_futbol_a_input)
        row_layout_4.addWidget(self.ocupacion_futbol_b_label)
        row_layout_4.addWidget(self.ocupacion_futbol_b_input)
        layout.addLayout(row_layout_4)

        layout.addSpacing(30)

        row_layout_5 = QHBoxLayout()
        row_layout_5.addWidget(self.ocupacion_hand_a_label)
        row_layout_5.addWidget(self.ocupacion_hand_a_input)
        row_layout_5.addWidget(self.ocupacion_hand_b_label)
        row_layout_5.addWidget(self.ocupacion_hand_b_input)
        layout.addLayout(row_layout_5)

        layout.addSpacing(30)

        row_layout_6 = QHBoxLayout()
        row_layout_6.addWidget(self.ocupacion_basket_a_label)
        row_layout_6.addWidget(self.ocupacion_basket_a_input)
        row_layout_6.addWidget(self.ocupacion_basket_b_label)
        row_layout_6.addWidget(self.ocupacion_basket_b_input)
        layout.addLayout(row_layout_6)

        layout.addSpacing(30)

        row_layout_7 = QHBoxLayout()
        row_layout_7.addWidget(self.cant_grupos_label)
        row_layout_7.addWidget(self.cant_grupos_input)
        row_layout_7.addWidget(self.filas_mostrar_label)
        row_layout_7.addWidget(self.filas_mostrar_input)
        row_layout_7.addWidget(self.fila_desde_label)
        row_layout_7.addWidget(self.fila_desde_input)
        layout.addLayout(row_layout_7)

        layout.addSpacing(30)

        # Sección RUNGE KUTTA
        label_runge_kutta = QLabel("RUNGE KUTTA")
        label_runge_kutta.setFont(font_title)
        layout.addWidget(label_runge_kutta)

        row_layout_8 = QHBoxLayout()
        row_layout_8.addWidget(self.valor_t_label)
        row_layout_8.addWidget(self.valor_t_input)
        row_layout_8.addWidget(self.valor_m_label)
        row_layout_8.addWidget(self.valor_m_input)
        layout.addLayout(row_layout_8)

        row_layout_9 = QHBoxLayout()
        row_layout_9.addWidget(self.uniforme_a_label)
        row_layout_9.addWidget(self.uniforme_a_input)
        row_layout_9.addWidget(self.uniforme_b_label)
        row_layout_9.addWidget(self.uniforme_b_input)
        row_layout_9.addWidget(self.h_label)
        row_layout_9.addWidget(self.h_input)
        layout.addLayout(row_layout_9)

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
        self.valor_t = 0
        self.valor_m = 0
        self.uniforme_a = 0
        self.uniforme_b = 0
        self.h = 0
        self.cola = []
        self.bandera_retiro = False
        self.cant_partidos = 0
        self.bandera_tiempo_ocupacion = False
        self.primeros_valores = []
        self.siguiente_valores = []
        self.tiempo_espera = []
        self.obj_en_sim = []
        self.no_borrar = False

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
        column_index = 37

        # Contador para el número de objetos
        object_count = 0

        # Índices de las columnas de interés (contando desde 0)
        columnas_interes = [2, 3, 4, 5, 6, 7, 8, 9, 10, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
                            29, 30, 31, 32, 33, 34, 35, 36, 37]

        # Lista para guardar los valores de las columnas de interés de la primera fila
        if i == 0:
            self.primeros_valores = fila[:]
        else:
            self.siguiente_valores = fila[:]

        # Itera sobre cada elemento en la fila de datos
        for idx, item in enumerate(fila):
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
                # Comparar y decidir si mostrar el valor o dejar en blanco
                if i > 0 and idx in columnas_interes and self.primeros_valores[idx] == fila[idx]:
                    item_widget = QTableWidgetItem("")
                else:
                    # Formatea el número si es un float
                    if isinstance(item, float):
                        item = f"{item:.2f}"
                    # Crea un QTableWidgetItem para el dato
                    item_widget = QTableWidgetItem(str(item))
                    # Centra el texto en la columna
                    item_widget.setTextAlignment(Qt.AlignCenter)

                # Para las columnas 23, 24 y 25, aplica la lógica especial
                if i > 0 and idx in [23, 24, 25]:
                    if self.primeros_valores[23] == fila[23]:
                        item_widget = QTableWidgetItem("")
                    else:
                        if isinstance(item, float):
                            item = f"{item:.2f}"
                        item_widget = QTableWidgetItem(str(item))
                        item_widget.setTextAlignment(Qt.AlignCenter)

                # Inserta el elemento en la tabla
                self.tableWidgetSecond.setItem(i, j, item_widget)
                # Incrementa el índice de la columna
                j += 1

        # Ajusta el número de columnas para los objetos si es necesario
        while self.tableWidgetSecond.columnCount() < column_index:
            self.tableWidgetSecond.insertColumn(self.tableWidgetSecond.columnCount())

        for col in range(self.tableWidgetSecond.columnCount()):
            self.tableWidgetSecond.setColumnWidth(col, 500)

        # Reemplaza el vector primeros_valores por siguiente_valores
        if i > 0:
            self.primeros_valores = self.siguiente_valores[:]

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

        valor_t_text = self.valor_t_input.text()
        self.inicial_valor_t = valor_t_text

        valor_m_text = self.valor_m_input.text()
        self.inicial_valor_m = valor_m_text

        uniforme_a_text = self.uniforme_a_input.text()
        self.inicial_uniforme_a = uniforme_a_text

        uniforme_b_text = self.uniforme_b_input.text()
        self.inicial_uniforme_b = uniforme_b_text

        h_text = self.h_input.text()
        self.inicial_h = h_text

        # Validar que todos los campos estén completados
        if (not iteraciones_text  or not llegada_futbol_text or not llegada_hand_a_text or
                not llegada_hand_b_text or not llegada_basket_a_text or not llegada_basket_b_text or
                not ocupacion_futbol_a_text or not ocupacion_futbol_b_text or not ocupacion_hand_a_text or
                not ocupacion_hand_b_text or not ocupacion_basket_a_text or not ocupacion_basket_b_text or
                not cant_grupos_text or not filas_mostrar_text or not fila_desde_text or not valor_t_text or not valor_m_text
        or not uniforme_a_text or not uniforme_b_text or not h_text):
            QMessageBox.warning(self, 'Campos incompletos', 'Por favor, complete todos los campos.')
            return

        # Convertir los textos a los tipos adecuados
        try:
            iteraciones = int(iteraciones_text)
           
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
            valor_t = float(valor_t_text)
            valor_m = float(valor_m_text)
            uniforme_a = float(uniforme_a_text)
            uniforme_b = float(uniforme_b_text)
            h = float(h_text)

        except ValueError:
            QMessageBox.warning(self, 'Valor inválido',
                                'Por favor, ingrese valores numéricos válidos en todos los campos.')
            return

        # Validaciones adicionales
        if (iteraciones <= 0 or llegada_futbol <= 0 or llegada_hand_a <= 0 or llegada_hand_b <= 0 or
                llegada_basket_a <= 0 or llegada_basket_b <= 0 or ocupacion_futbol_a < 0 or ocupacion_futbol_b < 0 or
                ocupacion_hand_a < 0 or ocupacion_hand_b < 0 or ocupacion_basket_a < 0 or ocupacion_basket_b < 0 or
                filas_mostrar < 0 or fila_desde < 0 or valor_t < 0 or valor_m < 0 or uniforme_a < 0 or uniforme_b < 0
        or h < 0):
            QMessageBox.warning(self, 'Valores no permitidos', 'Por favor, ingrese valores mayores a cero. ')
            return

        # Validación de iteraciones máximas
        if iteraciones > 100000:
            QMessageBox.warning(self, 'Iteraciones máximas excedidas',
                                'El número de iteraciones no puede ser mayor a 100000.')
            return

        # Llamar a la función para inicializar la segunda página
        self.init_second_page2(iteraciones, llegada_futbol, llegada_hand_a, llegada_hand_b, llegada_basket_a,
                               llegada_basket_b, ocupacion_futbol_a, ocupacion_futbol_b, ocupacion_hand_a,
                               ocupacion_hand_b,
                               ocupacion_basket_a, ocupacion_basket_b, cant_grupos, filas_mostrar, fila_desde, valor_t,
                               valor_m, uniforme_a, uniforme_b, h)

    def init_second_page2(self, iteraciones, llegada_futbol, llegada_hand_a, llegada_hand_b, llegada_basket_a,
                          llegada_basket_b, ocupacion_futbol_a, ocupacion_futbol_b, ocupacion_hand_a,
                          ocupacion_hand_b, ocupacion_basket_a, ocupacion_basket_b, cant_grupos, filas_mostrar,
                          fila_desde, valor_t, valor_m, uniforme_a, uniforme_b, h):
        self.tableWidgetSecond = QTableWidget(self)
        self.tableWidgetSecond.setColumnCount(37)
        self.tableWidgetSecond.setHorizontalHeaderLabels(
            ["Evento", "Reloj", "Fútbol RND", "Fútbol Tiempo entre Llegadas", "Fútbol Próxima Llegada", "Hand RND",
             "Hand Tiempo entre Llegadas", "Hand Próxima Llegada", "Basket RND",
             "Basket Tiempo entre Llegadas", "Basket Próxima Llegada", "Cola Cancha", "Grupo Retirado", "Estado Cancha",
             "Fútbol RND", "Fútbol Tiempo de Ocupación", "Fútbol Fin Ocupación", "Hand RND", "Hand Tiempo de Ocupación",
             "Hand Fin Ocupación", "Basket RND", "Basket Tiempo de Ocupación",
             "Basket Fin Ocupación","RND", "Nivel de Mantenimiento", "Tiempo de Limpieza", "Tiempo Fin Ocupación",
             "Tiempo de Espera", "Cantidad Grupos Fútbol", "Cantidad Grupos Hand",
             "Cantidad Grupos Basket", "Fútbol Tiempo de espera acumulado", "Hand Tiempo de espera acumulado",
             "Basket Tiempo de espera acumulado", "Tiempo de limpieza acumulado", "Cantidad Grupos Retirados",
             "Cantidad de Partidos Jugados"])

        self.iniciar_simulacion(iteraciones, llegada_futbol, llegada_hand_a, llegada_hand_b, llegada_basket_a,
                                llegada_basket_b, ocupacion_futbol_a, ocupacion_futbol_b, ocupacion_hand_a,
                                ocupacion_hand_b, ocupacion_basket_a, ocupacion_basket_b, cant_grupos, filas_mostrar,
                                fila_desde, valor_t, valor_m, uniforme_a, uniforme_b, h)

        self.backButton = QPushButton("Volver", self)
        self.rungeKuttaButton = QPushButton("Runge Kutta", self)
        self.backButton.setGeometry(250, 540, 100, 30)
        self.rungeKuttaButton.setGeometry(370, 540, 120, 30)
        self.backButton.clicked.connect(self.show_main_page)
        self.rungeKuttaButton.clicked.connect(self.open_runge_kutta_window)


        font = QFont()
        font.setPointSize(11)
        self.backButton.setFont(font)
        self.rungeKuttaButton.setFont(font)
        self.tableWidgetSecond.setFont(font)
        self.tableWidgetSecond.horizontalHeader().setFont(font)
        layout_vertical = QVBoxLayout()  # Layout vertical principal
        layout_horizontal = QHBoxLayout()  # Layout horizontal para los botones

        layout_horizontal.addWidget(self.backButton)
        layout_horizontal.addWidget(self.rungeKuttaButton)

        layout_vertical.addWidget(self.tableWidgetSecond)
        layout_vertical.addLayout(layout_horizontal)
        second_page_widget = QWidget()
        second_page_widget.setLayout(layout_vertical)
        self.setCentralWidget(second_page_widget)

    def show_main_page(self):
        self.init_main_window()

    def open_runge_kutta_window(self):
        self.window.show()


    # Aca empece a modificar

    def iniciar_simulacion(self, iteraciones, llegada_futbol, llegada_hand_a, llegada_hand_b,
                           llegada_basket_a,
                           llegada_basket_b, ocupacion_futbol_a, ocupacion_futbol_b, ocupacion_hand_a,
                           ocupacion_hand_b, ocupacion_basket_a, ocupacion_basket_b, cant_grupos, filas_mostrar,
                           fila_desde, valor_t, valor_m, uniforme_a, uniforme_b, h):

        ocupacion_futbol_a = ocupacion_futbol_a / 60
        ocupacion_futbol_b = ocupacion_futbol_b / 60
        ocupacion_hand_a = ocupacion_hand_a / 60
        ocupacion_hand_b = ocupacion_hand_b / 60
        ocupacion_basket_a = ocupacion_basket_a / 60
        ocupacion_basket_b = ocupacion_basket_b / 60

        # Defini este vector estado con el excel, lo unico que en vez de hacer tantas columnas para calcular la llegada de los equipos hice una por equipo, al igual que la ocupacion
        # Para la ocupacion, solo muestro cuando se va a desocupar (en tiempo) y que equipo la esta ocupando, para ahorrar columnas, porque solo un equipo ocupa la cancha a la vez
        tiempo_llegada_futbol, rnd_futbol_llegada = self.calcularProxLlegadaFutbol(0, llegada_futbol)
        tiempo_llegada_hand, rnd_hand_llegada = self.calcularProxLlegadaHandball(0, llegada_hand_a, llegada_hand_b)
        tiempo_llegada_basket, rnd_basket_llegada = self.calcularProxLlegadaBasketball(0, llegada_basket_a,
                                                                                       llegada_basket_b)
        # EVENTO  #RELOJ #RND #TIEMPO ENTRE LLEGADAS #LLEGADA
        vectorEstado = ["Inicio", 0, rnd_futbol_llegada, 0, tiempo_llegada_futbol, rnd_hand_llegada, 0,
                        tiempo_llegada_hand,
                        rnd_basket_llegada, 0, tiempo_llegada_basket, 0, "", "Libre", 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                        0, 0, 0, 0, 0, 0, 0, 0, 0]

        # Si fila_desde es 0, incluir el estado inicial en la tabla
        if fila_desde == 0:
            self.insertar_en_tabla(vectorEstado)

        # Variables para controlar la iteración desde fila_desde
        se_alcanzo_fila_desde = False
        primera_iteracion_fila_desde = None

        

        resultados = self.runge_kutta2(valor_t, valor_m, h, uniforme_a, uniforme_b)

        # Todo esto iria en un for o en un while que vaya iterando en el tiempo
        # después en 5 debería ir la variable iteraciones
        for i in range(iteraciones):
            prox_reloj, nombre_proxEvento = self.proximoEvento(vectorEstado)
            # Asignamos el valor de prox_reloj al reloj actual y tambien el nombre del evento
            vectorEstado[0] = nombre_proxEvento
            vectorEstado[1] = prox_reloj
            # Acá voy viendo el tamaño que tiene el vector cola, en la primera iteración 0 va a dar bien y va a
            # a estar en 0, luego para actualizar este contador en fin ocupación y descontarlo también
            # lo actualicé en esos casos
            vectorEstado[11] = len(self.cola)

            # Verificar si se alcanzó la fila desde
            if prox_reloj >= fila_desde and not se_alcanzo_fila_desde:
                se_alcanzo_fila_desde = True
                primera_iteracion_fila_desde = i

            if se_alcanzo_fila_desde and (i >= primera_iteracion_fila_desde and i <= filas_mostrar):
                self.no_borrar = True
            else:
                self.no_borrar = False

            if i > filas_mostrar:
                vectorEstado = vectorEstado[:37]

            # Verifico que el vector cola sea mayor a 2 ya que no puedo ejecutar la función porque es solo
            # para la prioridad en el caso de que basketball se encuentre en la posición 1 del vector
            if len(self.cola) > 2:
                # La función me va a devolver por ejemplo: si tengo el vector cola como
                # cola = ["futbol", "basketball", "handball"]
                # me va a devolver: cola = ["futbol", "handball", "basketball"]
                self.verificar_prioridad_cola()

            if i == 0 or self.bandera_tiempo_ocupacion == True:
                if (nombre_proxEvento == "Llegada futbol"):
                    # Aca iria la logica si llega un equipo de futbol
                    # Primero calculamos la proxima llegada de un equipo de futbol

                    vectorEstado[3], vectorEstado[2] = self.calcularProxLlegadaFutbol(vectorEstado[1], llegada_futbol)

                    vectorEstado[4] = vectorEstado[3] + prox_reloj

                    vectorEstado[13] = "Ocupado"

                    # luego calculo cuanto tiempo va a ocupar la cancha pero me falta el if que si no esta ocupada la cancha
                    vectorEstado[15], vectorEstado[14] = self.calcularFinOcupacionFutbol(vectorEstado[1],
                                                                                         ocupacion_futbol_a,
                                                                                         ocupacion_futbol_b)
                    vectorEstado[16] = vectorEstado[15] + prox_reloj

                    # APLICACIÓN DEL RUNGE KUTTA
                    #vectorEstado[24], vectorEstado[23] = self.calcular_uniforme_dif(uniforme_a, uniforme_b)
                    #if vectorEstado[24] == 1:
                    #    vectorEstado[25] = resultados[0]
                    #elif vectorEstado[24] == 2:
                    #    vectorEstado[25] = resultados[1]
                    #elif vectorEstado[24] == 3:
                    #    vectorEstado[25] = resultados[2]

                    # Aplicacion del rounge kutta 2
                    vectorEstado[24], vectorEstado[23] = self.calcular_uniforme_dif(uniforme_a, uniforme_b)
                    uniforme_a = int(uniforme_a)
                    uniforme_b = int(uniforme_b)
                    cant_niveles = uniforme_b - uniforme_a
                    for i in range(cant_niveles + 1):
                        if vectorEstado[24] == i+uniforme_a:
                            vectorEstado[25] = resultados[i]

                    vectorEstado[26] = vectorEstado[16] + vectorEstado[25]
                    vectorEstado[34] += vectorEstado[25]
                    vectorEstado[12] = "NO"
                    self.bandera_tiempo_ocupacion = False

                    objeto = ["futbol", "en cancha", vectorEstado[11]]
                    self.obj_en_sim.append(objeto)
                    # Voy agregando los nombres al vector cola
                    self.cola.append(objeto[0])
                    vectorEstado[28] += 1
                elif (nombre_proxEvento == "Llegada handball"):
                    # Aca iria la logica si llega handball

                    vectorEstado[6], vectorEstado[5] = self.calcularProxLlegadaHandball(vectorEstado[1], llegada_hand_a,
                                                                                        llegada_hand_b)

                    vectorEstado[7] = vectorEstado[6] + prox_reloj

                    vectorEstado[13] = "Ocupado"

                    # luego calculo cuanto tiempo va a ocupar la cancha
                    vectorEstado[18], vectorEstado[17] = self.calcularFinOcupacionHandball(vectorEstado[1],
                                                                                           ocupacion_hand_a,
                                                                                           ocupacion_hand_b)
                    vectorEstado[19] = vectorEstado[18] + prox_reloj

                    # APLICACIÓN DEL RUNGE KUTTA
                    #vectorEstado[24], vectorEstado[23] = self.calcular_uniforme_dif(uniforme_a, uniforme_b)
                    #if vectorEstado[24] == 1:
                    #    vectorEstado[25] = resultados[0]
                    #elif vectorEstado[24] == 2:
                    #    vectorEstado[25] = resultados[1]
                    #elif vectorEstado[24] == 3:
                    #    vectorEstado[25] = resultados[2]

                    # Aplicacion del rounge kutta 2
                    vectorEstado[24], vectorEstado[23] = self.calcular_uniforme_dif(uniforme_a, uniforme_b)
                    uniforme_a = int(uniforme_a)
                    uniforme_b = int(uniforme_b)
                    cant_niveles = uniforme_b - uniforme_a
                    for i in range(cant_niveles + 1):
                        if vectorEstado[24] == i+uniforme_a:
                            vectorEstado[25] = resultados[i]

                    vectorEstado[26] = vectorEstado[19] + vectorEstado[25]
                    vectorEstado[34] += vectorEstado[25]
                    vectorEstado[12] = "NO"

                    self.bandera_tiempo_ocupacion = False
                    objeto = ["handball", "en cancha", vectorEstado[11]]
                    self.obj_en_sim.append(objeto)
                    # Voy agregando los nombres al vector cola
                    self.cola.append(objeto[0])
                    vectorEstado[29] += 1

                elif (nombre_proxEvento == "Llegada basketball"):
                    # Aca iria la logica si llega un equipo de basketball

                    vectorEstado[9], vectorEstado[8] = self.calcularProxLlegadaBasketball(vectorEstado[1],
                                                                                          llegada_basket_a,
                                                                                          llegada_basket_b)

                    vectorEstado[10] = vectorEstado[9] + prox_reloj

                    vectorEstado[13] = "Ocupado"

                    # luego calculo cuanto tiempo va a ocupar la cancha
                    vectorEstado[21], vectorEstado[20] = self.calcularFinOcupacionHandball(vectorEstado[1],
                                                                                           ocupacion_basket_a,
                                                                                           ocupacion_basket_b)
                    vectorEstado[22] = vectorEstado[21] + prox_reloj

                    # APLICACIÓN DEL RUNGE KUTTA
                    #vectorEstado[24], vectorEstado[23] = self.calcular_uniforme_dif(uniforme_a, uniforme_b)
                    #if vectorEstado[24] == 1:
                    #    vectorEstado[25] = resultados[0]
                    #elif vectorEstado[24] == 2:
                    #    vectorEstado[25] = resultados[1]
                    #elif vectorEstado[24] == 3:
                    #    vectorEstado[25] = resultados[2]

                    # Aplicacion del rounge kutta 2
                    vectorEstado[24], vectorEstado[23] = self.calcular_uniforme_dif(uniforme_a, uniforme_b)
                    uniforme_a = int(uniforme_a)
                    uniforme_b = int(uniforme_b)
                    cant_niveles = uniforme_b - uniforme_a
                    for i in range(cant_niveles + 1):
                        if vectorEstado[24] == i+uniforme_a:
                            vectorEstado[25] = resultados[i]

                    vectorEstado[26] = vectorEstado[22] + vectorEstado[25]
                    vectorEstado[34] += vectorEstado[25]
                    vectorEstado[12] = "NO"

                    self.bandera_tiempo_ocupacion = False
                    objeto = ["basketball", "en cancha", vectorEstado[11]]
                    self.obj_en_sim.append(objeto)
                    # Voy agregando los nombres al vector cola
                    self.cola.append(objeto[0])
                    vectorEstado[30] += 1

            elif i > 0:
                retiro = self.verificar_grupo_retirado(cant_grupos)

                if (nombre_proxEvento == "Llegada futbol"):
                    if retiro == False:
                        vectorEstado[3], vectorEstado[2] = self.calcularProxLlegadaFutbol(vectorEstado[1],
                                                                                          llegada_futbol)

                        vectorEstado[4] = vectorEstado[3] + prox_reloj

                        objeto = ["futbol", "en cola", vectorEstado[11]]
                        self.obj_en_sim.append(objeto)
                        # Voy agregando los nombres al vector cola
                        self.cola.append(objeto[0])
                        self.tiempo_espera.append(prox_reloj)
                        vectorEstado[28] += 1
                        vectorEstado[12] = "NO"

                    else:
                        vectorEstado[3], vectorEstado[2] = self.calcularProxLlegadaFutbol(vectorEstado[1],
                                                                                          llegada_futbol)
                        vectorEstado[4] = vectorEstado[3] + prox_reloj
                        vectorEstado[12] = "SI"
                        vectorEstado[35] += 1

                elif (nombre_proxEvento == "Llegada handball"):
                    if retiro == False:
                        vectorEstado[6], vectorEstado[5] = self.calcularProxLlegadaHandball(vectorEstado[1],
                                                                                            llegada_hand_a,
                                                                                            llegada_hand_b)

                        vectorEstado[7] = vectorEstado[6] + prox_reloj

                        objeto = ["handball", "en cola", vectorEstado[11]]
                        self.obj_en_sim.append(objeto)
                        # Voy agregando los nombres al vector cola
                        self.cola.append(objeto[0])
                        self.tiempo_espera.append(prox_reloj)
                        vectorEstado[29] += 1
                        vectorEstado[12] = "NO"

                    else:
                        vectorEstado[6], vectorEstado[5] = self.calcularProxLlegadaHandball(vectorEstado[1],
                                                                                            llegada_hand_a,
                                                                                            llegada_hand_b)
                        vectorEstado[7] = vectorEstado[6] + prox_reloj
                        vectorEstado[12] = "SI"
                        vectorEstado[35] += 1

                elif (nombre_proxEvento == "Llegada basketball"):
                    if retiro == False:
                        vectorEstado[9], vectorEstado[8] = self.calcularProxLlegadaBasketball(vectorEstado[1],
                                                                                              llegada_basket_a,
                                                                                              llegada_basket_b)

                        vectorEstado[10] = vectorEstado[9] + prox_reloj

                        objeto = ["basketball", "en cola", vectorEstado[11]]
                        self.obj_en_sim.append(objeto)
                        # Voy agregando los nombres al vector cola
                        self.cola.append(objeto[0])
                        self.tiempo_espera.append(prox_reloj)
                        vectorEstado[30] += 1
                        vectorEstado[12] = "NO"

                    else:
                        vectorEstado[9], vectorEstado[8] = self.calcularProxLlegadaBasketball(vectorEstado[1],
                                                                                              llegada_basket_a,
                                                                                              llegada_basket_b)
                        vectorEstado[10] = vectorEstado[9] + prox_reloj
                        vectorEstado[12] = "SI"
                        vectorEstado[35] += 1


                elif (nombre_proxEvento == "Fin Ocupacion futbol") or (
                        nombre_proxEvento == "Fin Ocupacion handball") or (
                        nombre_proxEvento == "Fin Ocupacion basketball"):

                    if len(self.cola) == 1:
                        self.actualizar_vectores(self.obj_en_sim)
                        # Esto se ejecuta SOLAMENTE cuando resulta el caso de que entra un equipo en cancha y sale antes
                        # de cualquier llegada por lo tanto solo actualizo vector
                        vectorEstado[12] = "NO"
                        vectorEstado[13] = "Libre"
                        self.cant_partidos += 1
                        vectorEstado[36] = self.cant_partidos
                        self.cola.pop(0)
                        vectorEstado[11] = len(self.cola)
                        self.bandera_tiempo_ocupacion = True

                    # Acá lo que hago es verificar qué equipo está en posición 1 en la cola para poder calcular
                    # el tiempo de ocupación de ese equipo en la misma fila que apareció el evento Fin Ocupación
                    # del equipo que estaba en posición 0
                    elif self.cola[1] == "futbol":
                        vectorEstado[15], vectorEstado[14] = self.calcularFinOcupacionFutbol(vectorEstado[1],
                                                                                             ocupacion_futbol_a,
                                                                                             ocupacion_futbol_b)
                        vectorEstado[16] = vectorEstado[15] + prox_reloj

                        # APLICACIÓN DEL RUNGE KUTTA
                        #vectorEstado[24], vectorEstado[23] = self.calcular_uniforme_dif(uniforme_a, uniforme_b)
                        #if vectorEstado[24] == 1:
                        #    vectorEstado[25] = resultados[0]
                        #elif vectorEstado[24] == 2:
                        #    vectorEstado[25] = resultados[1]
                        #elif vectorEstado[24] == 3:
                        #    vectorEstado[25] = resultados[2]

                        # Aplicacion del rounge kutta 2
                        vectorEstado[24], vectorEstado[23] = self.calcular_uniforme_dif(uniforme_a, uniforme_b)
                        uniforme_a = int(uniforme_a)
                        uniforme_b = int(uniforme_b)
                        cant_niveles = uniforme_b - uniforme_a
                        for i in range(cant_niveles+1):
                            if vectorEstado[24] == i+uniforme_a:
                                vectorEstado[25] = resultados[i]

                        vectorEstado[26] = vectorEstado[16] + vectorEstado[25]
                        vectorEstado[34] += vectorEstado[25]
                        vectorEstado[12] = "NO"
                        # Acá llamo a esta función ya que si llegó este evento de fin ocupación debo pasar el equipo
                        # que termino de ocupar a destruido y el que estaba en posición 1 a que esté en cancha
                        # y además actualizar las posiciones de los demás objetos en cola
                        self.actualizar_vectores(self.obj_en_sim)

                        vectorEstado[27] = prox_reloj - self.tiempo_espera[0]
                        tiempo_espera_futbol = vectorEstado[27]
                        vectorEstado[31] += tiempo_espera_futbol

                        self.tiempo_espera.pop(0)
                        # borro en el vector cola el equipo en posición 0 ya que termino de ocupar la cancha
                        self.cola.pop(0)
                        # actualizo el contador cola porque uno que estaba en fila entro a la cancha
                        vectorEstado[11] = len(self.cola) - 1

                        self.cant_partidos += 1
                        vectorEstado[36] = self.cant_partidos

                    elif self.cola[1] == "handball":
                        vectorEstado[18], vectorEstado[17] = self.calcularFinOcupacionHandball(vectorEstado[1],
                                                                                               ocupacion_hand_a,
                                                                                               ocupacion_hand_b)
                        vectorEstado[19] = vectorEstado[18] + prox_reloj

                        # APLICACIÓN DEL RUNGE KUTTA
                        #vectorEstado[24], vectorEstado[23] = self.calcular_uniforme_dif(uniforme_a, uniforme_b)
                        #if vectorEstado[24] == 1:
                        #    vectorEstado[25] = resultados[0]
                        #elif vectorEstado[24] == 2:
                        #    vectorEstado[25] = resultados[1]
                        #elif vectorEstado[24] == 3:
                        #    vectorEstado[25] = resultados[2]

                        # Aplicacion del rounge kutta 2
                        vectorEstado[24], vectorEstado[23] = self.calcular_uniforme_dif(uniforme_a, uniforme_b)
                        uniforme_a = int(uniforme_a)
                        uniforme_b = int(uniforme_b)
                        cant_niveles = uniforme_b - uniforme_a
                        for i in range(cant_niveles+1):
                            if vectorEstado[24] == i+uniforme_a:
                                vectorEstado[25] = resultados[i]

                        vectorEstado[26] = vectorEstado[19] + vectorEstado[25]
                        vectorEstado[34] += vectorEstado[25]
                        vectorEstado[12] = "NO"
                        self.actualizar_vectores(self.obj_en_sim)

                        vectorEstado[27] = prox_reloj - self.tiempo_espera[0]
                        tiempo_espera_hand = vectorEstado[27]
                        vectorEstado[32] += tiempo_espera_hand

                        self.tiempo_espera.pop(0)
                        self.cola.pop(0)
                        vectorEstado[11] = len(self.cola) - 1
                        self.cant_partidos += 1
                        vectorEstado[36] = self.cant_partidos

                    elif self.cola[1] == "basketball":
                        vectorEstado[21], vectorEstado[20] = self.calcularFinOcupacionHandball(vectorEstado[1],
                                                                                               ocupacion_hand_a,
                                                                                               ocupacion_hand_b)
                        vectorEstado[22] = vectorEstado[21] + prox_reloj

                        # APLICACIÓN DEL RUNGE KUTTA
                        #vectorEstado[24], vectorEstado[23] = self.calcular_uniforme_dif(uniforme_a, uniforme_b)
                        #if vectorEstado[24] == 1:
                        #    vectorEstado[25] = resultados[0]
                        #elif vectorEstado[24] == 2:
                        #    vectorEstado[25] = resultados[1]
                        #elif vectorEstado[24] == 3:
                        #    vectorEstado[25] = resultados[2]

                        # Aplicacion del rounge kutta 2
                        vectorEstado[24], vectorEstado[23] = self.calcular_uniforme_dif(uniforme_a, uniforme_b)
                        uniforme_a = int(uniforme_a)
                        uniforme_b = int(uniforme_b)
                        cant_niveles = uniforme_b - uniforme_a
                        for i in range(cant_niveles+1):
                            if vectorEstado[24] == i+uniforme_a:
                                vectorEstado[25] = resultados[i]

                        vectorEstado[26] = vectorEstado[22] + vectorEstado[25]
                        vectorEstado[34] += vectorEstado[25]
                        vectorEstado[12] = "NO"
                        self.actualizar_vectores(self.obj_en_sim)

                        vectorEstado[27] = prox_reloj - self.tiempo_espera[0]
                        tiempo_espera_basket = vectorEstado[27]
                        vectorEstado[33] += tiempo_espera_basket

                        self.tiempo_espera.pop(0)
                        self.cola.pop(0)
                        vectorEstado[11] = len(self.cola) - 1
                        self.cant_partidos += 1
                        vectorEstado[36] = self.cant_partidos

            # Verificar si estamos dentro del rango de filas a mostrar
            if se_alcanzo_fila_desde and (i >= primera_iteracion_fila_desde and i <= filas_mostrar):
                if len(vectorEstado) == 34:
                    vectorEstado.extend(self.obj_en_sim)
                    self.insertar_en_tabla(vectorEstado)
                else:
                    vectorEstado = vectorEstado[:37]
                    vectorEstado.extend(self.obj_en_sim)
                    self.insertar_en_tabla(vectorEstado)

            elif i == iteraciones - 1:

                self.insertar_en_tabla(vectorEstado)

                vectorCalculo = self.fila_calculo(vectorEstado)
                self.agregar_fila_flotante(vectorCalculo)


    def runge_kutta(self,valor_t, valor_m, h, valor_a, valor_b):
        vector_runge = [0, 0, 0, 0, 0, 0, 0, 0]
        resultados = []

        while True:

            self.window.insertar_en_tabla_runge(vector_runge)

            # Guardar vector[0] si vector[1] alcanza los umbrales 1, 2, 3
            if vector_runge[1] >= 1 and len(resultados) == 0:
                tiempo = vector_runge[0] * 0.1
                resultados.append(tiempo)
            if vector_runge[1] >= 2 and len(resultados) == 1:
                tiempo = vector_runge[0] * 0.1
                resultados.append(tiempo)
            if vector_runge[7] >= 3 and len(resultados) == 2:
                tiempo = vector_runge[6] * 0.1
                resultados.append(tiempo)

            print(resultados)

            vector_runge[0] = vector_runge[6]
            vector_runge[1] = vector_runge[7]

            # Actualizar vector_runge según las fórmulas de Runge-Kutta
            vector_runge[2] = valor_t * vector_runge[0] + valor_m * vector_runge[1] * (vector_runge[0] ** 2)
            vector_runge[3] = valor_t * (vector_runge[0] + h / 2) + valor_m * (vector_runge[1] + (h / 2) * vector_runge[2]) * (
                        (vector_runge[0] + h / 2) ** 2)
            vector_runge[4] = valor_t * (vector_runge[0] + h / 2) + valor_m * (vector_runge[1] + (h / 2) * vector_runge[3]) * (
                        (vector_runge[0] + h / 2) ** 2)
            vector_runge[5] = valor_t * (vector_runge[0] + h/2) + valor_m * (vector_runge[1] + h * vector_runge[4]) * ((vector_runge[0] + h/2) ** 2)

            vector_runge[6] = vector_runge[0] + h
            vector_runge[7] = vector_runge[1] + (h / 6) * (vector_runge[2] + 2 * vector_runge[2] + 2 * vector_runge[2] + vector_runge[2])

            # Verificar si vector_runge[1] ha alcanzado o superado 3
            if vector_runge[1] > 3:
                break

        return resultados
    
    def runge_kutta2(self,valor_t, valor_m, h, valor_a, valor_b):
        vector_runge = [0, 0, 0, 0, 0, 0, 0, 0]
        resultados = []
        valor_a = int(valor_a)
        valor_b = int(valor_b)

        while True:

            self.window.insertar_en_tabla_runge(vector_runge)

            # Guardar vector[0] si vector[1] alcanza los umbrales 1, 2, 3
            #if vector_runge[1] >= 1 and len(resultados) == 0:
            #    tiempo = vector_runge[0] * 0.1
            #    resultados.append(tiempo)
            #if vector_runge[1] >= 2 and len(resultados) == 1:
            #    tiempo = vector_runge[0] * 0.1
            #    resultados.append(tiempo)
            #if vector_runge[7] >= 3 and len(resultados) == 2:
            #    tiempo = vector_runge[6] * 0.1
            #    resultados.append(tiempo)

            cantidad = valor_b - valor_a

            #Primero tengo que buscar el valor de A en la tabla para empezar a iterar desde ahi
            empezar = False
            if vector_runge[1] >= valor_a:
                empezar = True

            if (empezar):
                for i in range(cantidad+1):
                    if vector_runge[1] >= valor_a + i and len(resultados) == i:
                        tiempo = (vector_runge[0] * 10) / 60
                        resultados.append(tiempo)

            print(resultados)

            vector_runge[0] = vector_runge[6]
            vector_runge[1] = vector_runge[7]

            # Actualizar vector_runge según las fórmulas de Runge-Kutta
            vector_runge[2] = valor_t * vector_runge[0] + valor_m * vector_runge[1] * (vector_runge[0] ** 2)
            vector_runge[3] = valor_t * (vector_runge[0] + h / 2) + valor_m * (vector_runge[1] + (h / 2) * vector_runge[2]) * (
                        (vector_runge[0] + h / 2) ** 2)
            vector_runge[4] = valor_t * (vector_runge[0] + h / 2) + valor_m * (vector_runge[1] + (h / 2) * vector_runge[3]) * (
                        (vector_runge[0] + h / 2) ** 2)
            vector_runge[5] = valor_t * (vector_runge[0] + h/2) + valor_m * (vector_runge[1] + h * vector_runge[4]) * ((vector_runge[0] + h/2) ** 2)

            vector_runge[6] = vector_runge[0] + h
            vector_runge[7] = vector_runge[1] + (h / 6) * (vector_runge[2] + 2 * vector_runge[2] + 2 * vector_runge[2] + vector_runge[2])

            # Verificar si vector_runge[1] ha alcanzado o superado 3
            if len(resultados) == cantidad + 1:
                break

        return resultados

    def proximoEvento(self, vectorEstado):
        proximoRelojLlegada = [vectorEstado[4], vectorEstado[7], vectorEstado[10], vectorEstado[26]]

        # Todo este if lo unico que hace es no devolver como primer evento el fin de ocupacion, cuando vale 0 en la primer "fila" de la tabla
        # en el evento de "Inicio"
        if vectorEstado[26] > 0 and self.bandera_tiempo_ocupacion == False:

            # Encontrar el índice del valor mínimo en proximoRelojLlegada
            indice_minimo = proximoRelojLlegada.index(min(proximoRelojLlegada))

            nombres_reloj = ["Llegada futbol", "Llegada handball", "Llegada basketball", "Fin Ocupacion"]

            # Acá lo que hago es que si llegue al evento Fin Ocupación debo saber cuál de todos los equipos
            # terminó de desocupar la cancha por eso concateno la string que está en la posición 0 en el vector cola
            if len(self.cola) > 0:
                # Añadir la primera palabra del subvector a "Fin Ocupacion"
                nombres_reloj[3] += " " + self.cola[0]

            nombre_reloj_minimo = nombres_reloj[indice_minimo]

        elif vectorEstado[26] > 0 and self.bandera_tiempo_ocupacion == True:
            # Encontrar el índice del valor mínimo en proximoRelojLlegada
            indice_minimo = proximoRelojLlegada.index(
                min(proximoRelojLlegada[0], proximoRelojLlegada[1], proximoRelojLlegada[2]))

            # Asignar nombres de reloj según el índice
            nombres_reloj = ["Llegada futbol", "Llegada handball", "Llegada basketball"]
            nombre_reloj_minimo = nombres_reloj[indice_minimo]

            # Devolver el número de reloj y el nombre del próximo evento
        elif vectorEstado[26] == 0 and self.bandera_tiempo_ocupacion == False:
            # Encontrar el índice del valor mínimo en proximoRelojLlegada
            indice_minimo = proximoRelojLlegada.index(
                min(proximoRelojLlegada[0], proximoRelojLlegada[1], proximoRelojLlegada[2]))

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

            if self.no_borrar == False:
                # Eliminar el vector que ha sido destruido
                del vector_estado[indice_en_cancha]

            vector_estado = self.verificar_prioridad_objeto(vector_estado)

            # Verificar si no hay equipo en posición 0 y en cancha
            if all(vector[1] != "en cancha" for vector in vector_estado if isinstance(vector, list) and vector[2] == 1):
                # Buscar el siguiente equipo en cola con la posición más baja
                indice_en_cola = None
                posicion_en_cola_minima = float('inf')  # Inicializar con un valor grande
                for i, vector in enumerate(vector_estado):
                    if isinstance(vector, list) and vector[1] == "en cola" and vector[2] < posicion_en_cola_minima and \
                            vector[2] > 0:
                        indice_en_cola = i
                        posicion_en_cola_minima = vector[2]

                # Mover el equipo en cola con la posición más baja a la cancha
                if indice_en_cola is not None:
                    vector_estado[indice_en_cola][1] = "en cancha"
                    vector_estado[indice_en_cola][2] = 0

                equipos_basketball = [vector for vector in vector_estado if
                                      isinstance(vector, list) and vector[0] == "basketball" and vector[1] == "en cola"]
                if len(equipos_basketball) > 1:
                    primer_basket_en_cancha = any(
                        isinstance(vector, list) and vector[1] == "en cancha" and vector[0] == "basketball" for vector
                        in vector_estado
                    )

                    anterior_basket_en_cola = next(
                        (i for i, vector in enumerate(vector_estado)
                         if
                         isinstance(vector, list) and vector[1] == "en cola" and vector[0] == "basketball" and vector[
                             2] == 1),
                        None
                    )

                    for vector in vector_estado:
                        if isinstance(vector, list) and vector[1] == "en cola" and vector[2] > 0:

                            if vector in equipos_basketball and not primer_basket_en_cancha and anterior_basket_en_cola == None:
                                vector[2] -= 1
                            elif vector in equipos_basketball and primer_basket_en_cancha:
                                vector[2] -= 1
                            elif vector not in equipos_basketball:
                                vector[2] -= 1

                    # Reajustar las posiciones de los equipos de basketball consecutivos
                    if len(equipos_basketball) > 1 and equipos_basketball[0][2] == 1:
                        for i in range(1, len(equipos_basketball)):
                            equipos_basketball[i][2] = equipos_basketball[i - 1][2] + 1


                        # Aplicar los cambios de equipos_basketball a vector_estado
                        for vector in vector_estado:
                            for equipo in equipos_basketball:
                                if vector == equipo:
                                    vector[2] = equipo[2]

                else:
                    for vector in vector_estado:
                        if isinstance(vector, list) and vector[1] == "en cola" and vector[2] > 0:
                            vector[2] -= 1

        return vector_estado

    def verificar_prioridad_cola(self):
        # Verificar si hay al menos un equipo de baloncesto seguido por futbol o handball
        for i in range(1, len(self.cola)):
            if self.cola[i] == "basketball":
                # Buscar el primer equipo de futbol o handball después del primer equipo de baloncesto
                for j in range(i + 1, len(self.cola)):
                    if self.cola[j] in ["futbol", "handball"]:
                        # Intercambiar las posiciones del primer equipo de baloncesto y el equipo de futbol/handball
                        self.cola[i], self.cola[j] = self.cola[j], self.cola[i]
                        self.tiempo_espera[i - 1], self.tiempo_espera[j - 1] = self.tiempo_espera[j - 1], \
                        self.tiempo_espera[i - 1]
                        return  # Terminar la función después de hacer el intercambio

    def verificar_prioridad_objeto(self, vector_estado):
        indices_en_cola = self.obtener_indices_en_cola(vector_estado)
        if indices_en_cola:
            for indice_en_cola in indices_en_cola:
                if vector_estado[indice_en_cola][0] == "basketball":
                    siguiente_indice = indice_en_cola + 1
                    while siguiente_indice < len(vector_estado):
                        if vector_estado[siguiente_indice][1] == "en cola" and vector_estado[siguiente_indice][2] >= 0:
                            if vector_estado[siguiente_indice][0] in ["futbol", "handball"]:
                                vector_estado[indice_en_cola][2] = 2
                                vector_estado[siguiente_indice][2] = 1
                                break
                        siguiente_indice += 1
        return vector_estado

    def obtener_indices_en_cola(self, vector_estado):
        # Buscar todos los índices de los equipos en cola
        indices_en_cola = []
        for i, vector in enumerate(vector_estado):
            if isinstance(vector, list) and vector[1] == "en cola" and vector[2] == 1:
                indices_en_cola.append(i)
        return indices_en_cola

    def verificar_grupo_retirado(self, cant_grupos):
        bandera = False
        if len(self.cola) > cant_grupos:
            bandera = True

        return bandera

    def fila_calculo(self, vectorEstado):
        vector_final = ["PROMEDIO DE ESPERA", 0, 0, 0, "TASA DE LIMPIEZA", 0]

        if vectorEstado[28] != 0:
            vector_final[1] = vectorEstado[31] / vectorEstado[28]
        else:
            vector_final[1] = 0
        if vectorEstado[29] != 0:
            vector_final[2] = vectorEstado[32] / vectorEstado[29]
        else:
            vector_final[2] = 0
        if vectorEstado[30] != 0:
            vector_final[3] = vectorEstado[33] / vectorEstado[30]
        else:
            vector_final[3] = 0
        valor = (vectorEstado[34] / self.cant_partidos) * 100
        vector_final[5] = f"{valor:.2f}%"

        return vector_final

    # Acá quise aplicar string y después pasarlo a float para usar los números pero no se puede al pasarlo a float
    # sigue mostrando una cantidad de decimales gigantes así que directamente aplicar el format en el frontend de la
    # tabla
    def redondear_a_2_decimales(self, numero):
        return round(numero, 2)

    def calcularProxLlegadaFutbol(self, relojActual, llegada_futbol):
        # Esta funcion calcula y devuelve en que momento va a llegar el proximo equipo de futbol

        # Coloqué este while ya que si da 1 me da error en el logaritmo
        while True:
            rnd = random.random()
            rnd_redondeado = self.redondear_a_2_decimales(rnd)
            # Check to avoid 0 and 1
            if 0 < rnd_redondeado < 1:
                break

        rnd_exponencial = rnd_redondeado

        rnd_exp = self.redondear_a_2_decimales(-(llegada_futbol) * math.log(1 - rnd_exponencial))
        return rnd_exp, rnd_exponencial

    def calcularProxLlegadaHandball(self, relojActual, llegada_hand_a, llegada_hand_b):
        # Esta funcion calcula la proxima llegada de un equipo de handball
        rnd = random.random()
        rnd_redondeado = self.redondear_a_2_decimales(rnd)
        rnd_unif = llegada_hand_a + rnd_redondeado * (llegada_hand_b - llegada_hand_a)
        return self.redondear_a_2_decimales(rnd_unif), rnd_redondeado

    def calcularProxLlegadaBasketball(self, relojActual, llegada_basket_a, llegada_basket_b):
        # Esta funcion calcula la proxima llegada de un equipo de basketball
        rnd = random.random()
        rnd_redondeado = self.redondear_a_2_decimales(rnd)
        rnd_unif = llegada_basket_a + rnd_redondeado * (llegada_basket_b - llegada_basket_a)
        return self.redondear_a_2_decimales(rnd_unif), rnd_redondeado

    def calcularFinOcupacionFutbol(self, relojActual, ocupacion_futbol_a, ocupacion_futbol_b):
        rnd = random.random()
        rnd_redondeado = self.redondear_a_2_decimales(rnd)
        rnd_unif = ocupacion_futbol_a + rnd_redondeado * (ocupacion_futbol_b - ocupacion_futbol_a)
        return self.redondear_a_2_decimales(rnd_unif), rnd_redondeado

    def calcularFinOcupacionHandball(self, relojActual, ocupacion_hand_a, ocupacion_hand_b):
        rnd = random.random()
        rnd_redondeado = self.redondear_a_2_decimales(rnd)
        rnd_unif = ocupacion_hand_a + rnd_redondeado * (ocupacion_hand_b - ocupacion_hand_a)
        return self.redondear_a_2_decimales(rnd_unif), rnd_redondeado

    def calcularFinOcupacionBasketball(self, relojActual, ocupacion_basket_a, ocupacion_basket_b):
        rnd = random.random()
        rnd_redondeado = self.redondear_a_2_decimales(rnd)
        rnd_unif = ocupacion_basket_a + rnd_redondeado * (ocupacion_basket_b - ocupacion_basket_a)
        return self.redondear_a_2_decimales(rnd_unif), rnd_redondeado

    def calcular_uniforme_dif(self, uniforme_a, uniforme_b):
        rnd = random.random()
        rnd_redondeado = self.redondear_a_2_decimales(rnd)
        rnd_unif = uniforme_a + rnd_redondeado * (uniforme_b - uniforme_a)
        # Redondear directamente la parte entera
        parte_entera = round(rnd_unif)
        return parte_entera, rnd_redondeado

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

