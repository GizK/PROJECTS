class FamilyIndividual: #This class is used for adding the family member relationships and displaying them based on the users input.
    def __init__(self, FirstName, SurName, DOB): #The attributes of the family members are initialised.
        self.FirstName = FirstName #First name, surname and DOB  of the family member is not as a list as its a constant.
        self.SurName = SurName
        self.Parents = [] #Empty lists are used for the family members to be added to.
        self.Siblings = []
        self.Spouse = []
        self.Children = []
        self.Cousins = []
        self.DOB = DOB
#Methods to add family member relationships.
    def add_parent(self, parent): #The parents name is taken into the parameters and appended to the attribute "Parents".
        self.Parents.append(parent)

    def add_sibling(self, sibling): #The siblings name is taken into the parameters and appended to the attribute "Sibling".
        self.Siblings.append(sibling)

    def add_spouse(self, spouse):#The spouse name is taken into the parameters and appended to the attribute "Spouse".
        self.Spouse.append(spouse)

    def add_child(self, child): #The child name is taken into the parameters and appended to the attribute "Children" as well as "Parents".
        self.Children.append(child)
        child.Parents.append(self)

    def add_cousin(self, cousin): #The cousin name is taken into the parameters and appended to the attribute "Cousins".
        self.Cousins.append(cousin)

#Methods to display family member relationships.
    def display_siblings(self):
        if self.Siblings:
            print("Siblings of "+ self.FirstName+ " "+ self.SurName + ":")
            for sibling in self.Siblings:
                print(sibling.FirstName + " " + sibling.SurName) #Displays the first name and surname for the siblings of the selected family member of the user.
        else:
            print(self.FirstName + " " + self.SurName + " has no siblings.") #If selected member has no siblings it will display this line.

    def display_cousins(self):
        if self.Cousins:
            print("Cousins of " + self.FirstName + self.SurName +": ")#Displays the first name and surname for the cousins of the selected family member of the user.
            for cousin in self.Cousins:
                print(cousin.FirstName + cousin.SurName)
        else:
            print(self.FirstName + self.SurName + " has no cousins.")#If selected member has no cousins it will display this line.


class FamilyTree: #This class is used to also add the members into one place and to retrieve information about them as well as display data about them based on the users input.
    def __init__(self):
        self.members = {}

    def add_member(self, member): #This method adds the family member into the FamilyTree class by using their full name as a key in the member dictionary.
        FullName = member.FirstName + " " + member.SurName
        self.members[FullName] = member

    def get_member(self, name): #Method to retrieve information about the family member name.
        return self.members.get(name)

