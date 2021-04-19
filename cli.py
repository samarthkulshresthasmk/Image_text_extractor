import argparse
import easyocr
import os
from threading import Thread
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
class PhotoSelection(BoxLayout):
    
    def extract(self):
            text_find = []
            try:
                os.mkdir("data")
            except:pass
            location = os.path.join(
                    os.getcwd(),
                    "data"
            )
            file = self.file.selection[0]
            lang = self.output.text
            reader = easyocr.Reader(['en'], 'True')
            for line in reader.readtext(file, detail="1"):
                text_find.append(line[1])
                text_find.append(" ")

            fi = open(f"{location}\\{lang}.txt" , 'w' )
            self.status.text = "Progressing"
            for i in range(len(text_find)):
                fi.write(text_find[i])
            fi.close()
            self.status.text = "File created"
    def runByThread(self):
        t = Thread(
            target=self.extract,
            name='EXTRACT_THREAD'
        )
        t.start()

class TextApp(App):
    def build(self):
        return PhotoSelection()

if __name__ == '__main__':
    TextApp().run()
	