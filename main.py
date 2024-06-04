import sys
from random import random

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
        self.inicial_filas_mostrar = "10"
        self.inicial_fila_desde = "10"
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
        row_layout_7.addWidget(self.filas_mostrar_label)
        row_layout_7.addWidget(self.filas_mostrar_input)
        row_layout_7.addWidget(self.fila_desde_label)
        row_layout_7.addWidget(self.fila_desde_input)
        layout.addLayout(row_layout_7)

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
        self.filas_mostrar = 0
        self.fila_desde = 0

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

    def mostrar_datos(self, dias, ventas, costo_ventas, costo_obrero, total_dias, filas_mostrar, fila_desde):
        data = [[0] * 8, [0] * 8]  # Inicializamos data con dos elementos
        beneficio_acumulado = [0, 0, 0]  # Inicializamos beneficio_acumulado con tres ceros
        ventas_acumuladas = [0, 0, 0]
        costos_acumulados = [0, 0, 0]
        salario_acumulado = [0, 0, 0]

        # Calcular el índice final de las filas a mostrar
        fila_hasta = fila_desde + filas_mostrar

        for i in range(dias):
            rnd = round(random(), 2)
            ausentes = self.calcular_ausentes(total_dias, rnd)
            nomina = [max(0, 21 - ausentes), max(0, 22 - ausentes), max(0, 23 - ausentes)]
            ventas_dia = [0, 0, 0]
            costos_produccion_dia = [0, 0, 0]
            for numero_nomina in range(len(nomina)):
                if nomina[numero_nomina] >= 20:
                    ventas_dia[numero_nomina] = ventas
                    costos_produccion_dia[numero_nomina] = costo_ventas
            salario = [x * costo_obrero for x in [21, 22, 23]]
            beneficio = [0, 0, 0]

            for j in range(3):
                beneficio[j] = ventas_dia[j] - costos_produccion_dia[j] - salario[j]
                beneficio_acumulado[j] += beneficio[j]  # Acumulamos el beneficio
                # Acumulamos ventas, costos y salario
                ventas_acumuladas[j] += ventas_dia[j]
                costos_acumulados[j] += costos_produccion_dia[j]
                salario_acumulado[j] += salario[j]

            # Verificar si estamos dentro del rango de filas a mostrar
            if fila_desde <= i <= fila_hasta - 1 or i == dias - 1:
                # Aca uso el modulo de i para ir alternando entre 0 y 1, para poder alternar entre los objetos del vector
                data[i % 2] = [i + 1, rnd, ausentes, nomina, ventas_acumuladas, costos_acumulados, salario_acumulado,
                               beneficio_acumulado.copy()]

                self.insertar_en_tabla(data[i % 2])

    def insertar_en_tabla(self, fila):
        # Obtiene el número de filas existentes en la tabla. ya que esta funcion puede ser llamada con filas
        # ya insertadas en la tabla
        i = self.tableWidgetSecond.rowCount()
        # Inserta una nueva fila en la tabla en la posición 'i'
        self.tableWidgetSecond.insertRow(i)
        # Inicializa el índice de la columna a 0
        j = 0

        # Itera sobre cada elemento en la fila de datos
        for item in fila:
            # Verifica si el elemento es una lista
            if isinstance(item, list):
                # Si el elemento es una lista, itera sobre cada subelemento en la lista, en caso que sea
                # el vector de beneficio
                for subitem in item:
                    # Inserta el subelemento en la tabla en la fila 'i' y la columna 'j'
                    self.tableWidgetSecond.setItem(i, j, QTableWidgetItem(str(subitem)))
                    # Incrementa el índice de la columna
                    j += 1
            else:
                # Si el elemento no es una lista, lo inserta directamente en la tabla en la fila 'i' y la columna 'j'
                self.tableWidgetSecond.setItem(i, j, QTableWidgetItem(str(item)))
                # Incrementa el índice de la columna
                j += 1

    def create_input_field(self, text):
        layout = QHBoxLayout()
        label = QLabel(text)
        layout.addWidget(label)

        input_field = QLineEdit()
        layout.addWidget(input_field)

        return layout, input_field, label

    def show_second_page(self):
        dias_text = self.dias_input.text()
        self.inicial_dias = dias_text

        ventas_text = self.ventas_input.text()
        self.inicial_ventas = ventas_text

        costo_ventas_text = self.costo_ventas_input.text()
        self.inicial_costo_ventas = costo_ventas_text

        costo_obrero_text = self.costo_obrero_input.text()
        self.inicial_costo_obrero = costo_obrero_text

        filas_mostrar_text = self.filas_mostrar_input.text()
        self.inicial_filas_mostrar = filas_mostrar_text

        fila_desde_text = self.fila_desde_input.text()
        self.inicial_fila_desde = fila_desde_text


        # Validación de todos los campos para que todos sean completados
        if dias_text.strip() == '' or ventas_text.strip() == '' or costo_ventas_text.strip() == '' \
                or costo_obrero_text.strip() == '' or filas_mostrar_text.strip() == '' or fila_desde_text.strip() == '':
            QMessageBox.warning(self, 'Campos vacíos', 'Por favor, complete todos los campos.')
            return


        # Validación de días

        dias = int(dias_text)
        if dias <= 0 or dias > 100000:
            QMessageBox.warning(self, 'Valor inválido', 'El número de días debe estar entre 1 y 100,000.')
            return

        # Validación de filas_mostrar

        filas_mostrar = int(filas_mostrar_text)
        if filas_mostrar > dias:
            QMessageBox.warning(self, 'Valor inválido',
                                'El número de filas a mostrar no debe exceder al número de días.')
            return

        if filas_mostrar <= 0 or filas_mostrar > 400:
            QMessageBox.warning(self, 'Valor inválido',
                                'El número de filas a mostrar debe estar entre 1 y 400.')
            return

        # Validación de fila_desde

        fila_desde = int(fila_desde_text)
        if fila_desde < 0 or fila_desde > dias - filas_mostrar:
            QMessageBox.warning(self, 'Valor inválido',
                                'El número de fila desde debe estar entre 0 y {}.'.format(dias - filas_mostrar))
            return

        dias = int(dias_text)
        ventas = float(ventas_text)
        costo_ventas = float(costo_ventas_text)
        costo_obrero = float(costo_obrero_text)
        filas_mostrar = int(filas_mostrar_text)
        fila_desde = int(fila_desde_text)
        self.init_second_page2(dias, ventas, costo_ventas, costo_obrero, filas_mostrar, fila_desde)

    def init_second_page2(self, dias, ventas, costo_ventas, costo_obrero, filas_mostrar, fila_desde):
        self.tableWidgetSecond = QTableWidget(self)
        self.tableWidgetSecond.setColumnCount(18)
        self.tableWidgetSecond.setHorizontalHeaderLabels(
            ["Reloj", "RND", "AUSENTES", "NÓMINA 21", "NÓMINA 22", "NÓMINA 23",
             "VENTAS 21", "VENTAS 22", "VENTAS 23", "COSTOS 21",
             "COSTOS 22", "COSTOS 23", "SALARIO 21",
             "SALARIO 22", "SALARIO 23", "BENEFICIO 21", "BENEFICIO 22", "BENEFICIO 23"])
        total_dias = sum(int(self.tableWidget.item(row, 1).text()) for row in range(self.tableWidget.rowCount()))
        self.mostrar_datos(dias, ventas, costo_ventas, costo_obrero, total_dias, filas_mostrar, fila_desde)

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

    def calcular_ausentes(self, total_dias, rnd):
        limites_inferiores = [0]
        numeros_ausentes = [0, 1, 2, 3, 4, 5]

        for row in range(self.tableWidget.rowCount() - 1):
            dias = int(self.tableWidget.item(row, 1).text())
            if total_dias == 0:
                limites_inferiores.append(limites_inferiores[-1])
            else:
                proporciones = dias / total_dias

                limites_inferiores.append(limites_inferiores[-1] + round(proporciones, 2))

        ausentes = self.buscar(rnd, limites_inferiores, numeros_ausentes)

        return ausentes

    def buscar(self, rnd, limites_inf, numeros_ausentes):
        # enumerate lo que hace es que el for pueda devolver tanto el indice i, como el valor de limite_inf para ese indice
        for i, limite_inf in enumerate(limites_inf):
            if rnd < limite_inf:
                return numeros_ausentes[i - 1]
        return numeros_ausentes[-1]

    def show_main_page(self):
        self.init_main_window()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
