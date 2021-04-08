name = input("What's your name?: ")

def greet(lang):
  if lang == 'es':
    return 'Hola!
  elif lang == 'fr':
    return 'Bonjour!'
  else:
    return 'Hello'
print(greet('en'), name)

print(greet('es'), name)
print(greet('fr'), name)
