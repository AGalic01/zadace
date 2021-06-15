def prva(ime):
  return ("Pozdrav",{ime},"!")
print(prva("Antonela"))

druga=lambda x: ("Dobrodosao" ,{x}, "!")
print(druga("Antonela"))

def treca():
  return druga("Antonela")
print(treca())
