from engine import SentinelBusiness as eg

class GUIMenu():

    def __init__(self,questions3,bt,opt,select,otp):
            self.questions3 = questions3
            self.bt= bt
            self.opt = opt
            self.select = select
            self.otp = otp
            
            opt =  {1 : "Marketing" , 2 : "Servers ", 3 : "Salaries"  }
                
            def questions2(self):

                print("***************")
                print("****Welcome****")
                print("***************\n")
                
                print("For exit menu type 0 :")
        
                          
                while questions3 is True:
                    self.opt1 = float(input("*How much money you have invested on for attract new clients this month?* : "))
                    self.opt2 = float(input("*Which is the cost for maintain the platform online* : "))
                    self.opt3 = float(input("*How much money you have invested on for attract new clients this month?* : "))
                    self.bt = input("Okay, you have another categor for add something? ")
                    bt.lower()
                    
                    if self.bt =="yes":
                         new_opt = input(("How do you call this new option for bill pay? :  "))
                         total_value= float(input(f"Okay, What is the total value for [{new_opt}] "))
                         opt[new_opt] = total_value
                         print(f"\nUpdated options: {opt}")
                    
    
    
    
                    
                
                
                
                
                
                
                