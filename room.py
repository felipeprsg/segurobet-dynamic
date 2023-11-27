from constants import groups

from operation import send_signal


def roletaBrasileira(msg: str):
    lines = msg.splitlines()

    lines = [line for line in lines if "Roleta" not in line]

    msg = '\n'.join(lines).replace("*", "")

    if "ENTRADA CONFIRMADA" in msg:
        return "signal", msg

    return "message", msg


def spaceman(msg: str):
    lines = msg.splitlines()

    lines = [line for line in lines if "Acesse" not in line]

    msg = '\n'.join(lines).replace("*", "")

    if "ENTRADA CONFIRMADA" in msg:
        return "signal", msg

    return "message", msg


def aviator(msg: str):
    lines = msg.splitlines()

    lines = [line for line in lines if "Acesse" not in line]

    msg = '\n'.join(lines).replace("*", "")

    if "ENTRADA CONFIRMADA" in msg:
        return "signal", msg

    return "message", msg


processors = {
    "roleta brasileira": roletaBrasileira,
    "spaceman": spaceman,
    "aviator": aviator,
}


async def handle_signal(event):
    if event is None or event.chat is None or event.text is None:
        return

    print("event")

    group_username = event.chat.id
    game = groups.get(int("-100" + str(group_username)), None)

    if game is None:
        print("Group not found")
        print(f"{group_username = }, {game = }")
        return

    processor = processors.get(game, None)

    if processor is None:
        print("Processor not found")
        print(f"{game = }")
        return

    signal_type, signal = processor(event.text)

    if not signal:
        return

    print(f"{game = }, {signal_type = }")
    print(signal)

    await send_signal(game, signal, signal_type)
