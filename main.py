import keyboard, playsound, threading
keys = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", ",", ".", "/", "?", "!", "'", "\"", ":", ";", "[", "]", "{", "}", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "tab", "Shift", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+"]
pressed_keys = []
for i in range(len(keys)):
    pressed_keys.append(False)
while True:
    for key in range(len(keys)):
        if keyboard.is_pressed(keys[key]):
            if pressed_keys[key]==False:
                pressed_keys[key] = True
                threading.Thread(target=playsound.playsound, args=('./quak.mp3',), daemon=True).start()
        else:
            pressed_keys[key] = False