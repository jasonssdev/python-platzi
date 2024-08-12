# String

user_name = "Jason"
user_lastname = "Dev"
user_nickname = "JSNDEV"
user_email = "jasonssdev@gmail.com     "
print(type(user_name))

print(user_name[0:6:2])
print(user_name[-1:])

print(user_name + user_lastname)
print(user_name * 5)

print(len(user_lastname))
print(len(user_name))

print(user_nickname.lower())
print(user_name.upper())
print(user_email.strip())

# Integer
user_age = 34
print(type(user_age))

#Float
user_weight = 83.5
print(type(user_weight))
user_heigh = 176.5
print(user_heigh)
print(user_heigh + user_weight)

#Boolean

is_true = True
is_false = False
print(is_true)
print(type(is_false))

print(f"Hi, I am {user_name} {user_lastname}, I am {user_age}, my weight is {user_weight} kg")



