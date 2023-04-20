import sys
from PyQt5.QtWidgets import QApplication
from cover_page import CoverPage

if __name__ == "__main__":
    app = QApplication(sys.argv)
    cover_page = CoverPage()
    cover_page.show()
    sys.exit(app.exec_())
