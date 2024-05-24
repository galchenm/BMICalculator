import sys

# Import necessary PyQt6 modules
from PyQt6.QtWidgets import QApplication, QGridLayout, QLabel, QLineEdit, QWidget, QPushButton


class BMIcalculator(QWidget):
    def __init__(self):
        super().__init__() 
        self.setWindowTitle("BMI calculator")
        grid = QGridLayout()

        weight_label = QLabel("Weight (kg):")
        self.weight_line_edit = QLineEdit()

        height_label = QLabel("Height (cm):")
        self.height_line_edit = QLineEdit()

        grid.addWidget(weight_label, 0, 0)
        grid.addWidget(self.weight_line_edit, 0, 1)
        grid.addWidget(height_label, 1, 0)
        grid.addWidget(self.height_line_edit, 1, 1)

        calculate_button = QPushButton("Calculate BMI")
        calculate_button.clicked.connect(self.calculate_bmi)
        self.output_label = QLabel("Your BMI will appear here.")
        grid.addWidget(calculate_button, 2, 0, 1, 2)
        grid.addWidget(self.output_label, 3, 0, 1, 2)

        self.setLayout(grid)


    def calculate_bmi(self):
        try:
            weight = float(self.weight_line_edit.text())
            height = float(self.height_line_edit.text()) / 100
            self.output_label.setText(f"Your BMI is: {weight / (height ** 2):.2f}")
        except ValueError:
            self.output_label.setText("Please enter a valid number.") 

app = QApplication(sys.argv)
window = BMIcalculator()
window.show()
sys.exit(app.exec())