dictionary = {
    "Post":{'fa':"پست"},
    "Draft":{'fa':"پیش نویس"}
}


class Settings:
    language = 'en'


class Button:
    def __init__(self, text) -> None:
        self.text = text

    def show(self):
        print(self.text)


class T:
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return dictionary.get(self.text, {}).get(Settings.language, self.text)



class Twitter:
    def input(self):
        buttons = [
            Button("Post"),
            Button("Draft")
        ]
        self.show_buttons(buttons)

    def show_buttons(self, buttons):
        for b in buttons:
            b.show()

