#andrew kellmer 9/21/18
#change sorter



def change():

    #ask how much change they have

    total_change = int (input ("how much change do you have in your pocket"))

    #calculate the change

    q = total_change // 25
    whats_left = total_change % 25
    d = whats_left // 10
    whats_left = whats_left % 10
    n = whats_left // 5
    whats_left = whats_left % 5
    p = whats_left

    #display it back

    print("Quarters: ", q, "/nDimes: ", d, "/nNickels: ", n, "/nPennies: ", p)

#change()

def change2(total_change):

    #ask how much change they have

    total_change = total_change

    #calculate the change

    dol = total_change // 100
    whats_left = total_change % 100
    q = whats_left // 25
    whats_left = whats_left % 25
    d = whats_left // 10
    whats_left = whats_left % 10
    n = whats_left // 5
    whats_left = whats_left % 5
    p = whats_left

    return dol, q, d, n, p    


total_change = int (input ("how many cents do you have in your pocket"))

dol, q, d, n, p = change2(total_change)

#display it back

print("Dollars:", dol, "Quarters:", q, "Dimes:", d, "Nickels:", n, "Pennies:", p)
