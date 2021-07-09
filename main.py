from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import socket


class Container(BoxLayout):
    s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
    n = 0

    def con(self):
        try:
            self.s = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
            self.s.connect(('98:D3:71:F6:3A:BA', 1))
            return 'Соединение установлено'
        except (TimeoutError, OSError):
            return 'Не удалось синхронизироваться с устройством'

    def sm(self):
        if self.n == 0:
            self.but.text = 'Разорвать соединение'
            self.dost.text = self.con()
            self.n = 1

        else:
            self.but.text = 'Подключиться'
            self.dost.text = '...'
            self.n = 0
            try:
                self.s.close()
            except (TimeoutError, OSError):
                pass

    def signal(self, x):
        try:
            self.s.send(str(x).encode('UTF-8'))
        except (TimeoutError, OSError):
            pass


class CarApp(App):
    def build(self):
        return Container()


if __name__ == '__main__':
    CarApp().run()
