from slackblox.composition import TextObject
import slackblox.constants as c


class BlockElement():
    """
    View block elements documentation here https://api.slack.com/reference/block-kit/block-elements

    """

    def __init__(self):
        self.payload = {}
        self.payload["type"] = self.type

    def __str__(self):
        return json.dumps(self.payload)

    def __repr__(self):
        return json.dumps(self.payload)


class Button(BlockElement):
    def __init__(self):
        self.type = "button"


class Checkboxes(BlockElement):
    def __init__(self):
        self.type = "checkboxes"


class DatePicker(BlockElement):
    def __init__(self):
        self.type = "datepicker"


class Image(BlockElement):
    def __init__(self):
        self.type = "image"


class MultiSelectMenu(BlockElement):
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


class Overflow(BlockElement):
    def __init__(self):
        self.type = "overflow"


class PlainTextInput(BlockElement):
    def __init__(self):
        self.type = "plain_text_input"


class RadioButtons(BlockElement):
    def __init__(self):
        self.type = "radio_buttons"


class SelectMenu(BlockElement):
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
