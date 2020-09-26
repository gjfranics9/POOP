import random
class Crop:
    """A generic food crop"""

    #constructor
    def __init__(self,growth_rate, light_need, water_need):
        #attributes with initial value

        self._growth = 0
        self._height = 0
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._light_need = light_need
        self._water_need = water_need
        self._status = "Seed"
        self._type = "Generic"

    def rate(self):
        return{'growth rate': self._growth_rate}
    
    def needs(self):
      return {'water need': self._water_need, 'light need': self._light_need}

    def report(self):
      return {'type': self._type, 'status': self._status, 'growth': self._growth, 'days growing': self._days_growing}

    def _update_status(self):
        if self._growth > 15:
            self._status = "Old"
        elif self._growth > 10:
            self._status = "Mature"
        elif self._growth > 5:
            self._status = "Young"
        elif self._growth > 0:
            self._status = "Seedling"
        elif self._growth == 0:
            self._status = "Seed"
            

    def grow(self,light,water):
        if light >= self._light_need and water >= self._water_need:
            self._growth += self._growth_rate
        #number of days growing
        self._days_growing += 1
        #update status
        self._update_status()
        
def auto_grow(crop, days):
    #grow the crop
    for day in range(days):
        light = random.randint(1,10)
        water = random.randint(1,10)
        crop.grow(light,water)
def manual_grow(crop):
    #light and water values input
    valid = False
    while not valid:
        try:
            light = int(input("Please enter a light value (1-10): "))
            if 1 <= light <=10:
                valid = True
            else:
                print("Value entered not valid - please enter a value between 1 and 10")
        except:
            print("Value entered not valid - please enter a value between 1 and 10")
    valid = False
    while not valid:
        try:
            water = int(input("Please enter a water value (1-10): "))
            if 1 <= water <= 10:
                valid = True
            else:
                print("Value entered not valid - please enter a value between 1 and 10")
        except:
            print("Value entered not valid - please enter a value between 1 and 10")
    crop.grow(light,water)

#test
def main():
    #instansiate class
    new_crop = Crop(1,4,3)
    print(new_crop.rate())
    print(new_crop.needs())
    print(new_crop.report())
##    auto_grow(new_crop, 5)
    manual_grow(new_crop)
    print(new_crop.report())

if __name__ == "__main__":
    main()
