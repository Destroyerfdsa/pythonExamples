## Nicholaus Whites
# 9/21/2018
# Change Sorter



def change():
    # Input for how much change
    total_change = int(input("How much change do you have on you: "))
    # calculate for q n d p
    q = total_change // 25
    whats_left = total_change % 25 #-(q*25)
    d = whats_left // 10
    whats_left = whats_left % 10
    n = whats_left // 5
    whats_left = whats_left % 5
    p = whats_left
    # display
    print("Quarters:",q,"\nDimes:   ",d,"\nNickels: ",n,"\nPennies: ",p)

###change()


def change2(total_change ):
    # Input for how much change
    total_change = total_change
    # calculate for q n d p
    dol = total_change // 100
    whats_left = total_change % 100
    q = whats_left // 25
    whats_left = whats_left % 25
    d = whats_left // 10
    whats_left = whats_left % 10
    n = whats_left // 5
    whats_left = whats_left % 5
    p = whats_left
    return dol,q,d,n,p


total_change = int(input("How much change in your pocket: "))
dol,q,d,n,p =change2(total_change)

# display
print("$: ",dol,"\nQuarters: ",q,"\nDimes: ",d,"\nNickels: ",n,"\nPennies:",p)
