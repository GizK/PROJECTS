#class representing individual family members
class FamilyMember:
    def __init__(self, first_name, surname, birth_year, death_year=None, parents=None, siblings=None, spouse=None, children=None):
        self.first_name = first_name
        self.surname = surname
        self.birth_year = birth_year
        self.death_year = death_year
        self.parents = [] #empty list
        self.siblings = []
        self.spouse = None
        self.children = []

    def add_child(self, child):
        self.children.append(child) #add a child to the family members children list
        child.parents.append(self) #add the current member as the parent of the child
        if child not in self.siblings:  # add child to siblings list if not already there
            self.siblings.append(child)

    def add_sibling(self, sibling):
        self.siblings.append(sibling)  #add a sibling to the family members siblings list
        sibling.siblings.append(self) #adds the current member as sibling to the sibling

    def set_spouse(self, spouse):
        self.spouse = spouse  #set the spouse for the family member

#class representing the family tree
class FamilyTree:
    def __init__(self):
        self.members = [] #creates a list to hold all the family members

    #method to add family member to the family tree
    def add_member(self, member):
        self.members.append(member) #Append family member to the list

    #method to find member by theur full name
    def find_member(self, name):
        for member in self.members:
            #if the full name matches the firstname and surname, return that member
            if f"{member.first_name} {member.surname}" == name:
                return member
        return None #returns none if there is no member with that name found

    #method to display parents
    def display_parents(self, name):
        member = self.find_member(name)  #find the member in the family tree
        if member:
            # Collect names of parents
            parents = [f"{parent.first_name} {parent.surname}" for parent in member.parents]
            if parents:
                print(f"{name}'s parents: {', '.join(parents)}")  #print the parents names
            else:
                print(f"{name} has no known parents.")  #if no parents,print this message
        else:
            print(f"{name} is not in the family tree.")  #if member isnt found, print this message

        #method to display the grandchildren of a family member
    def display_grandchildren(self, name):
        member = self.find_member(name)  #find the member in the family tree
        if member:
            grandchildren = []
            #get the children for each child of the member (grandchildren)
            for child in member.children:
                grandchildren.extend(child.children)  #add the children of the members children (grandchildren)
            if grandchildren:
                # Print the names of the grandchildren
                print(f"{name}'s grandchildren: {', '.join(f'{grandchild.first_name} {grandchild.surname}' for grandchild in grandchildren)}")
            else:
                print(f"{name} has no known grandchildren.")
        else:
            print(f"{name} is not in the family tree.")

    #this method is AI generated
    def display_immediate_family(self, name):
        member = self.find_member(name)  #find the member in the family tree
        if member:
            print(f"{name}'s Immediate Family:")
            #display the names of the members parents, siblings, spouse, and children
            print(f"  Parents: {', '.join(f'{parent.first_name} {parent.surname}' for parent in member.parents) if member.parents else 'None'}")
            print(f"  Siblings: {', '.join(f'{sibling.first_name} {sibling.surname}' for sibling in member.siblings) if member.siblings else 'None'}")
            print(f"  Spouse: {f'{member.spouse.first_name} {member.spouse.surname}' if member.spouse else 'None'}")
            print(f"  Children: {', '.join(f'{child.first_name} {child.surname}' for child in member.children) if member.children else 'None'}")
        else:
            print(f"{name} is not in the family tree.")  #if member isnt found, print this message

    #method to display extended family of the member (includes immediate family)
    def display_extended_family(self, name):
        member = self.find_member(name)  #find the member in the family tree
        if member:
            extended_family = set()

            #add immediate family members to the extended family list
            #include parents, siblings, spouse, and children in the extended family
            extended_family.update(member.parents)
            extended_family.update(member.siblings)
            if member.spouse:
                extended_family.add(member.spouse)
            extended_family.update(member.children)

            #add the siblings of each of the members parents (aunts and uncles)
            for parent in member.parents:
                extended_family.update(parent.siblings)
                #add the members parent's children (siblings of the current member)
                extended_family.update(parent.children)

            #remove the immediate family members (parents, siblings, spouse, and children) from extended family
            extended_family.discard(member)  # Remove the member themselves from the extended family
            extended_family.discard(member.spouse)  # Remove the spouse from the extended family
            extended_family.difference_update(set(member.children))  # Remove children
            extended_family.difference_update(set(member.siblings))  # Remove siblings

            #convert the set of extended family to a list of names
            extended_family = [f"{relative.first_name} {relative.surname}" for relative in extended_family]

            if extended_family:
                #print the names of extended family members
                print(f"{name}'s Extended Family (including immediate family): {', '.join(extended_family)}")
            else:
                print(f"{name} has no known extended family.")  #if no extended family, print this message
        else:
            print(f"{name} is not in the family tree.")  #if member isnt found, print this message


