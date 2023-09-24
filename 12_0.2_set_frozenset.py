class ContactList:
    def __init__(self,name):
        self.name = name

    def __hash__(self):
        print("self.name",self.name,"hash key",hash(frozenset(self.name)))
        return hash(frozenset(self.name))
    
    def __eq__(self,other):
        print("self.name",self.name,"other.name",other.name)

        return set(self.name) == set(other.name)
    
def merge_contact_lists(contacts):
    return list(set(contacts))


contact_list1 = [ContactList("John"), ContactList("Mary"), ContactList("John")]
contact_list2 = [ContactList("Mary"), ContactList("Jane"), ContactList("Jane")]


merged_contacts = merge_contact_lists(contact_list1 + contact_list2)

for contact in merged_contacts:
    print(contact.name)    
    
