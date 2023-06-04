import time

import pyautogui


def reel_and_shot():
    pyautogui.rightClick()
    pyautogui.sleep(0.5)
    pyautogui.rightClick()


count = 0


def locate_bobber_subtitle() -> bool:
    img = pyautogui.screenshot()

    location = pyautogui.locate(
        needleImage="images/subtitle3.png", haystackImage=img, confidence=0.6
    )
    global count
    count += 1

    print(f"Found subtitle on {location} {count}")

    return location != None


def main():
    while True:
        subtitle_found = locate_bobber_subtitle()
        if subtitle_found:
            print(f"Clicking and sleeping 5 seconds")
            reel_and_shot()
            time.sleep(5)

        time.sleep(0.5)


if "__main__" in __name__:
    main()
