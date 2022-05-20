"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def hello_user():
  user_say = ''
  while True:
    user_say = input('Как дела? ').lower().capitalize()
    if user_say == 'Хорошо':
      print('Ну и хорошо раз хорошо')
      break
    else:
      print(f'Что значит твое "{user_say}" ?')


if __name__ == "__main__":
    hello_user()


