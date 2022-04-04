import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
	r.adjust_for_ambient_noise(source)

while True:
	with sr.Microphone() as source:
		audio = r.listen(source)
	try:
		a=r.recognize_google(audio)
		print(f"{a}")
	except:
		print("sorry, didn't get that")
