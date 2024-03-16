import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Temperature_Converter(object):
    def setupUi(self, Temperature_Converter):
        Temperature_Converter.setObjectName("Temperature_Converter")
        Temperature_Converter.resize(606, 489)
        Temperature_Converter.setMinimumSize(QtCore.QSize(606, 489))
        Temperature_Converter.setMaximumSize(QtCore.QSize(606, 489))
        Temperature_Converter.setStyleSheet("background-color:rgb(131, 143, 255);\n"
"color:black;")
        self.label = QtWidgets.QLabel(Temperature_Converter)
        self.label.setGeometry(QtCore.QRect(70, 10, 481, 51))
        self.label.setObjectName("label")
        self.CurrentTemperature = QtWidgets.QTextEdit(Temperature_Converter)
        self.CurrentTemperature.setGeometry(QtCore.QRect(60, 110, 271, 41))
        self.CurrentTemperature.setStyleSheet("font: 16pt \"Calibri\";\n"
"background-color:rgb(255, 255, 255);")
        self.CurrentTemperature.setObjectName("CurrentTemperature")
        self.CurrentTemperatureUnit = QtWidgets.QComboBox(Temperature_Converter)
        self.CurrentTemperatureUnit.setEnabled(True)
        self.CurrentTemperatureUnit.setGeometry(QtCore.QRect(350, 110, 171, 41))
        self.CurrentTemperatureUnit.setStyleSheet("font: 16pt \"Calibri\";\n"
"background-color:rgb(255, 255, 255);")
        self.CurrentTemperatureUnit.setObjectName("CurrentTemperatureUnit")
        self.CurrentTemperatureUnit.addItem("")
        self.CurrentTemperatureUnit.addItem("")
        self.CurrentTemperatureUnit.addItem("")
        self.pushButton = QtWidgets.QPushButton(Temperature_Converter)
        self.pushButton.setGeometry(QtCore.QRect(190, 210, 241, 41))
        self.pushButton.setStyleSheet("font: 16pt \"Calibri\";\n"
"background-color:rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.Display_NewTemperature_1 = QtWidgets.QLabel(Temperature_Converter)
        self.Display_NewTemperature_1.setEnabled(False)
        self.Display_NewTemperature_1.setGeometry(QtCore.QRect(90, 320, 451, 41))
        self.Display_NewTemperature_1.setStyleSheet("border:2px soild black;\n"
"color:black;\n"
"font: 16pt \"Calibri\";")
        self.Display_NewTemperature_1.setObjectName("Display_NewTemperature_1")
        self.Display_NewTemperature_2 = QtWidgets.QLabel(Temperature_Converter)
        self.Display_NewTemperature_2.setEnabled(False)
        self.Display_NewTemperature_2.setGeometry(QtCore.QRect(90, 390, 451, 41))
        self.Display_NewTemperature_2.setStyleSheet("border:2px soild black;\n"
"color:black;\n"
"font: 16pt \"Calibri\";")
        self.Display_NewTemperature_2.setObjectName("Display_NewTemperature_2")

        self.retranslateUi(Temperature_Converter)
        QtCore.QMetaObject.connectSlotsByName(Temperature_Converter)

    def retranslateUi(self, Temperature_Converter):
        _translate = QtCore.QCoreApplication.translate
        Temperature_Converter.setWindowTitle(_translate("Temperature_Converter", "Temperature Converter"))
        self.label.setText(_translate("Temperature_Converter", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">Temperature Converter </span></p></body></html>"))
        self.CurrentTemperature.setPlaceholderText(_translate("Temperature_Converter", "Current Temperature"))
        self.CurrentTemperatureUnit.setItemText(0, _translate("Temperature_Converter", "Celsius"))
        self.CurrentTemperatureUnit.setItemText(1, _translate("Temperature_Converter", "Fahrenheit"))
        self.CurrentTemperatureUnit.setItemText(2, _translate("Temperature_Converter", "Kelvin"))
        self.pushButton.setText(_translate("Temperature_Converter", "Convert"))
        self.Display_NewTemperature_1.setText(_translate("Temperature_Converter", ""))
        self.Display_NewTemperature_2.setText(_translate("Temperature_Converter", ""))

def convert_temperature(ui):
        CurrentTemperature = ui.CurrentTemperature.toPlainText()
        if CurrentTemperature == '':
                converted_temp1 = "Please check temperature value"
                ui.Display_NewTemperature_1.setText(converted_temp1)
                return
            
        current_temp = float(CurrentTemperature)
        current_unit = ui.CurrentTemperatureUnit.currentText()

        if current_unit == "Celsius":
                converted_temp1 = f"{current_temp}°C = {current_temp * 9/5 + 32}°F"  # Celsius to Fahrenheit
                converted_temp2 = f"{current_temp}°C = {current_temp + 273.15}K "   # Celsius to Kelvin
        elif current_unit == "Fahrenheit":
                converted_temp1 = f"{current_temp}°F = {(current_temp - 32) * 5/9}°C"  # Fahrenheit to Celsius
                converted_temp2 = f"{current_temp}°F = {(current_temp - 32) * 5/9 + 273.15}K"  # Fahrenheit to Kelvin
        elif current_unit == "Kelvin":
                converted_temp1 = f"{current_temp}K = {current_temp - 273.15}°C"  # Kelvin to Celsius
                converted_temp2 = f"{current_temp}K = {(current_temp - 273.15) * 9/5 + 32}°F"  # Kelvin to Fahrenheit
        else:
                return

        # Update the display labels with the converted temperatures
        ui.Display_NewTemperature_1.setText(converted_temp1)
        ui.Display_NewTemperature_2.setText(converted_temp2)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Temperature_Converter = QtWidgets.QWidget()
    ui = Ui_Temperature_Converter()
    ui.setupUi(Temperature_Converter)

    ui.pushButton.clicked.connect(lambda: convert_temperature(ui))

    Temperature_Converter.show()
    sys.exit(app.exec_())
