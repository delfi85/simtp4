from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QTableWidget, QVBoxLayout, QWidget, QTableWidgetItem


class RungeKuttaWindow(QWidget):  # Cambiado a QWidget en lugar de QMainWindow
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Runge Kutta Window")
        self.setMinimumSize(1500, 1000)

        self.tableWidgetRunge = QTableWidget(self)
        self.tableWidgetRunge.setColumnCount(8)
        self.tableWidgetRunge.setMinimumSize(700, 500)
        self.tableWidgetRunge.setHorizontalHeaderLabels(
            ["t", "M", "K1", "K2", "K3", "K4", "t[i+1]", "M[i+1]"])

        font = QFont()
        font.setPointSize(11)
        self.tableWidgetRunge.setFont(font)
        self.tableWidgetRunge.horizontalHeader().setFont(font)

        layout = QVBoxLayout()
        layout.addWidget(self.tableWidgetRunge)

        self.setLayout(layout)  # Establece el layout en la propia QWidget

    def insertar_en_tabla_runge(self, fila):
        # Obtiene el número de filas existentes en la tabla
        i = self.tableWidgetRunge.rowCount()
        # Inserta una nueva fila en la tabla en la posición 'i'
        self.tableWidgetRunge.insertRow(i)

        # Itera sobre cada elemento en la fila de datos
        for idx, item in enumerate(fila):
            # Formatea el número si es un float
            if isinstance(item, float):
                item = f"{item:.2f}"
            # Crea un QTableWidgetItem para el dato
            item_widget = QTableWidgetItem(str(item))
            # Centra el texto en la columna
            item_widget.setTextAlignment(Qt.AlignCenter)
            # Inserta el elemento en la tabla
            self.tableWidgetRunge.setItem(i, idx, item_widget)

        # Ajusta el ancho de las columnas
        for col in range(self.tableWidgetRunge.columnCount()):
            self.tableWidgetRunge.setColumnWidth(col, 150)

