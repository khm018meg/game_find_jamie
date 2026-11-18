from random import randint

ll_duty = ["duty_phone_yes", "duty_phone_no"]

GAME_STATE = {
    # ---------------------------------------------------------
    # Initial State: Dark Room
    # ---------------------------------------------------------
    "start": {
        "title": "Reception area",
        "prompt": "You go down from your room to the reception area looking for Jamie and find no one there...",
        "status": "active",
        "choices": [
            {"text": "Call duty phone", "next_state": "duty_phone_no", "alter_state" : "duty_phone_yes"}, #
            {"text": "Go look in the canteen", "next_state": "canteen"}, #
            {"text": "Go to common room 1", "next_state": "cr1"},
            {"text": "Go to common room 2", "next_state": "cr2"},
        ],
    },

    "cr1": {
        "title": "Common Room 1",
        "prompt": "You go to common room 1, and you see Vlad sitting there",
        "status": "active",
        "choices": [
            {"text": "Say hi", "next_state": "gate", "alter_state" : "answer"},
            {"text": "Say ", "next_state": "start"}, #
        ],
    },

    "canteen": {
        "title": "Canteen",
        "prompt": "You go to the canteen, and see Ms. ARMINE sitting there",
        "status": "active",
        "choices": [
            {"text": "Ask Ms. Armine about Jamie", "next_state": "gate", "alter_state" : "answer"},
            {"text": "Go back to reception", "next_state": "start"}, #
        ],
    },

    "gate": {
        "title": "GATED",
        "prompt": "OH NO! Ms. Armine was in a very bad mood, so she GATED you for 1 month",
        "status": "game_over",
        "choices": [],
    },

    "answer": {
        "title": "Canteen",
        "prompt": "Ms. Armine said she last saw him in reception area",
        "status": "active",
        "choices": [
            {"text": "Go back to reception area", "next_state": "start"}, #
        ],
    },

    "back_room": {
        "title": "Your room",
        "prompt": "You gave up, you did not look for Jamie.",
        "status": "game_over",
        "choices": [],
    },

    "duty_phone_yes": {
        "title": "Reception area",
        "prompt": "You call the duty phone, and JAMIE PICKED UP!",
        "status": "victory",
        "choices": [],
    },

    "duty_phone_no": {
        "title": "Raception area",
        "prompt": "You gave up, you did not look for Jamie.",
        "status": "game_over",
        "choices": [],
    },
}
