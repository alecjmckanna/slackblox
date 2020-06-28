"""
Define any constant values here.
"""
MAX_BLOCKS = 100
MAX_TITLE = 24
MAX_TEXT = 3000

"""
 - SURFACE_LAYOUTS: which layouts can be applied to a surface
 - LAYOUT_ELEMENTS: which elements can be applied to a layout
 - ELEMENT_SURFACES: which surfaces can use an element attached to a layout
"""
SURFACE_LAYOUTS = {
    "message": ["actions", "context", "divider", "file", "image", "section"],
    "modal": ["actions", "context", "divider", "image", "input", "section"],
    "home": ["actions", "context", "divider", "image", "section"],
}

LAYOUT_ELEMENTS = {
    "actions": ["button", "checkboxes", "datepicker", "overflow", "plain_text_input", "radio_buttons", "static_select", "external_select", "users_select", "conversations_select", "channels_select", ],
    "context": ["image", ],
    "divider": [],
    "file": [],
    "image": [],
    "input": ["checkboxes", "date_picker", "multi_static_select", "multi_external_select", "multi_users_select", "multi_conversations_select", "multi_channels_select", "plain_text_input", "radio_buttons", "static_select", "external_select", "users_select", "conversations_select", "channels_select", ],
    "section": ["button", "checkbox", "datepicker", "image", "multi_static_select", "multi_external_select", "multi_users_select", "multi_conversations_select", "multi_channels_select", "overflow", "plain_text_input", "radio_buttons", "static_select", "external_select", "users_select", "conversations_select", "channels_select", ],
}

ELEMENT_SURFACES = {
    "button": ["message", "modal", "home", ],
    "checkbox": ["modal", "home", ],
    "datepicker": ["message", "modal", "home", ],
    "image": ["message", "modal", "home", ],
    "multi_static_select": ["message", "modal", "home", ],
    "multi_external_select": ["message", "modal", "home", ],
    "multi_users_select": ["message", "modal", "home", ],
    "multi_conversations_select": ["message", "modal", "home", ],
    "multi_channels_select": ["message", "modal", "home", ],
    "overflow": ["message", "modal", "home", ],
    "plain_text_input": ["message", "modal", "home", ],
    "radio_buttons": ["modal", "home", ],
    "static_select": ["message", "modal", "home", ],
    "external_select": ["message", "modal", "home", ],
    "users_select": ["message", "modal", "home", ],
    "conversations_select": ["message", "modal", "home", ],
    "channels_select": ["message", "modal", "home", ],
}
