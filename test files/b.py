import winsound
import time

def play_sound(sound_type):
    winsound.MessageBeep(sound_type)
    print(f"Playing sound: {sound_type}")

if __name__ == "__main__":
    # Toggle the default beep sound ON
    play_sound(winsound.MB_ICONHAND)

    # Wait for a few seconds
    time.sleep(2)

    # Play other sounds
    play_sound(winsound.MB_ICONASTERISK)
    time.sleep(2)

    play_sound(winsound.MB_ICONEXCLAMATION)
    time.sleep(2)

    play_sound(winsound.MB_ICONQUESTION)
    time.sleep(2)

    play_sound(winsound.MB_OK)
    time.sleep(2)

    play_sound(winsound.MB_ICONERROR)
