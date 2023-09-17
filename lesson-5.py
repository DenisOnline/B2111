# name = "Denis"
# age = 21
# PI = 3.14159265
# x = age / PI
# print(f"Привет, {name}")
# print(f"Привет, {name * 2}")
# print(f"Привет, {len(name)}")
# print(f"Привет, {name}. Тебе {age} лет?")
# print(f"Привет, {name:25}")
# print(f"Тебе {age:15d} лет?")
# print(f"Тебе {age:15n} лет?")
# print(f"Привет, {name:25s}")
# print(f"Число PI = {PI:.4f}")
# print(f"Число PI = {x:5.3%}")
# print(f"Тебе {age:<15d} лет?")
# print(f"Привет, {name:>}")
# print(f"Привет, {name:^}")
# print("Тебе {:15n} лет?".format(age))
# print("Привет, {1:10d}. Тебе {0} лет?".format(name, age))
# print("Привет, {name:10s}. Тебе {age} лет?".format(name="Олег", age=22))
# print("Hello \nworld")
# print("Hello wor\bld")
# print("Hello\tworld")
# print("Hello\rworld")

details_damage_price = {"energy gun": 100,
                        "minigun": 70,
                        "Thor hammer": 50,
                        "laser gun": 80,
                        "rail gun": 90,
                        "sniper rifle": 150}
details_survive_price = {"shield": 50,
                         "energyshield": 80,
                         "resist": 30,
                         "evasion": 100,
                         "armor": 140}
users_bot = {}
player_list = []


def player_maker(player_list):
    user_choose = "yes"
    while user_choose == "yes" or user_choose == "y":
        user_input = input("Input a Player name – ")
        if len(user_input) < 3:
            continue
        player_list.append(str.capitalize(user_input))
        user_choose = input("More players – Y/N – ")
        print(f"Players – {str(player_list)[1:-1]}")


def bot_maker(start_sum, player_list):
    for player in player_list:
        wallet = start_sum
        users_bot[player] = {}
        while wallet >= min(details_damage_price.values()):
            string_1 = f"{player}, you have {wallet} coins"
            print(f"{string_1:=^82}")
            string_2 = "You can buy:"
            print(f"{string_2:-^82}")
            print("{detail:^^80}".format(detail="Damagedealdetails"))
            for gun, price in details_damage_price.items():
                print(f"{gun} – {price}")
                print("{detail:^^80}".format(detail="Survivedetails"))
            for survive_detail, price in details_survive_price.items():
                print(f"{survive_detail} – {price}")
            user_choose = str.lower(input("Choose thedetail – "))
            if user_choose in users_bot[player].keys():
                print("{string:!^80}".format(string="Your bot has this detail"))
                continue
            if user_choose in details_damage_price.keys():
                if wallet < details_damage_price[user_choose]:
                    print("{string:!^80}".format(string="Not enough coins"))
                    continue
                wallet -= details_damage_price[user_choose]
                users_bot[player][user_choose] = details_damage_price[user_choose]
            else:
                if user_choose in details_survive_price.keys():
                    if wallet < details_survive_price[user_choose]:
                        print("{string:!^80}\n".format(string="Not enough coins"))
                        continue
                    wallet -= details_survive_price[user_choose]
                    users_bot[player][user_choose] = details_survive_price[user_choose]
                else:
                    print("\nYour choose is wrong!\n")
                    continue
            print(f"\n\n{player} bot details: {str(users_bot[player].keys())[11:-2]} \n\n")
    for player in player_list:
        print(f"{player} bot details:{str(users_bot[player].keys())[11:-2]}")


player_maker(player_list)
start_sum = int(input("Input start capital – "))
max_start_sum = sum(details_damage_price.values()) + sum(details_survive_price.values())
min_start_sum = min(details_damage_price.values())
if start_sum > max_start_sum:
    start_sum = max_start_sum
if start_sum < min_start_sum:
    start_sum = min_start_sum
bot_maker(start_sum=start_sum, player_list=player_list)