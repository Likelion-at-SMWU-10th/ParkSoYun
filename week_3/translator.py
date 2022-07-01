from googletrans import Translator

trans=Translator()
#sen="안녕하세요 코드라이언입니다."
sen=input('번역을 원하는 문장을 입력해주세요: ')
lan=input('원하는 언어를 입력해주세요: ')
#detct=trans.detect(sen)
#print(detct.lang)
rslt=trans.translate(sen,lan) #version: 4.0.0-rc1
detct=trans.detect(sen)
print('=========출력결과=========')
print(detct.lang,':',sen)
print(rslt.dest,':',rslt.text)
print('==========================')