from PyQt6.QtWidgets import *
import os
from journal_gui import *
from file_name_gui import *
from confimation_gui import *
from append_gui import *
from file_finder_gui import *


a_file_is_open = False

def overwrite_file(file_name, entry):
    try:
        with open(file_name, "w") as f:
            f.write(entry)
        print(f"'{file_name}' overwritten.")
    except Exception as e:
        print(f"Error!: {e}")

class Window1(QMainWindow, Ui_MainWindow):
    """
    Window1 is the primary window where the Journal's contents are entered.
    Features a Save, and Exit button.
    """

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.Button_exit.clicked.connect(lambda : self.exit())
        self.Button_save.clicked.connect(lambda: self.save())
        self.Button_open.clicked.connect(lambda: self.open())

    def exit(self):
        """
        Closes the window.
        """
        self.close()

    def save(self):
        """
        If no .txt file is open:
        Retrieves text entered into "textEntryBox," then
        opens Window2 (to allow user to name their .txt file).

        If a .txt file is open:
        Saves the contents of the text entry box to the opened .txt file,
        no questions asked. And changes the "Info" panel to tell you it saved.
        """
        global a_file_is_open
        if a_file_is_open == True:
            global pre_exist_file_text
            pre_exist_file_text = self.textEntryBox.toPlainText()
            overwrite_file(file_search_name, pre_exist_file_text)
            self.label_info.setText(f"Saved to '{file_search_name}'")
        else:
            global entry
            entry = self.textEntryBox.toPlainText()
            global window2
            window2 = Window2()
            window2.show()

    def open(self):
        """
        Opens the "File Finder" text entry window.
        """
        window5 = Window5()
        window5.show()
        self.close()



class Window2(QMainWindow, Ui_MainWindow2):
    """
    File Name Entry when "Save" is clicked.
    """
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.Button_accept.clicked.connect(lambda: self.accept())

    def accept(self):
        """
        What happens when the "Accept" button is clicked.
        Searches to see if the entered file already exists,
        if it does opens Window3 (Overwrite Confirmation Window),
        if not creates a .txt file with that name.
        """
        global a_file_is_open
        global file_name
        file_name = self.lineEdit_fileNameEntry.text() + '.txt'

        if os.path.exists(file_name):
            window3 = Window3()
            window3.show()
        else:
            try:
                with open(file_name, 'a') as f:
                    f.write(entry)
                print(f"Entry written to '{file_name}'")
                self.close()
            except Exception as e:
                print(f"Error!: {e}")



class Window3(QMainWindow, Ui_MainWindow3):
    """
    Overwrite.
    Asks if user wants to overwrite a preexisting file.
    """
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.Button_yes.clicked.connect(lambda: self.yes())
        self.Button_no.clicked.connect(lambda: self.no())

    def yes(self):
        global entry
        overwrite_file(file_name, entry)
        self.close()
        window2.close()

    def no(self):
        window4 = Window4()
        window4.show()
        self.close()



class Window4(QMainWindow, Ui_MainWindow4):
    """
    Append.
    """
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.Button_yes.clicked.connect(lambda: self.yes())
        self.Button_no.clicked.connect(lambda: self.no())

    def append_file(self, file_name, entry):
        try:
            with open(file_name, "a") as f:
                f.write('\n' + entry)
            print(f"'{file_name}' appended.")
        except Exception as e:
            print(f"Error!: {e}")

    def yes(self):
        global entry
        self.append_file(file_name, entry)
        self.close()
        window2.close()

    def no(self):
        self.close()

class Window5(QMainWindow, Ui_MainWindow5):
    """
    Opens when user clicks the "Open" button in the file panel.
    Brings up a line entry box to search for pre-existing files.
    """
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.Button_openFile.clicked.connect(lambda: self.open())

    def open(self):
        """
        Searches for files with the entered name.
        If none are found opens the Window1 (Journal Window), and displays "File not found" in info panel.
        """
        global file_search_name
        file_search_name = self.lineEdit_fileFinderNameEntry.text() + '.txt'

        if os.path.exists(file_search_name):
            file = open(file_search_name)
            contents = file.read()
            file.close()

            print(f"'{file_search_name}' opened")

            window1 = Window1()
            window1.textEntryBox.setText(contents)
            window1.label_fileName.setText(file_search_name)
            self.close()
            window1.show()

            global a_file_is_open
            a_file_is_open = True
        else:
            window1 = Window1()
            self.close()
            window1.show()
            window1.label_info.setText("File not found.")