#Methods to display family relationships
    def display_parents(self, name):
        member = self.get_member(name) #retrieves the name of the member
        if member:
            Parents = [f"{parent.FirstName} {parent.SurName}" for parent in member.Parents] #Combines the first name and surname of the member to make the full name.
            if Parents:
                print(name +"'s parents: " +", ".join(Parents))
            else:
                print(name+ " has no known parents.") #Message to be displayed if the family member has no parents.
        else:
            print(name +" is not in the family tree.") #Messgae to be displayed if the family member is not found in the family tree.

    def display_grandchildren(self, name):
        member = self.get_member(name)
        if member:
            grandchildren = [grandchild for child in member.Children for grandchild in child.Children] #Collects all grandchildren of the member and puts it in a list.
            if grandchildren:
                print(f"{name}'s grandchildren: {', '.join(f'{grandchild.FirstName} {grandchild.SurName}' for grandchild in grandchildren)}")
                #Combines first name and surname of the grandchild and prints the full name.
            else:
                print(name + " has no known grandchildren.") #If the selected family member has no grandchildren this message will be displayed.
        else:
            print(name + " is not in the family tree.") #If the selected family members name was not found in  the family tree, this message will be displayed.

    #this method is AI generated, in summary it retrieves the immediate family of the selected member, displays their name and it displays the appropriate message if theyre not found in the family tree.
    def display_immediate_family(self, name):
        member = self.get_member(name)
        if member:
            print(name +"'s Immediate Family:")
            print( f" Parents: {', '.join(f'{parent.FirstName} {parent.SurName}' for parent in member.Parents) if member.Parents else 'None'}")
            print( f" Siblings: {', '.join(f'{sibling.FirstName} {sibling.SurName}' for sibling in member.Siblings) if member.Siblings else 'None'}")
            print(f" Spouse: {f'{member.Spouse.FirstName} {member.Spouse.SurName}' if member.Spouse else 'None'}")
            print(f" Children: {', '.join(f'{child.FirstName} {child.SurName}' for child in member.Children) if member.Children else 'None'}")
        else:
            print(name +" is not in the family tree.")

    def display_extended_family(self, name):
        member = self.get_member(name)
        if member:
            extended_family = set(member.Parents + member.Siblings + member.Children) #Creates a set of the members extended family.
            if member.Spouse:
                extended_family.add(member.Spouse) #Adds the spouse to the extended family if the member has one.
            for parent in member.Parents:
                extended_family.update(parent.Children) #Adds the children of the members parent into extended family.
                extended_family.update(parent.Siblings) #Adds the siblings of the members parent into extended family.
            extended_family.discard(member) #Removes the current member from the extended family.
            extended_family_names = [f"{relative.FirstName} {relative.SurName}" for relative in extended_family]
            if extended_family_names:
                print(f"{name}'s Extended Family: {', '.join(extended_family_names)}") #Prints the extended family names in a single string.
            else:
                print(name + " has no known extended family.") #If the family member has no extended family it will display this message.
        else:
            print(name + " is not in the family tree.") #If the name of the selected family member is not found then it will display this message.

    def display_children_count(self):
        total_children = sum(len(member.Children) for member in self.members.values()) #This line sums up the amount of children for each family member.
        average_children = str(total_children / len(self.members))
        print("Number of children per family member:")
        for FullName, member in self.members.items():
            print(member.FirstName+":"+ str(len(member.Children))+" children") #This line displays the amount of children per family member.
        print("Average number of children per person: "+str(average_children)+":") #This line displays the average amount of children in the family tree.

    def display_average_age_at_death(self): #There are no deceased family members hence displays the appropriate message.
        print("No deceased members in the family tree.")

    def start(self, birthday_calendar):
        while True:
            name = input("Enter the full name of a person or 'Exit' to quit: ") #Prompts the user to enter the name of the selected family member of their choice.
            if name.lower() == 'Exit':
                print("Exiting family tree functionality.") #To exit if the user does not want to continue with the program.
                break
            member = self.get_member(name)
            if member:
                print("\nWhat would you like to see?") #A menu is displayed for the user to select from.
                print("1. Siblings")
                print("2. Cousins")
                print("3. Parents")
                print("4. Grandchildren")
                print("5. Immediate Family")
                print("6. Extended Family")
                print("7. Children Count")
                print("8. Average Age at Death")
                choice = input("Enter your choice (1-8): ")
                #Depending on the users choice, the following methods run and displayed.
                if choice == "1":
                    member.display_siblings()
                elif choice == "2":
                    member.display_cousins()
                elif choice == "3":
                    self.display_parents(name)
                elif choice == "4":
                    self.display_grandchildren(name)
                elif choice == "5":
                    self.display_immediate_family(name)
                elif choice == "6":
                    self.display_extended_family(name)
                elif choice == "7":
                    self.display_children_count()
                elif choice == "8":
                    self.display_average_age_at_death()
                else:
                    print("Invalid choice, please select a choice.") #Appropriate message is displayed if the users input is invalid.
            else:
                print(name +" is not found in the family tree.") #Appropriate message is displayed if the selected member is not found in the family tree.

        while True:
            choice = input("Enter 'Calendar' to view the birthday calendar or 'Exit' to quit: ")
            if choice == "Calendar": #If the member wants to view the sorted birthday calendar and the family members birthday, the following method is run and displayed.
                birthday_calendar.display_birthday()
            elif choice == "Exit": #If the user doesnt want to continue with the program, the appropriate message is displayed and program is terminated.
                print("Exiting.")
                break
            else:
                print("Invalid choice, please select a choice.") #If the user inputs an invalid choice, the appropriate message is displayed.


