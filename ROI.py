#how much will my rental property have on income, my expenses(monthly, property tax, mortgage insurance ect.),  my cash flow is income vs expenses
#my ROI(return on investment) how much money did i spend getting the property down payment, closing cost, money to fix it up
# you will times your cash flow times 12 to know how much your making per year
# you will divide your annual cash flow by how much you invested then times 100 to get you ROI percentage and thats what given back to user 


class rentalInvest():

    def __init__(self, income= [None], expenses =[None], cashflow= [None], roi = [None], total = [None]):
        self.income = income
        self.expenses = expenses
        self.cashflow = cashflow
        self.roi = roi
        self.total = total

    def incomes(self):
        x = int(input("How much income does the property generate?\n"))
        if x >= 0:
            self.income[0]= x
            print(self.income)
        else: 
            print('Invalid Amount')
            self.incomes()
       
    def expense(self):
        y= int(input("What is the total monthly expenses for the property? Property tax, Insuarance, Mortgage ect...\n"))
        if y <= 0:
            print('Invalid Amount')
            self.expense()
        else:
            self.expenses[0] = y
            print(self.expenses)

    def cashflows(self):
        j=input("Enter yes to calculate your annual cash flow.\n")
        if j.lower() == "yes":
            p = (self.income[0]-self.expenses[0])*12
            self.cashflow[0] = p
            print(self.cashflow)
        else:
            self.cashflows()
       

    def rois(self):
        i = int(input('Total amount invested into property? Down payment, Closing Cost, Rehab Budget ect...\n'))
        if i <= 0:
            print('Invalid amount')
            self.rois
        else: 
            self.roi[0] = i
            resp = input('Enter yes to calculate your ROI.\n')
            if resp.lower() == 'yes':
                w = (self.cashflow[0] / self.roi[0])*100
                self.total[0] = w
                print("\nProperty Summary\n")
                print(f'\nMonthly income for property.\n{self.income}\n')
                print(f'\nMonthly total expenses from the property.\n{self.expenses}\n')
                print(f'\nAnnual cash flow from the property.\n{self.cashflow}\n')
                print(f'\nTotal cash invested into property.\n{self.roi}\n')
                print(f"\nYour return of investment for the property.\n{self.total} %\n")
            else:
                self.rois()
        e = input('Would you like to run another ROI for a different property? Enter yes to continue, enter no to go to the main menu.\n')
        while True:
            if e.lower() == 'yes':
                self.incomes()
                self.expense()
                self.cashflows()
                self.rois()

            else:
                break
                
    def runCalculator(self):
        while True:
            response = input("Would you like to see your ROI for the property? Enter yes to begin or no to cancel. \n")
            if response.lower() == 'yes':
                self.incomes()
                self.expense()
                self.cashflows()
                self.rois()
            elif response.lower() == 'no':
                print(f'\nThank you for using our services have a great day!\n')
                break
            
            else:
                self.runCalculator

property = rentalInvest()
property.runCalculator()
