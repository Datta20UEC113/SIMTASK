#collecting email from user
Email = input("Provide your email here :-")


#slice and store the user information
user_name = Email[:Email.index('@')]


#slice and store the domain information
domain_name = Email[Email.index('@') + 1 :]


#print user information and domain information
print(user_name)
print(domain_name)