MAX_FINE = 500
FINE_PER_DAY = 5

days = int(input("enter late days : "))
fine = (days * FINE_PER_DAY)
if (fine>MAX_FINE):
    fine = MAX_FINE

print("your fine :" ,fine )