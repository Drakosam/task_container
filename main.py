import sys

from PySide6 import QtWidgets

from views.mainView import MainView

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    main_view = MainView()

    main_view.show()
    sys.exit(app.exec())
