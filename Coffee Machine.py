class CoffeeMachine:
    def __init__(self, water, milk, beans, disposable_cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.disposable_cups = disposable_cups
        self.money = money

    def has(self):
        print('''The coffee machine has:
{} of water
{} of milk
{} of coffee beans
{} of disposable cups
${} of money
    '''.format(self.water, self.milk, self.beans, self.disposable_cups, self.money))

    def make_espresso(self):
        if self.water >= 250 and self.beans >= 16 and self.disposable_cups >= 1:
            print("I have enough resources, making you a coffee!")
            print()
            self.water -= 250
            self.beans -= 16
            self.milk -= 0
            self.disposable_cups -= 1
            self.money += 4
        elif self.water < 250:
            print("Sorry, not enough water!")
            print()
        elif self.beans < 16:
            print("Sorry, not enough coffee beans!")
            print()
        elif self.disposable_cups < 1:
            print("Sorry, not enough disposable cups!")
            print()

    def make_latte(self):
        if self.water >= 350 and self.milk >= 75 and self.beans >= 20 and self.disposable_cups >= 1:
            print("I have enough resources, making you a coffee!")
            self.water -= 350
            self.milk -= 75
            self.beans -= 20
            self.disposable_cups -= 1
            self.money += 7
        elif self.water < 350:
            print("Sorry, not enough water!")
        elif self.beans < 20:
            print("Sorry, not enough coffee beans!")
        elif self.milk < 75:
            print("Sorry, not enough milk!")
        elif self.disposable_cups < 1:
            print("Sorry, not enough disposable cups!")

    def make_cappuccino(self):
        if self.water >= 200 and self.milk >= 100 and self.beans >= 12 and self.disposable_cups >= 1:
            print("I have enough resources, making you a coffee!")
            print()
            self.water -= 200
            self.milk -= 100
            self.beans -= 12
            self.disposable_cups -= 1
            self.money += 6
        elif self.water < 200:
            print("Sorry, not enough water!")
        elif self.beans < 12:
            print("Sorry, not enough coffee beans!")
        elif self.milk < 100:
            print("Sorry, not enough milk!")
        elif self.disposable_cups < 1:
            print("Sorry, not enough disposable cups!")

    def act_buy(self):
        value = input("""What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:
""")
        if value == 'back':
            print()      
            CoffeeMachine.action(self)
        else:
            value_1 = int(value)
            if value_1 == 1:
                CoffeeMachine.make_espresso(self)
                print()
            elif value_1 == 2:
                CoffeeMachine.make_latte(self)
                print()
            elif value_1 == 3:
                CoffeeMachine.make_cappuccino(self)
                print()

    def act_fill(self):
        print()
        print("""Write how many ml of water you want to add:
""")
        add_water = int(input())
        print("""Write how many ml of milk you want to add:
""")
        add_milk = int(input())
        print("""Write how many grams of coffee beans you want to add:
""")
        add_beans = int(input())
        print("""Write how many disposable cups you want to add:
""")
        add_disposable_cups = int(input())
        self.water += add_water
        self.milk += add_milk
        self.beans += add_beans
        self.disposable_cups += add_disposable_cups

    def act_take(self):
        print()
        print('I gave you ${}'.format(self.money))
        print()
        print()
        self.money -= self.money

    def action(self):
        while True:
            action = str(input("""Write action (buy, fill, take, remaining, exit):
"""))
            if action == "buy":
                print()
                CoffeeMachine.act_buy(self)
            elif action == "fill":
                print()
                CoffeeMachine.act_fill(self)
            elif action == "take":
                print()
                CoffeeMachine.act_take(self)
            elif action == "remaining":
                print()
                CoffeeMachine.has(self)
            elif action == 'exit':
                exit()
                            
    
               

coffeemachine = CoffeeMachine(400, 540, 120, 9, 550)
coffeemachine.action()















