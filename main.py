from engine import SentinelBusiness as eg

class GUIMenu(eg):

    def __init__(self):
        # use super to initialize the parent with empty values first
        super().__init__(name="", revenue=0, costs=0)
        self.questions3 = True # while loop control
        self.opt = {1 : "Marketing" , 2 : "Servers", 3 : "Salaries"} # initial dictionary
                
    def questions2(self): # menu with questions
        print("***************")
        print("****Welcome****")
        print("***************\n")
        
        # we ask for basic data to fill the parent's attributes
        self.name = input("Enter Business Name: ")
        self.revenue = float(input(f"Enter Monthly Revenue for {self.name}: "))

        print("\nFor exit menu type 0 :")

        self.opt1 = float(input("*How much money you have invested on for attract new clients this month?* : "))
        self.opt2 = float(input("*Which is the cost for maintain the platform online* : "))
        self.opt3 = float(input("*How much money you have invested on for attract new clients this month?* : "))
        
        # initial total calculation
        total = self.opt1 + self.opt2 + self.opt3

        while self.questions3 is True:
            self.bt = input("\nOkay, you have another category to add? (yes/no): ")
            self.bt = self.bt.lower() # lower to avoid input errors
                
            if self.bt == "yes":
                new_opt = input("How do you call this new option for bill pay? : ")
                total_value = float(input(f"Okay, What is the total value for [{new_opt}]? "))
                
                
                self.opt[new_opt] = total_value
                total += total_value 

                print(f"\nUpdated options: {self.opt}")
                print(f"Current total: {total}")
            else:
                # if the user says no or anything else close the iteration
                print(f"\nClosing expense registration, final total: {total}")
                self.questions3 = False
        
        # we pass the final total to self.costs
        self.costs = total
        
 
        print("\n" + "="*20)
        print(f"BUSINESS STATUS: {self.get_health_status()}")
        print(f"MARGIN: {self.calculate_margin():.2f}%")
        print("="*20)
        
        return total

# EXEEC
if __name__ == "__main__":
    menu = GUIMenu()
    menu.questions2()
                