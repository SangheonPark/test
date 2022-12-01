import gamepkg.game
name= input('이름을 입력하시오.')
c= int(input('시작할 돈을 입력하시오 ( 1000원과 2000원 중 선택하시오.)'))
count = 0
print('당신은 목표 금액인 15000원을 달성해야 합니다.')
while True:
  count += 1 
  choose= input('홀과 짝중 하나를선택하시오 게임이 시작됩니다')
  

  instanceg=Game(name,c,choose)
  
  while instanceg.is_valid2(choose)== False:
      choose= input('홀과 짝중 하나를선택하시오 게임이 시작됩니다')
  instanceg.inform()
  instanceg.inform2()

  instanceg.makeA()
  instanceg.uanswer()
  c = instanceg.money_cal()
  print('당신의 돈은 {}입니다 '.format(c))
  
  if instanceg.go_stop() == False :
    break
  else :
    continue
