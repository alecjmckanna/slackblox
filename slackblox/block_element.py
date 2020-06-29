import json
from slackblox.composition import set_text_from_object_or_string
import slackblox.constants as c


class _BlockElement():
    """
    View block elements documentation here https://api.slack.com/reference/block-kit/block-elements
    """

    def __init__(self, action_id=None):
        self.payload = {}
        self.payload["type"] = self.type
        self._set_action_id(action_id)

    def __str__(self):
        return json.dumps(self.payload)

    def __repr__(self):
        return json.dumps(self.payload)

    def _set_action_id(self, action_id=None):
        if action_id is not None:
            # TODO - Maximum length for this field is 255 characters.
            self.action_id = action_id
            self.payload["action_id"] = self.action_id

class Button(_BlockElement):
    def __init__(self, text, action_id=None, url=None, value=None, style=None, confirm=None):
        """An interactive component that inserts a button. 
        The button can be a trigger for anything from opening a simple link to starting a complex workflow. https://api.slack.com/reference/block-kit/block-elements#button

        :param text: A text object that defines the button's text. Can only be of type: plain_text.
        :type text: str
        :param action_id: An identifier for this action. You can use this when you receive an interaction payload to identify the source of the action, defaults to None.
        :type action_id: str, optional
        :param url: A URL to load in the user's browser when the button is clicked, defaults to None
        :type url: str, optional
        :param value: The value to send along with the interaction payload, defaults to None
        :type value: str, optional
        :param style: Decorates buttons with alternative visual color schemes. Use this option with restraint, defaults to None
        :type style: str, optional
        :param confirm: A confirm object that defines an optional confirmation dialog after the button is clicked, defaults to None
        :type confirm: ConfirmationDialog, optional
        """
        self.type = "button"
        super().__init__(action_id)
        # TODO - TEXT: Maximum length for the text in this field is 75 characters.
        self.text = set_text_from_object_or_string(text, "plain_text")
        self.payload["text"] = self.text
        # TODO - URL: Maximum length for this field is 3000 characters.
        if url is not None:
            self.url = url
            self.payload["url"] = self.url
        # TODO - VALUE: Maximum length for this field is 2000 characters.
        if value is not None:
            self.value = value
            self.payload["value"] = self.value
        if style is not None:
            self.style = style
            self.payload["style"] = self.style
        if confirm is not None:
            self.confirm = confirm.payload
            self.payload["confirm"] = self.confirm


class Checkboxes(_BlockElement):
    def __init__(self, action_id=None, options=None, initial_options=None, confirm=None):
        """A checkbox group that allows a user to choose multiple items from a list of possible options. https://api.slack.com/reference/block-kit/block-elements#checkboxes

        :param action_id: An identifier for the action triggered when the checkbox group is changed. 
        You can use this when you receive an interaction payload to identify the source of the action, defaults to None
        :type action_id: str, optional
        :param options: An array of Option objects, defaults to None
        :type options: []Option, optional
        :param initial_options: An array of Option objects that exactly matches one or more of the options within options, defaults to None
        :type initial_options: []Option, optional
        :param confirm: A confirm object that defines an optional confirmation dialog that appears after clicking one of the checkboxes in this element, defaults to None
        :type confirm: ConfirmationDialog, optional
        """
        self.type = "checkboxes"
        super().__init__(action_id)
        if options is not None:
            self.options = [option.payload for option in options]
            self.payload["options"] = []
            for option in self.options:
                self.payload["options"].append(option)
        if initial_options is not None:
            self.initial_options = [initial_option.payload for initial_option in initial_options]
            self.payload["initial_options"] = []
            for initial_option in self.initial_options:
                self.payload["initial_options"].append(initial_option)
        if confirm is not None:
            self.confirm = confirm.payload
            self.payload["confirm"] = self.confirm


class DatePicker(_BlockElement):
    def __init__(self, action_id=None, placeholder=None, initial_date=None, confirm=None):
        """https://api.slack.com/reference/block-kit/block-elements#datepicker

        :param action_id: [description], defaults to None
        :type action_id: [type], optional
        :param placeholder: [description], defaults to None
        :type placeholder: [type], optional
        :param initial_date: [description], defaults to None
        :type initial_date: [type], optional
        :param confirm: [description], defaults to None
        :type confirm: [type], optional
        """
        self.type = "datepicker"


class Image(_BlockElement):
    def __init__(self, image_url, alt_text):
        """An element to insert an image as part of a larger block of content. If you want a block with only an image in it, 
        you're looking for the image block (layout). https://api.slack.com/reference/block-kit/block-elements#image

        :param image_url: The URL of the image to be displayed.
        :type image_url: str
        :param alt_text: A plain-text summary of the image. This should not contain any markup.
        :type alt_text: str
        """
        self.type = "image"
        super().__init__()
        self.image_url = image_url
        self.payload["image_url"] = self.image_url
        self.alt_text = alt_text
        self.payload["alt_text"] = self.alt_text


class MultiSelectMenu(_BlockElement):
    def __init__(self):
        super().__init__()


class MultiStaticSelect(MultiSelectMenu):
    def __init__(self):
        self.type = "multi_static_select"


class MultiExternalSelect(MultiSelectMenu):
    def __init__(self):
        self.type = "multi_external_select"


class MultiUsersSelect(MultiSelectMenu):
    def __init__(self):
        self.type = "multi_users_select"


class MultiConversationSelect(MultiSelectMenu):
    def __init__(self):
        self.type = "multi_conversations_select"


class MultiChannelsSelect(MultiSelectMenu):
    def __init__(self):
        self.type = "multi_channels_select"


class Overflow(_BlockElement):
    def __init__(self):
        self.type = "overflow"


class PlainTextInput(_BlockElement):
    def __init__(self):
        self.type = "plain_text_input"


class RadioButtons(_BlockElement):
    def __init__(self):
        self.type = "radio_buttons"


class SelectMenu(_BlockElement):
    def __init__(self):
        super().__init__()


class StaticSelect(SelectMenu):
    def __init__(self):
        self.type = "static_select"


class ExternalSelect(SelectMenu):
    def __init__(self):
        self.type = "external_select"


class UsersSelect(SelectMenu):
    def __init__(self):
        self.type = "users_select"


class ConversationsSelect(SelectMenu):
    def __init__(self):
        self.type = "conversations_select"


class ChannelsSelect(SelectMenu):
    def __init__(self):
        self.type = "channels_select"
