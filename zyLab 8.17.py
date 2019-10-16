
hold_results = {

}


for player in range (1,6): #means 1-5. 
    jers_num= int(input("Enter player " + str(player) + "'s " + "jersey number: "))   #concatenate to join idea was borrowed from friend because I could not figure it out.
    print()
    player_rat= int(input("Enter player " + str(player) + "'s " + "rating: "))
    print()
    hold_results[jers_num]= player_rat    #stores in dictionary
print('''
ROSTER''')
for key in sorted(hold_results):
        print ("Jersey number:", str(key)+"," " Rating:", hold_results[key]) #since it was stored we must print using a loop as seen in zyLAB 5.16
        print()



def add_player(hold_results):
    jers_num=int(input("Enter a new player's jersey number: "))  #Since using functions all we have to do is ask for input from user and re-store it exactly how we did above
    player_rat=int(input("Enter the player's rating: "))
    hold_results[jers_num]=player_rat



def output_roster(hold_results):
    print("ROSTER")
    print()
    for key in sorted(hold_results):                #we sort everything then print so it is in order if we don't use "sorted" it does not print in order
        print ("Jersey number:", str(key)+"," " Rating:", hold_results[key])
        print()



def del_player(hold_results):
    jers_num_del = int(input("Enter a jersey number: "))  #prompt user for jersey number
    del hold_results[jers_num_del]           #simply delete using del and access list using the name of our dictionary and the number the user entered 



def update_pl(hold_results):
    jers_num2=int(input("Enter a jersey number: "))       #prompt user for jersey number and new player rating
    update_player_rat= int(input("Enter a new rating for player: "))
    hold_results[jers_num2]=update_player_rat     #simply update the player rating by accessing the list and making it equal to the new player rating just entered.


    
def output_above(hold_results):      
    above_rat=int(input("Enter a rating: "))   #prompt user for a rating 
    print ("ABOVE", above_rat)  
    print()
    new = sorted(hold_results)  #sort 
    for i in new:
        if hold_results[i] > above_rat:  #this accesses and will only output players on the roster above the rating the user entered and keeps looping until none are left
            print ("Jersey number:", str(i)+"," " Rating:", hold_results[i])   
            print()



def main():
    while True:
        menu = input('''MENU
a - Add player
d - Remove player
u - Update player rating
r - Output players above a rating
o - Output roster
q - Quit

Choose an option:
''')
        if menu=="q":          #calling of functions occur here
            break
        if menu=="a":
            add_player(hold_results)
        if menu=="o":
            output_roster(hold_results)
        if menu=="d":
            del_player(hold_results)
        if menu=="u":
            update_pl(hold_results)
        if menu=="r":
            output_above(hold_results)



if __name__ == '__main__':   #calls main function
    main()
