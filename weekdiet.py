"""Задание состоит из двух частей:
1 часть – написать программу в соответствии со своим вариантом задания.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно ограничение
на характеристики объектов и целевую функцию для оптимизации решения.

В холодильнике 10 брикетов мороженого разного вида. Ребенку разрешается взять вечером не более 2 брикетов.
Подготовьте различные варианты поедания мороженного ребенком на неделю."""


from icecream import Ice_cream

class WeekiDiet:
    full_list = []

    def init(self):
        print("init")
        self.full_list.append(Ice_cream("Шоколад", "качественное", 100))
        self.full_list.append(Ice_cream ("Банан", "некачественное", 150))
        self.full_list.append(Ice_cream ("Клубника", "некачественное", 120))
        self.full_list.append(Ice_cream ("Апельсин", "качественное", 80))
        self.full_list.append(Ice_cream ("Ваниль", "некачественное", 110))
        self.full_list.append(Ice_cream ("Лесные ягоды", "качественное", 90))
        self.full_list.append(Ice_cream ("Облепиха", "некачественное", 130))
        self.full_list.append(Ice_cream ("Смородина", "качественное", 70))
        self.full_list.append(Ice_cream ("Крем-брюле", "некачественное", 140))
        self.full_list.append(Ice_cream ("Сыр", "качественное", 60))


    # вернуть полный список для разных вариантов
    def get_full_list(self):
        return self.full_list


    # получить количество каллорий для списка combination
    def calculate_total_calories(self, combination):
        return sum(ice_cream.energy for ice_cream in combination)

    # выборка для всех вариантов от текущего day
    def default_selection(self, ice_creams, day, days):
        for sub_day in range(day, days):
            # проходим для каждого по выборке от 0 до 2
            total_calories = 0
            for selection in range(3):
                print('День:', sub_day + 1)
                if len(ice_creams[:selection]) == 0:
                    print('список пуст, количесиво калорий 0')
                else:
                    total_calories += self.calculate_total_calories(ice_creams[selection:])
                    print('количество калорий в день', sub_day, ' :', self.calculate_total_calories(ice_creams[selection:]))
                    print( *ice_creams[:selection], "\n")
                del ice_creams[:selection]
        return total_calories
