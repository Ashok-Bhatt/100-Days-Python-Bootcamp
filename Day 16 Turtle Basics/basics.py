class Country:
    name = "India"
    status = "Developing"

India = Country()       # ----> Internally considered as Country(India)
print(India)    # Gives Address
print(India.name)
print(India.status)

America = Country()
print(America)
print(America.name)
print(America.status )