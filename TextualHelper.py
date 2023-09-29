from textual.app import App, ComposeResult
from textual.widgets import Header, Footer
from textual.containers import Horizontal, VerticalScroll, Container
from textual.widgets import Button, Input, Static, Markdown, RadioSet, RadioButton

class MessageDialog(App):

    CSS = """
        Button {
            width: 100%;
            height: auto;
            dock: bottom;
        }

        .message {
            margin: 1 0;
            text-style: bold;
            height: 100%;
        }

        .header {
            margin: 2 2 2 2;
            text-style: bold;
        }
    """   

    def __init__(self, message='Place *your* message here, markdown mode *on*', title='Title', ok_button_text='OK'):
        super().__init__()
        self.message = message
        self.title = title
        self.ok_button_text = ok_button_text

    def compose(self):
        """Create child widgets for the app."""
        yield Header(self.title)
        yield Footer()
        yield Container(
            Markdown(self.message, classes="message"),
            Button(self.ok_button_text,variant="primary", id='confirm')
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        # self.exit(str(event.button))
        self.exit(True)


class RadioDialog(App):

    CSS = """
        Button {
            width: 100%;
            height: auto;
            dock: bottom;
        }

        .message {
            margin: 1 0;
            text-style: bold;
            min-height: 2;
        }

        .header {
            margin: 2 2 2 2;
            text-style: bold;
        }
    """
    def __init__(self, message='Place *your* message here, markdown mode *on*', title='Title', place_holder='Inserisci il valore qui..', ok_button_text='OK', options = [("opzione1","opzione1"), ("opzione2","opzione2"), ("opzione3","opzione3")]):
        super().__init__()
        self.message = message
        self.title = title
        self.ok_button_text = ok_button_text
        self.place_holder = place_holder
        self.options = options


    def compose(self):
        """Create child widgets for the app."""
        yield Header(self.title)
        yield Footer()
        yield VerticalScroll(
            Markdown(self.message, classes='message'),
            RadioSet(
                *[ RadioButton(desc, id=f"{val}") for desc, val in self.options ],
            id='radioset'),
            Button(self.ok_button_text,variant='primary', id='confirm')
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.exit(self.query_one("#radioset").pressed_button.id)

class InputDialog(App):

    CSS = """
        Button {
            width: 100%;
            height: auto;
            dock: bottom;
        }

        .message {
            margin: 1 0;
            text-style: bold;
            min-height: 2;
        }

        .header {
            margin: 2 2 2 2;
            text-style: bold;
        }
    """

    def __init__(self, message='Place *your* message here, markdown mode *on*', title='Title', place_holder='Inserisci il valore qui..', ok_button_text='OK', default_value=''):
        super().__init__()
        self.message = message
        self.title = title
        self.ok_button_text = ok_button_text
        self.place_holder = place_holder
        self.default_value = default_value

    def compose(self):
        """Create child widgets for the app."""
        yield Header(self.title)
        yield Footer()
        yield VerticalScroll(
            Markdown(self.message, classes="message"),
            Input(
                placeholder=self.place_holder, id='input_box', value=self.default_value,
            ),
            Button(self.ok_button_text,variant="primary", id='confirm')
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.exit(self.query_one("#input_box").value)

class YesNoDialog(App):

    CSS = """
    .header {
        margin: 2 2 2 2;
        text-style: bold;
    }

    .message {
        margin: 1 0;
        width: 100%;
        column-span: 2;
        content-align: center middle;
    }

    .buttons {
        width: 100%;
        height: auto;
        dock: bottom;
    }

    Button {
        width: 50%;
    }

    """
    def __init__(self, message='Place *your* message here, markdown mode *on*', title='Title', place_holder='Inserisci il valore qui..', yes_button_text='OK', no_button_text='NO'):
        super().__init__()
        self.message = message
        self.title = title
        self.yes_button_text = yes_button_text
        self.no_button_text = no_button_text
        self.place_holder = place_holder

    def compose(self) -> ComposeResult:
        yield Header(self.title)
        yield Footer()
        yield VerticalScroll(
            Markdown(self.message, classes="message"),
            Horizontal(
                Button(self.yes_button_text, id="yes", variant="primary"),
                Button(self.no_button_text, id="no", variant="error"),
                classes="buttons"),
            id = 'container', 
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == 'yes':
            self.exit(True)
        elif event.button.id == 'no':
            self.exit(False)


if __name__ == "__main__":
    """
    ret = RadioDialog().run()
    print(ret)
    ret = YesNoDialog().run()
    print(ret)
    ret = MessageDialog().run()
    print(ret)
    """
    ret = InputDialog(default_value='valore di default').run()
    print(ret)