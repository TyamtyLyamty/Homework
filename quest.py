import random
class Player:
    def __init__(self):
        self.money = 100
        self.wins = 0
    def lost_money(self, amount):
        self.money -= amount
        print(f"Количество рублей уменьшилось на {amount}. Осталось {self.money}")
    def win_money(self, amount):
        self.money += amount
        print(f"Количество рублей увеличилось на {amount}. Всего денег {self.money}")
    def add_win(self):
        self.wins += 1
        print(f'Всего побед {self.wins}')



class NotImplementedException (Exception):
    pass

def nap():
    while True:

        while True:
            try:
                print('''Вы подходите к мужику ближе. Он это замечает и готовится к игре
                   - "Ну, начнем" - говорит вам мужик и с ехидной улыбкой потирает ладони
                   Он показывает вам шарик под одним из трех наперстков, потом быстро их перемешивает между собой''')
                bet = int(input(f'У вас есть {player.money}. Введите вашу ставку: '))
                if bet <=0:
                    print('Сумма ставки должна быть больше 0')
                    continue
                elif bet > player.money:
                    print(f'Недостаточно денег. У вас {player.money}')
                    continue
                else:
                    break
            except ValueError:
                print('Пожалуйста, введите число')
        while True:
            n = input('Под каким наперстком оказался шарик?(1-3)')
            if n in ['1','2','3']:
                break
            print('Пожалуйста, введите 1, 2 или 3')

        win = random.randint(1, 3)
        if int(n) == win:
            print('''Вы выиграли!
            - "Вот досада, может сыграем еще?" - говорит мужик''')
            player.win_money(bet)
            player.add_win()
        else:
            print(f'''Вы проиграли, шарик оказался под {win} наперстком
            - "Ну ничего, повезет в следующий раз - с довольным лицом говорит мужик - хотите отыграться?"''')
            player.lost_money(bet)
        if player.money <= 0:
            print('У вас закончились деньги!')
            break

        while True:
            try:
                repeat = input('Попытать удачу еще раз? (да/нет)').strip().lower()
                if repeat == 'да':
                    print('- Отлично! Давай еще раз! - говорит мужик')
                    break
                elif repeat == 'нет':
                    print('- Ну, как знаешь, приходи еще! - говорит мужик')
                    print(f"\n=== Итог игры ===")
                    print(f"Ваш финальный баланс: {player.money} рублей")
                    print(f"Количество побед: {player.wins}")
                    return
                else:
                    print('Пожалуйста, введите да или нет')

            except NotImplementedException as e:
                print(f'Произошла ошибка:{e}')

def nope():
    raise NotImplementedException('''Вы идете дальше по своим делам
                - "Ну и не очень то хотелось" - кричит мужик вам в след
                Зато вы сохранили достоинство.''')
def card():
    raise NotImplementedException('''- Нет, в карты я не игрок. Не хочешь в наперстки - иди куда шел
           Вы пожали плечами и дальше пошли по своим делам''')


print('''Вы идете по городскому рынку, как вдруг вас кто-то подзывает к себе:
      - "Эй,мужик, не хочешь в наперстки сыграть?"
      Вы оборачиваетесь и видите сидящего на табурете забулдыгу, который рукой подзывает вас к себе.
      Перед вами стоит выбор как поступить: 
      1. Согласиться сыграть в наперстки .
      2. Сделать вид что это не вам и пройти дальше
      3. Предложить мужику сыграть в карты''')

player = Player()

while True:
        choise = input("Вам предстоит сделать выбор: (1), (2), (3)")

        try:
            if '1' == choise:
                nap()
                break
            elif '2' == choise:
                nope()
                break
            elif '3' == choise:
                card()
                break
            else:
                print('Пожалуйста, выберите 1,2 или 3')
        except ValueError as e:
            print(f'Необходимо ввести цифру от 1 до 3')
        except NotImplementedException as e:
            print(f'{e}')

if __name__ == '__main__':
    player = Player()