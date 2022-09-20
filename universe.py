import random
import string


a = 10

b = 20

d = 40



programming_language = 'Python'


language = 'Portuguese'


favorite_food = 'italian'




food_types = ['italian', 'japanese', 'brazilian', 'american', 'french']



temperature = random.randint(0,30)



creator = 'Ricardo'



names = {

    'creator': 'Ricardo'

}




print(temperature)




bed_type = 'Comfortable'

bed_width = 1.5

bed_length = 3.0





def check_temperature(temp):

    if temp > 15:

        print('Warm Day')

    elif temp < 15:

        print('Cold Day')






all_digits = string.digits






check_temperature(temperature)








print(all_digits)











tft = 'teamfight tactics'











champions = ['felix', 'orb', 'tera', 'quintes']








class Felix:
    """Felix Character class"""


    base_hp = 570

    base_mana = 240


    with_bird = False


    def first_skill(self):

        # This skill calls felix's bird to his hand
        self.with_bird = True