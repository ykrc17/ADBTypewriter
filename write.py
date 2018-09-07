import os


def keyevent(event):
    os.system("adb shell input keyevent %s" % event)


def text(input_text):
    os.system("adb shell input text \"%s\"" % input_text)


if __name__ == '__main__':
    while True:
        input_str = raw_input()
        if input_str == "clear":
            input_str = "67 " * 10
            keyevent(input_str)
        else:
            input_str = str.replace(input_str, " ", "%s")
            text(input_str)
            keyevent("66")
