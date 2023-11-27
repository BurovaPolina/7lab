days = 7


class Ice_cream:
   def __init__(self, name, quality, energy):
      self.name = name
      self.quality = quality
      self.energy = energy

   name = ''
   quality = ''
   energy = 0

   def __str__(self):
      return 'name:' + self.name + ' quality:' + self.quality + ' energy:' + str(self.energy)

class WeekiDiet:
   full_list = []

   def init(self):
      print("init")
      self.full_list.append(Ice_cream("Шоколад", "качественное", 100))
      self.full_list.append(Ice_cream("Банан", "некачественное", 150))
      self.full_list.append(Ice_cream("Клубника", "некачественное", 120))
      self.full_list.append(Ice_cream("Апельсин", "качественное", 80))
      self.full_list.append(Ice_cream("Ваниль", "некачественное", 110))
      self.full_list.append(Ice_cream("Лесные ягоды", "качественное", 90))
      self.full_list.append(Ice_cream("Облепиха", "некачественное", 130))
      self.full_list.append(Ice_cream("Смородина", "качественное", 70))
      self.full_list.append(Ice_cream("Крем-брюле", "некачественное", 140))
      self.full_list.append(Ice_cream("Сыр", "качественное", 60))

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
               print(*ice_creams[:selection], "\n")
            del ice_creams[:selection]
      return total_calories

def main():
   wd = WeekiDiet()
   wd.init()

   calc1(wd)
   wd.init()
   calc2(wd)

def calc1(wd: WeekiDiet):
   print("==========================================")
   print("Берем мороженое без ограничения от 0 до 2")
   print("==========================================")
   total_calories = 0
   # проходим по дням каждый с каждым
   for day in range(days):
      ice_creams = wd.get_full_list()
      total_calories += wd.default_selection(ice_creams, day, days)

   print('общее количество калорий: ', total_calories, '\n\n')

   print("==========================================")
   print("Берем мороженое сначало с минимальными каллориями")
   print("==========================================")

   total_calories = 0
   # проходим по дням каждый с каждым
   for day in range(days):
      ice_creams = wd.get_full_list()
      print('общее количество калорий: ', total_calories, '\n\n')
      # сортируем предпочтение тем что с минимальными каллориями
      ice_creams = sorted(ice_creams, key=lambda ice_cream: ice_cream[2])
      total_calories += wd.default_selection(ice_creams, day, days)
   print('общее количество калорий: ', total_calories, '\n\n')

def calc2(wd: WeekiDiet):
   total_calories = 0
   print("==========================================")
   print("Берем мороженое сначало качественное")
   print("==========================================")

   # проходим по дням каждый с каждым
   for day in range(days):
      ice_creams = wd.get_full_list()

      # сортируем предпочтение качественному
      ice_creams = sorted(ice_creams, key=lambda ice_cream: ice_cream.quality)
      total_calories += wd.default_selection(ice_creams, day, days)
   print('общее количество калорий: ', total_calories)


main()
