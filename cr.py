import win32api
import pyautogui
import time
import random
import keyboard
import msgs

LANG = "es" # en = English, es = Spanish, eo = Esperanto

cards_delay = tuple(input(msgs.msg(LANG,0)))
place_delay = tuple(input(msgs.msg(LANG,1)))
cards_delay = int(cards_delay[0]),int(cards_delay[1])
place_delay = int(place_delay[0]),int(place_delay[1])

slots = []

print(msgs.msg(LANG,2))

while len(slots) < 4:
	if win32api.GetKeyState(0x01) < 0:
		slots.append((pyautogui.position().x,pyautogui.position().y))
		time.sleep(0.3)

window = []

print(msgs.msg(LANG,3))
while len(window) < 2:
	if win32api.GetKeyState(0x01) < 0:
		window.append((pyautogui.position().x,pyautogui.position().y))
		time.sleep(0.3)

print(msgs.msg(LANG,4))
while not keyboard.is_pressed("p"):
	battle_loc = pyautogui.locateOnScreen(image=msgs.msg(LANG,5),confidence=0.5)
	ok_loc = pyautogui.locateOnScreen(image=msgs.msg(LANG,6),confidence=0.6)
	if battle_loc != None:
		pyautogui.click(battle_loc.left,battle_loc.top)

	if pyautogui.locateOnScreen(image="img/elixir.png",confidence=0.8):
		randslot = random.choice(slots)
		pyautogui.click(randslot[0],randslot[1])
		time.sleep(random.randint(cards_delay[0],cards_delay[1]))
		pyautogui.click(random.randint(window[0][0],window[1][0]),random.randint(window[0][1],window[1][1]))
		time.sleep(random.randint(place_delay[0],place_delay[1]))

	if ok_loc != None:
		pyautogui.click(ok_loc.left,ok_loc.top)