family_tree = FamilyTree()

# Define each member
WilliamJack = FamilyMember("William", "Jack", 1950, 2010)
LucyJack = FamilyMember("Lucy", "Jack", 1951)
JonothanJack = FamilyMember("Jonothan", "Jack", 1970)
RichardJack = FamilyMember("Richard", "Jack", 1972)
HenryJack = FamilyMember("Henry", "Jack", 1991)
BillyJack = FamilyMember("Billy", "Jack", 2011)
RobertJack = FamilyMember("Robert", "Jack", 1990)
JohnsonJack = FamilyMember("Johnson", "Jack", 2010)

RajKaan = FamilyMember("Raj", "Kaan", 1948)
MaryamKaan = FamilyMember("Maryam", "Kaan", 1949, 2019)
KairaBai = FamilyMember("Kaira", "Bai", 1978)
FatimaJack = FamilyMember("Fatima", "Jack", 1979)
AprilBai = FamilyMember("April", "Bai", 1992)
ArjanBai = FamilyMember("Arjan", "Bai", 2013)

# Add each member to the family tree
for member in [WilliamJack, LucyJack, JonothanJack, RichardJack, HenryJack, BillyJack, RobertJack, JohnsonJack,
               RajKaan, MaryamKaan, KairaBai, FatimaJack, AprilBai, ArjanBai]:
    family_tree.add_member(member)

# Set child relationships
WilliamJack.add_child(JonothanJack)  # Dad's grandad's kids
WilliamJack.add_child(RichardJack)
LucyJack.add_child(JonothanJack)  # Dad's grandma's kids
LucyJack.add_child(RichardJack)
RichardJack.add_child(HenryJack)  # Dad's kids
JonothanJack.add_child(RobertJack)  # Brother's kid
RobertJack.add_child(JohnsonJack)  # Brother's kid's kid
HenryJack.add_child(BillyJack)  # Dad's kid's kid

RajKaan.add_child(FatimaJack)  # Mum's granddad's kids
RajKaan.add_child(KairaBai)
MaryamKaan.add_child(FatimaJack)  # Mum's grandma's kids
MaryamKaan.add_child(KairaBai)
FatimaJack.add_child(HenryJack)  # Mum's kid
KairaBai.add_child(AprilBai)  # Sister's kid
AprilBai.add_child(ArjanBai)  # Sister's kid's kid

# Set sibling relationships
JonothanJack.add_sibling(RichardJack)
RichardJack.add_sibling(JonothanJack)
FatimaJack.add_sibling(KairaBai)
KairaBai.add_sibling(FatimaJack)


while True:
    print("\nPlease choose one:")
    print("1. Display parents of an individual")
    print("2. Display grandchildren of an individual")
    print("3. Display immediate family of an individual")
    print("4. Display extended family of an individual")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        individual_name = input("Enter the name of the individual (First Name and Last Name) (use capital letters for the first letter of each name): ")
        family_tree.display_parents(individual_name)
    elif choice == "2":
        individual_name = input("Enter the name of the individual (First Name and Last Name) (use capital letters for the first letter of each name): ")
        family_tree.display_grandchildren(individual_name)
    elif choice == "3":
        individual_name = input("Enter the name of the individual (First Name and Last Name) (use capital letters for the first letter of each name): ")
        family_tree.display_immediate_family(individual_name)
    elif choice == "4":
        individual_name = input("Enter the name of the individual (First Name and Last Name) (use capital letters for the first letter of each name): ")
        family_tree.display_extended_family(individual_name)
    elif choice == "5":
        print("Exiting")  # exit the program
        break
    else:
        print("Invalid choice. Please try again.")