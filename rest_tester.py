import requests
from kivy.app import App
from kivy.uix.dropdown import DropDown
from kivy.uix.widget import Widget
from requests import Session

class HttpMethodDropDown(DropDown):
    def select(self, data):
        print("Dropdown option was selected %s" % data)

class BaseWindow(Widget):
    def __init__(self, **kwargs):
        super(BaseWindow, self).__init__(**kwargs)

    def perform_http_requests(self, method):
        request = requests.Request(method, self.url.text)
        response = Session().send(request.prepare())
        self.response_body.text = response.text

class WebtesterApp(App):
    def build(self):
        base_window = BaseWindow()
        return base_window

if __name__ == "__main__":
    webster = WebtesterApp()
    webster.run()