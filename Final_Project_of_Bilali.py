class Recipe:

    def __init__(self,salt,butter,water,cooking_time):

        self.salt = salt
        self.butter = butter
        self.water = water
        self.cooking_time = cooking_time

    def show_ingredients(self):
        print(""" 

Salt(spoon): {}

Butter(spoon): {}

Water(glass): {}

    """.format(self.salt, self.butter, self.water))


    def cooking(self):
        
        print(""" 

Cooking Time(minute): {}
        
        """.format(self.cooking_time))        


    def make(self,crux):

        self.crux = crux

        print("Crux:",self.crux)

            

class rice_pilaf(Recipe):
    
    def __init__(self, salt, butter, water, cooking_time):
        super().__init__(salt, butter, water, cooking_time)
    
    def show_ingredients(self,rice,olive_oil): #Overriding method for different ingredients
        
        self.rice = rice
        self.olive_oil = olive_oil
        
        print(""" 

The İngredients of The Rice Pilaf:

Rice(glass): {}

Salt(spoon): {}

Butter(spoon): {}

Water(glass): {}

Olive Oil(spoon): {}

    """.format(self.rice,self.salt, self.butter, self.water,self.olive_oil))
        
        

class Pasta(Recipe):
    
    def __init__(self, salt, butter, water, cooking_time):
        super().__init__(salt, butter, water, cooking_time)

    def show_ingredients(self,pasta1):
        
        self.pasta = pasta1

        print(""" 

The İngredients of The Paste:

Pasta(gr): {}

Salt(spoon): {}

Butter(spoon): {}

Water(glass): {}

    """.format(self.pasta, self.salt, self.butter, self.water))
        


class lentil_soup(Recipe):
    def __init__(self, salt, butter, water, cooking_time):
        super().__init__(salt, butter, water, cooking_time)

    def show_ingredients(self, onion, garlic, lentil, flour, b_p, cumin):
        
        self.onion = onion
        self.garlic = garlic
        self.lentil = lentil 
        self.flour = flour
        self.b_p = b_p
        self.cumin = cumin

        print(""" 

The İngredients of The Lentil Soup:

Salt(spoon): {}

Butter(spoon): {}

Water(glass): {}

Onion(piece): {}

Garlic(clove): {}

Lentil(glass): {}

Flour(spoon): {}

Black Pepper(teaspoon): {}

Cumin(teaspoon): {}
    """.format(self.salt, self.butter, self.water, self.onion, self.garlic, self.lentil, self.flour, self.b_p, self.cumin))        



while True:
    print(""" 
   
1-) Rice Pilaf

2-) Macaroni

3-) Lentil Soup

Press'q' to EXİT

    """)
    
    main_choice = input("\nWhich food do you want to cook:")
    list1 = ["q", "Q", "exit", "Exit", "EXIT"]
    if main_choice in list1:
        print("\nThanks for visiting...")
        break
    
    elif main_choice == "1":
        print(""" 

1-) İngredients

2-) Cooking Time

3-) Crux

Return to Main Menu: Press'q'
        """)
        
        while True:
            second_choice = input("\nWhat do you want to learn about Rice Pilaf:")
            
            if second_choice in list1:
                break
            
            elif second_choice == "1":
                r1 = rice_pilaf("some", 3, 2.5, "untill you say that like 'where is the water?'")
                r1.show_ingredients(2, 1)

            elif second_choice == "2":
                r1.cooking()

            elif second_choice == "3":
                r1.make("\nDon't use sunflower oil, you have to use olive oil...")
            
            else:
                print("\nWe are working on some updates, please stay with us!!!")
                continue
    
    elif main_choice == "2":
        print(""" 

1-) İngredients

2-) Cooking Time

3-) Crux

Return to Main Menu: Press'q'
        """)
        
        while True:
            second_choice = input("\nWhat do you want to learn about Macaroni:")
            
            if second_choice in list1:
                break
            
            elif second_choice == "1":
                p1 = Pasta(1, 1, 8, 13)
                p1.show_ingredients(250)

            elif second_choice == "2":
                p1.cooking()
                
            elif second_choice == "3":
                p1.make("\nDon't forget to add cold water in cooking time...")
            
            else:
                print("\nWe are working on some updates, please stay with us!!!")
                continue

    elif main_choice == "3":

        print(""" 

1-) İngredients

2-) Cooking Time

3-) Crux

Return to Main Menu: Press'q'
        """)
        
        while True:
            second_choice = input("\nWhat do you want to learn about Lentil Soup:")
            
            if second_choice in list1:
                break
            
            elif second_choice == "1":
                l1 = lentil_soup(1.5, 1.5, 6, 30)
                l1.show_ingredients(1,1,1,1,0.5,1)

            elif second_choice == "2":
                l1.cooking()

            elif second_choice == "3":
                l1.make("\nYou should use a blender to get proper consistency...")
            
            else:
                print("\nWe are working on some updates, please stay with us!!!")
                continue

    else:
        print("\nWe are working on some updates, please stay with us!!!")
        