import random


def get_random_digits(count: int) -> str:
    random_num = ''
    for i in range(count):
        random_num += str(random.randint(0, 9))
    return random_num


class BankAccount:
    def __init__(self, card_holder):
        self.card_holder = card_holder.upper()
        self.money = 0
        self.account_number = get_random_digits(20)
        self.card_number = get_random_digits(16)


class Bank:
    def __int__(self):
        self.__bank_accounts: list[BankAccount] = []

    def open_account(self, card_holder) -> BankAccount:
        new_account = BankAccount(card_holder)
        self.__bank_accounts.append(new_account)
        return new_account

    def __get_account(self, account_number: str) -> BankAccount:
        for new_account in self.__bank_accounts:
            if new_account.account_number == account_number:
                return new_account
        return None

    def get_all_bank_accounts(self) -> list[BankAccount]:
        return self.__bank_accounts

    def add_money(self, account_number: str, money: float) -> BankAccount:
        account = self.__get_account(account_number)
        account.money += money

    def transfer_money(self, from_account_number, to_account_number, money):
        from_account = self.__get_account(from_account_number)
        to_account = self.__get_account(to_account_number)
        from_account.money -= money
        to_account.money += money

    def external_transfer(self, from_account_number, to_external_number, money):
        from_account = self.__get_account(from_account_number)
        from_account.money -= money

        print(f'Банк перевёл {money} $ с вашего счёта {from_account_number} на внешний счёт {to_external_number}')


class Controller:
    def __int__(self):
        self.bank = Bank()

    def run(self):
        print('Здравствуйте, наш банк открылся!')
        while True:
            print('Выберите действие:')
            print('0. Завершить программу')
            print('1. Открыть новый счёт')
            print('2. Просмотреть открытые счета')
            print('3. Положить деньги на счёт')
            print('4. Перевести деньги между счетами')
            print('5. Совершить платёж')

            action = int(input())
            if action == 0:
                print('До свидания!')
                break
            elif action == 1:
                name_surname = input('Введите имя и фамилию')
                account = self.bank.open_account(name_surname)
                print(f'Счет {account.account_number} создан')
            elif action == 2:
                for account in self.bank.get_all_bank_accounts():
                    print(f'Номер счета: {account.account_number}')
                    print(f'Остаток на счету {account.money} $')
                    print(f'Номер карты {account.card_number}')
                    print(f'Держатель карты {account.card_holder}')
            elif action == 3:
                account_number = input('Введите номер счёта: ')
                summ = float(input('Введите количество денег: '))
                self.bank.add_money(account_number, summ)
            elif action == 4:
                from_account_number = input('Введите номер счёта отправителя: ')
                to_account_number = input('Введите номер счёта получателя: ')
                summ_money = float(input('ведите количество денег: '))
                self.bank.transfer_money(from_account_number, to_account_number, summ_money)
            elif action == 5:
                from_account_num = input('Введите номер счета отправителя: ')
                external_account = input('Введите номер внешнего счета: ')
                money = input('ведите количество денег: ')
                self.bank.external_transfer(from_account_num, external_account, money)
            else:
                print('Неподдерживаемая операция.')



if __name__ == '__main__':
    controller = Controller()
    controller.run()
