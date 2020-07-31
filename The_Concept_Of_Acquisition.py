"""The concept of acquisition is a concept by me, Through this I want to 
make a clear understanding about multilevel inheritence in object oriented python
Although, it's a clear topic but many of you will find it difficult to learn or 
understand."""

# Company names I used - facebook, WhatsApp, Instagram

class Facebook: # Parent company
    founder = "person1"
    CEO = "person2"
    def __init__(self,name,country):
        '''A constructor for organising 
        names and country for users'''
        self.name = name
        self.country = country

    def about_fb_user(self):
        return(f"facebook user: Username is {self.name} and user country is {self.country}")
    # @constructor_for_whatsapp

# The company have 2 users
user1 = Facebook("Carry","USA")
user2 = Facebook("Harry","India")

# The company acquired a company known as WhatsApp4

class WhatsApp(Facebook):

    def __init__ (self,name,age,phone,user_country):
        self.name = name
        self.age = age
        self.phone = phone
        self.country = user_country # Acquiring Facebook Users
    
    def about_whatsapp_user(self):
        return f"Whatsapp user: Name is {self.name}, age is {self.age} and phone number is {self.phone}"

    # def __init__(self,user_contacts):
    #     self.user_contacts = user_contacts

    # def about_contacts(self):
    #     return f"Contacts are {self.user_contacts}"

user1 = WhatsApp("Carry",25,2563,"Canada")
# user2 = about_contacts(2645)
# print(user2)
# user2 = WhatsApp("Harry",26,9006)

print(user1.about_whatsapp_user())
print(user1.about_fb_user())
# print(user1.about_whatsapp_user())
# print(user1.about_instagram_user())

class Instagram(WhatsApp):

    def __init__(self,name):
        self.name = name
        # self.photo = photo

    def about_instagram_user(self):
        return f"Instagram user: Name is {self.name}"

user1 = Instagram("Carry")

# print(user1.about_whatsapp_user())
# print(user1.about_fb_user())
print(user1.about_instagram_user())