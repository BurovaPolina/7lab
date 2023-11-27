from weekdiet import WeekiDiet

days = 7

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