class SortedBirthDayCalendar: #This class displays and retrieves the sorted out birthdays of the family members via month.
    def __init__(self):
        self.members = []

    def add_member(self, member):
        self.members.append(member)

    def display_birthday(self):
        #sorted_members was AI generated.
        sorted_members = sorted(self.members, key=lambda member: member.DOB[3]+member.DOB[4]) #The sorted function sorts out the dates in ascending order and lambda uses the month of the date as a key to sort.
        print("Birthday Calendar")
        for member in sorted_members:
            print(member.FirstName + member.SurName +": "+member.DOB) #The sorted birthdays are displayed along with the fullname of family members

family_tree = FamilyTree() #FamilyTree class is initialised.
calendar = SortedBirthDayCalendar() #SortedBirthdayCalendar is initialised.


# Dads family members are initialised with the attributes of FullName, SurName and DOB.
WilliamJack = FamilyIndividual("William", "Jack", "01/12/1950")
LucyJack = FamilyIndividual("Lucy", "Jack", "02/11/1951")
JonothanJack = FamilyIndividual("Jonothan", "Jack", "03/10/1970")
RichardJack = FamilyIndividual("Richard", "Jack", "04/09/1972")
HenryJack = FamilyIndividual("Henry", "Jack", "05/08/1991")
BillyJack = FamilyIndividual("Billy", "Jack", "01/07/2011")
RobertJack = FamilyIndividual("Robert", "Jack", "02/06/ 2010")
JohnsonJack = FamilyIndividual("Johnson", "Jack", "03/05/2010")

# Mums family members are initialised with the attributes of FullName, SurName and DOB.
RajKaan = FamilyIndividual("Raj", "Kaan", "04/04/1948")
MaryamKaan = FamilyIndividual("Maryam", "Kaan", "05/03/1949")
KairaBai = FamilyIndividual("Kaira", "Bai", "06/02/1978")
FatimaJack = FamilyIndividual("Fatima", "Jack", "07/03/1979")
AprilBai = FamilyIndividual("April", "Bai", "08/04/1992")
ArjanBai = FamilyIndividual("Arjan", "Bai", "10/07/2013")

#This for loop prints out the calendar of the unsorted birthday dates and adds the members into the family tree and calendar.
for member in [WilliamJack, LucyJack, JonothanJack, RichardJack, HenryJack, BillyJack, RobertJack, JohnsonJack, RajKaan, MaryamKaan,KairaBai, FatimaJack, AprilBai, ArjanBai]:
    family_tree.add_member(member)
    calendar.add_member(member)
    print(member.FirstName + member.SurName +": "+member.DOB)

#The relationships are set.
WilliamJack.add_child(JonothanJack)
WilliamJack.add_child(RichardJack)
LucyJack.add_child(JonothanJack)
LucyJack.add_child(RichardJack)
RichardJack.add_child(HenryJack)
JonothanJack.add_child(RobertJack)
RobertJack.add_child(JohnsonJack)
HenryJack.add_child(BillyJack)

RajKaan.add_child(FatimaJack)
RajKaan.add_child(KairaBai)
MaryamKaan.add_child(FatimaJack)
MaryamKaan.add_child(KairaBai)
FatimaJack.add_child(HenryJack)
KairaBai.add_child(AprilBai)
AprilBai.add_child(ArjanBai)

JonothanJack.add_sibling(RichardJack)
FatimaJack.add_sibling(KairaBai)

HenryJack.add_cousin(AprilBai)
HenryJack.add_cousin(RobertJack)
AprilBai.add_cousin(HenryJack)
RobertJack.add_cousin(HenryJack)
BillyJack.add_cousin(ArjanBai)
BillyJack.add_cousin(JohnsonJack)
ArjanBai.add_cousin(BillyJack)

family_tree.start(calendar) #FamilyTree class is initialised with the attribute calendar of the BirthdayCalendar class passed as the parameter.
