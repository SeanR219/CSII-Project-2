"""
Journal Program:
Write journal entries and save them as .txt files.
Can also open locally stored .txt files.
Doing so changes how the save button works slightly.
Also has an info panel that changes when saving or file not found.
"""
from logic import *

def main():
    application = QApplication([])
    window1 = Window1()
    window1.show()
    application.exec()

if __name__ == '__main__':
    main()


#Sources:
#https://stackoverflow.com/questions/24035660/how-to-read-from-qtextedit-in-python
#https://www.riverbankcomputing.com/static/Docs/PyQt6/index.html
#The one below is Lecture 11, I'm not sure if the link will actually work.
#https://unomail-my.sharepoint.com/personal/aowora_unomaha_edu/_layouts/15/stream.aspx?id=%2Fpersonal%2Faowora%5Funomaha%5Fedu%2FDocuments%2FUNO%20%2D%20SHARED%2FUNO%2F1620%2FLectures%2F74%20%2D%20Graphical%20User%20Interfaces%20Lecture%2Emp4&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZyIsInJlZmVycmFsQXBwUGxhdGZvcm0iOiJXZWIiLCJyZWZlcnJhbE1vZGUiOiJ2aWV3In19&ga=1&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview%2E11d9b204%2D8b7f%2D4c9e%2D9540%2D71d75c63df4b
#I also went back and looked at my past lab work.