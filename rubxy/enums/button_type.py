from enum import auto
from .auto_name import AutoName

class ButtonType(AutoName):
    SIMPLE = auto()
    "Display the button normally"

    SELECTION = auto()
    "Display the button as a list"

    CALENDAR = auto()
    "Display the button as a calendar"

    NUMBER_PICKER = auto()
    "Display the button as a list of numbers"

    STRING_PICKER = auto()
    "Display the button as a list of strings"

    LOCATION = auto()
    "Location type"

    PAYMENT = auto()
    "Display the button for payment"

    CAMERA_IMAGE = auto()
    "Display the button for taking a photo with the camera"

    CAMERA_VIDEO = auto()
    "Display the button for recording a video with the camera"

    GALLERY_IMAGE = auto()
    "Show button to send image from gallery"

    GALLERY_VIDEO = auto()
    "Show button to send video from gallery"

    FILE = auto()
    "Show button to send a file"

    AUDIO = auto()
    "Show button to send audio"

    RECORD_AUDIO = auto()
    "Show button to record audio"

    MY_PHONE_NUMBER = auto()
    "My phone number"

    MY_LOCATION = auto()
    "My location"

    TEXTBOX = auto()
    "Show button to enter text message"

    LINK = auto()
    "Show button to send internet address"

    ASK_MY_PHONE_NUMBER = auto()
    "Request my phone number"

    ASK_LOCATION = auto()
    "Request location"

    BARCODE = auto()
    "Show button to scan barcode"