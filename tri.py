def skoliko_bukv(slovo):
  text =slovo
  text = text.replace(" ", "")
  tex = list(text)
  twotext = tex
  chet = 0
  chet2 = -1
  kol = 0
  povtor = []
  while chet < len(text)-1:
    for i in tex:
      if twotext[chet] == i:
        kol = kol + 1
    povtor.append(str(kol))
    povtor.append(" буква-ы ")
    povtor.append(twotext[chet]+"; ")
    if kol > 1:
      twotext = ''.join(twotext)
      twotext = twotext.replace(twotext[chet], " ")
      twotext = list(twotext)
    kol = 0
    chet = chet + 1
  
  david = 0
  while david < len(povtor):
    if povtor[david] == " ":
      povtor.pop(david + 2)
      povtor.pop(david +1)
      povtor.pop(david)
      david = david - 3
    david = david + 1
  povtor = ''.join(povtor)
  return(povtor)
  
bl = str(input("введите слово"))
print (skoliko_bukv(bl))