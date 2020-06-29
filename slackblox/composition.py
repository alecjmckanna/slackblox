import slackblox.constants as c
import json

"""
Composition objects can be used inside of block elements and certain message payload fields. 
They are simply common JSON object patterns that you'll encounter frequently when building blocks or composing messages.
https://api.slack.com/reference/block-kit/composition-objects

    Text
    Confirmation dialog
    Option
    Option group
    Filter for conversation lists
"""


class _Composer():
    def __init__(self):
        self.payload = {}

    def __str__(self):
        return json.dumps(self.payload)

    def __repr__(self):
        return json.dumps(self.payload)


class TextObject(_Composer):
    def __init__(self, text, type="mrkdwn", emoji=True, verbatim=False):
        super().__init__()
        self.type = type
        self.text = text
        self.verbatim = verbatim
        self.emoji = emoji
        self.payload["type"] = self.type
        self.payload["text"] = self.text
        if self.type == "plain_text":
            self.payload["emoji"] = self.emoji
        if self.type == "mrkdwn" and self.verbatim == True:
            self.payload["verbatim"] = self.verbatim


class ConfirmationDialog(_Composer):
    def __init__(self, title, text, confirm, deny, style="primary"):
        """An object that defines a dialog that provides a confirmation step to any interactive element."""
        super().__init__()
        self.payload["confirm"] = {}
        self.title = set_text_from_object_or_string(title, "plain_text")
        self.payload["confirm"]["title"] = self.title
        self.text = set_text_from_object_or_string(text)
        self.payload["confirm"]["text"] = self.text
        self.confirm = set_text_from_object_or_string(confirm, "plain_text")
        self.payload["confirm"]["confirm"] = self.confirm
        self.deny = set_text_from_object_or_string(deny, "plain_text")
        self.payload["confirm"]["deny"] = self.deny
        if not style == "primary":
            self.style = style
            self.payload["confirm"]["style"] = self.style


class Option(_Composer):
    def __init__(self):
        pass


class OptionGroup(Option):
    def __init__(self):
        # Try to inherit from Option
        pass


class Filter(_Composer):
    def __init__(self):
        pass


def set_text_from_object_or_string(text, type="mrkdwn"):
    # If user provided a string value, convert it to a text object.
    if isinstance(text, str):
        return TextObject(text, type).payload
    # If we already have a TextObject, just return the payload.
    elif isinstance(text, TextObject):
        return text.payload

