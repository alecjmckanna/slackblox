import json
from slackblox.composition import set_text_from_object_or_string
import slackblox.constants as c


class Slackblox():
    def __init__(self, **kwargs):
        """Default Block Kit payload surface for a message. https://api.slack.com/surfaces/messages

        :param **kwargs: Used to include additional keys in the payload.
        """
        if not hasattr(self, "type"):
            self.type = "message"
        self.payload = {}
        if hasattr(self, "surface"):
            self.payload.update(self.surface)
        if kwargs is not None:
            for k, v in kwargs.items():
                self.payload[k] = v
        self.payload["blocks"] = []
        self.blocks = self.payload["blocks"]

    def __str__(self):
        return json.dumps(self.payload)

    def __repr__(self):
        return json.dumps(self.payload)

    def add(self, layout):
        """Add a Block to the current surface.

        :param layout: Block layout to be appended to the block array.
        :type layout: _BlockLayout
        :raises err: Block cannot be added to this surface type.
        """
        if layout.type in c.SURFACE_LAYOUTS[self.type]:
            self.blocks.append(layout.payload)
        else:
            err = "error"
            raise err


class SlackbloxModal(Slackblox):
    def __init__(self, title, **kwargs):
        """Default Block Kit payload surface for a modal. https://api.slack.com/surfaces/modals

        :param title: Title of the pop-up modal.
        :type title: str or TextObject
        :param **kwargs: Used to include additional keys in the payload.
        """
        self.type = "modal"
        self.title = set_text_from_object_or_string(title)
        self.surface = {}
        self.surface["type"] = "modal"
        self.surface["title"] = self.title
        super().__init__(**kwargs)


class SlackbloxHome(Slackblox):
    def __init__(self, **kwargs):
        """Default Block Kit payload surface for a Home Tab. https://api.slack.com/surfaces/tabs

        :param **kwargs: Used to include additional keys in the payload.
        """
        self.type = "home"
        self.surface = {}
        self.surface["type"] = "home"
        super().__init__(**kwargs)
