from slackblox.block_element import BlockElement
from slackblox.composition import (
    TextObject,
    ConfirmationDialog,
    set_from_object_or_string
)
import slackblox.constants as c


class BlockLayout():
    def __init__(self, block_id=None):
        """View layout block documentation here https://api.slack.com/reference/block-kit/blocks"""
        self.payload = {}
        self.payload["type"] = self.type
        self._set_block_id(block_id)

    def __str__(self):
        return json.dumps(self.payload)

    def __repr__(self):
        return json.dumps(self.payload)

    def _set_block_id(self, block_id=None):
        if block_id is not None:
            # TODO - Maximum length for this field is 255 characters.
            self.block_id = block_id
            self.payload["block_id"] = self.block_id

    def add(self, element: BlockElement):
        if element.type in c.LAYOUT_ELEMENTS[self.type]:
            self.payload.update(element.payload)
        else:
            err = "error here"
            return err


class ActionsLayout(BlockLayout):
    def __init__(self, elements, block_id=None):
        """A block that is used to hold interactive elements. https://api.slack.com/reference/block-kit/blocks#actions

        :param elements: An array of interactive element objects - buttons, select menus, overflow menus, or date pickers. 
        :type elements: []BlockElement
        :param block_id: A string acting as a unique identifier for a block.  defaults to None
        :type block_id: str, optional
        """
        self.type = "actions"
        super().__init__(block_id)
        # There is a maximum of 5 elements in each action block.
        if len(elements) > 0 and len(elements) <= 5:
            self.payload["elements"] = []
            for element in elements:
                self.payload["elements"].append(element.payload)
        else:
            raise ValueError(
                "Elements expected.  There is a maximum of 5 elements in each action block.")


class ContextLayout(BlockLayout):
    def __init__(self, elements, block_id=None):
        """Displays message context, which can include both images and text. https://api.slack.com/reference/block-kit/blocks#context

        :param elements: An array of image elements and text objects. 
        :type elements: []Image/TextObject
        :param block_id: A string acting as a unique identifier for a block.  defaults to None
        :type block_id: str, optional
        :raises ValueError: [description]
        """
        self.type = "context"
        super().__init__(block_id)
        # There is a maximum of 10 elements in each action block.
        if len(elements) > 0 and len(elements) <= 10:
            self.payload["elements"] = []
            for element in elements:
                # TODO - Verify an array of image elements and/or text objects.
                self.payload["elements"].append(element.payload)
        else:
            raise ValueError(
                "Elements array expected. Image or TextObject, 10 objects or less.")


class DividerLayout(BlockLayout):
    def __init__(self, block_id=None):
        """A content divider, like an <hr>, to split up different blocks inside of a message. https://api.slack.com/reference/block-kit/blocks#divider

        :param block_id: A string acting as a unique identifier for a block.  defaults to None
        :type block_id: str, optional
        """
        self.type = "divider"
        super().__init__(block_id)


class FileLayout(BlockLayout):
    def __init__(self, external_id, source, block_id=None):
        """Displays a remote file. https://api.slack.com/reference/block-kit/blocks#file

        :param external_id: The external unique ID for this file.
        :type external_id: str
        :param source: At the moment, source will always be "remote" for a remote file.
        :type source: str
        :param block_id: A string acting as a unique identifier for a block.  defaults to None
        :type block_id: str, optional
        """
        self.type = "file"
        super().__init__(block_id)
        self.external_id = external_id
        self.payload["external_id"] = self.external_id
        self.source = source
        self.payload["source"] = self.source


class ImageLayout(BlockLayout):
    def __init__(self, image_url, alt_text, title=None, block_id=None):
        """A simple image block. https://api.slack.com/reference/block-kit/blocks#image

        :param image_url: The URL of the image to be displayed.
        :type image_url: str
        :param alt_text: A plain-text summary of the image. This should not contain any markup.
        :type alt_text: str
        :param title: An optional title for the image in the form of a text object that can only be of type: plain_text, defaults to None
        :type title: TextObject or str, optional
        :param block_id: A string acting as a unique identifier for a block, defaults to None
        :type block_id: str, optional
        """
        self.type = "image"
        super().__init__(block_id)
        # TODO - Maximum length for this field is 3000 characters.
        self.image_url = image_url
        self.payload["image_url"] = self.image_url
        # TODO - A plain-text summary of the image. This should not contain any markup. Maximum length for this field is 2000 characters.
        self.alt_text = alt_text
        self.payload["alt_text"] = self.alt_text
        # title - TextObject. Maximum length for the text in this field is 2000 characters.
        self.title = set_from_object_or_string(title, "plain_text")
        self.payload["title"] = self.title


class InputLayout(BlockLayout):
    def __init__(self, label, element, block_id=None, hint=None, optional=False):
        """A block that collects information from users - it can hold a plain-text input element, a select menu element, 
        a multi-select menu element, or a datepicker. https://api.slack.com/reference/block-kit/blocks#input

        :param label: A label that appears above an input element in the form of a text object that must have type of plain_text
        :type label: TextObject or str
        :param element: A plain-text input element, a select menu element, a multi-select menu element, or a datepicker
        :type element: Object
        :param block_id: A string acting as a unique identifier for a block, defaults to None
        :type block_id: str, optional
        :param hint: An optional hint that appears below an input element in a lighter grey, defaults to None
        :type hint: TextObject or str, optional
        :param optional: 	A boolean that indicates whether the input element may be empty when a user submits the modal, defaults to False
        :type optional: bool, optional
        """
        self.type = "input"
        super().__init__(block_id)
        self.label = set_from_object_or_string(label)
        self.payload["label"] = self.label
        self.element = element
        self.payload["element"] = self.element.payload
        if hint is not None:
            # TODO - Maximum length for the text in this field is 2000 characters.
            self.hint = set_from_object_or_string(hint)
            self.payload["hint"] = self.hint
        if optional is not False:
            self.optional = optional
            self.payload["optional"] = self.optional


class SectionLayout(BlockLayout):
    def __init__(self, text=None, block_id=None, fields=None, accessory=None):
        """Creates a ``section`` Layout Block.  Please see Slack Block Kit documentation for more details. https://api.slack.com/reference/block-kit/blocks#section

        :param text: The text for the block, defaults to None
        :type text: str or TextObject, optional
        :param block_id: A string acting as a unique identifier for a block, defaults to None
        :type block_id: str, optional
        :param fields: An array of text objects. Any text objects included with fields will be rendered
            in a compact format that allows for 2 columns of side-by-side text, defaults to None
        :type fields: []TextObject or []str, optional
        :param accessory: One of the available element objects, defaults to None
        :type accessory: BlockElement, optional
        :raises ValueError: Must provide "text" or "fields" variable.
        """
        self.type = "section"
        super().__init__(block_id)
        if text is None and fields is None:
            raise ValueError("Must supply either 'text' or 'fields' object")
        # Maximum length for the text in this field is 3000 characters.
        self.text = set_from_object_or_string(text)
        self.payload["text"] = self.text
        # TODO - FIELDS
        # Maximum number of items is 10.
        # Maximum length for the text in each item is 2000 characters.
        # TODO - accessory
