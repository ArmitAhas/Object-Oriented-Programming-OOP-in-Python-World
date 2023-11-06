import datetime

print(" -------------------------MENU-------------------------\n"
      "            FOOD                           PRICE           "
      "\n      ITALIAN PIZZA                    13.00 $"
      "\n      AMERICAN PIZZA                   12.80 $ "
      "\n      BURGER                            7.99 $ "
      "\n      CHEESE BURGER                     8.99 $"
      "\n      SALAD                             4.99 $"
      "\n      FRENCH FRIES                      6.99 $"
      "\n      COLA                              5.99 $"
      "\n      WATER                             2.00 $")
print("**********************            ***********************")

# n : Number of items
class resturant :
      def __init__(self,n1,italian_pizza,n2,american_pizza,n3,burger
                   ,n4,cheese_burger,n5,salad,n6,french_fries,n7,cola,n8,water):
       self.n1= n1
       self.italian_pizza= 13.00
       self.n2= n2
       self.american_pizza = 12.80
       self.n3 = n3
       self.burger = 7.99
       self.n4 = n4
       self.cheese_burger = 8.99
       self.n5 = n5
       self.salad = 4.99
       self.n6 = n6
       self.french_fries = 6.99
       self.n7 = n7
       self.cola = 5.99
       self.n8 = n8
       self.water = 2.00
          


      def factor(self):
            f=((self.n1 * self.italian_pizza) + (self.n2 * self.american_pizza) + (self.n3 * self.burger) + (self.n4 * self.cheese_burger) +
            (self.n5 * self.salad) + (self.n6 * self.french_fries) + (self.n7 * self.cola) + (self.n8 * self.water))
            tax = f * 0.09
            service = f * 0.15
            total = f + tax + service
            date = datetime.datetime.today()
            print("\n------------------FACTOR------------------"
                  "\n",date.year,"/",date.month,"/",date.day,"\t",date.hour,":",date.minute,":",date.second,
                  "\n   Price   : ",f,
                  "\n   Tax     : " ,int(tax),
                  "\n   Service : ",int(service),
                  "\n __________________________________________ "
                  "\n   Total Price : ",int(total))



# For example :
order1=resturant(2,"italian_pizza",1,"american_pizza",0,"burger",0,"cheese_burger",1,"salad",1,"french_fries",6,"cola",0,"water")
order1.factor()