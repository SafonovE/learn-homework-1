"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""


def hello_user():
  user_say = ''
  while True:
    try:
      user_say = input('Как дела? ').lower().capitalize()
      if user_say == 'Хорошо':
        print('Ну и хорошо раз хорошо')
        break
      else:
        print(f'Что значит твое "{user_say}" ?')
    except KeyboardInterrupt:
            print()
            print("Пока!")
            break


if __name__ == "__main__":
    hello_user()