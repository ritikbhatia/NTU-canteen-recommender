
#Below are the parts of our program and the distribution of who did what:
#Functions in our program:
#search_canteen()                                         ##Implemented by Ritik Bhatia
#search_rank()                                            ##Implemented by Ritik Bhatia
#search_food()                                            ##Implemented by Ritik Bhatia
#search_stall()                                           ##Implemented by Ritik Bhatia
#sort_rating()                                            ##Implemented by Manav Arora
#sort_price()                                             ##Implemented by Manav Arora
#sort_distance()                                          ##Implemented by Manav Arora
#transit()                                                ##Implemented by Manav Arora
#cal_dist()                                               ##Implemented by Manav Arora
#update()(including update location)                      ##Implemented by Ritik Bhatia
#crowd()                                                  ##Implemented by Ritik Bhatia
#favourites()(includes add/delete and print favourites)   ##Implemented by Ritik Bhatia

#database                                                 ##Implemented by Manav Arora
#User Interface(display_map() and display_map_ref())      ##Implemented by Ritik Bhatia

#importing all the required modules and packages
from database import *
import pygame
import math
import operator
from time import sleep
import datetime
import sys
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


#function to display the map
def display_map(arg,x,y):
        #load the required image
        introScreenImage = pygame.image.load("NTUMap.jpg")
        screen = pygame.display.set_mode((700,700))
        introScreenImage = pygame.transform.scale(introScreenImage, (700,700))
        #blit imgage onto the screen
        screen.blit(introScreenImage,(0,0))
        #if the argument to put marker is set, then put marker
        if arg == 1:
            marker = pygame.image.load("marker.png")
            marker = pygame.transform.scale(marker, (25,25))
            #adjustments fro positioning of marker
            screen.blit(marker, (x - 15,y - 15))
        pygame.display.flip()

#function to search for the canteen and display all its details
def search_canteen(pos):
    print("Canteen 1")
    print("Canteen 2")
    print("Canteen 9")
    print("Canteen 11")
    print("Canteen 13")
    print("Canteen 14")
    print("Canteen 16")
    print("North Hill Food Court")
    print("Tamarind Food Court")
    print("Pioneer Food Court")
    print("Quad Cafe")
    print("North Spine Plaza")
    print("Koufu")
    print()
    search = input("Enter the canteen you want to search about(as mentioned above): ")
    print()
    if search not in coordinates:
        print("Canteen not found! Please enter data according to format specified!")
    else:
        #display information
        print("The following data is retrieved for your search:")
        print()
        print("You are at location   =  ",pos)
        print("Canteen coordinates   = ", coordinates[search])
        print("Canteen rating        = ", rating[search])
        print("Canteen stalls        = ",end = '')
        #to print in an aesthetic format
        for stall in stalls[search]:
                if not stall == stalls[search][len(stalls[search]) - 1]:
                        print(stall,",",end = " ")
                else:
                        print(stall)
        print("Canteen average price =  $",end = "")
        print(pricing[search])
        print("Canteen food type     = ", end = '')
        for food in foodtype[search]:
                if not food == foodtype[search][len(foodtype[search]) - 1]:
                        print(food,',',end = " ")
                else:
                        print(food)
        #display image of the canteen input, using matplotlib
        if search == 'Canteen 1':
                img = mpimg.imread('canteen1.jpg')
                imgplot = plt.imshow(img)
                plt.show()
        elif search == 'Canteen 2':
                img = mpimg.imread('canteen2.png')
                imgplot = plt.imshow(img)
                plt.show()
        elif search == 'Canteen 9':
                img = mpimg.imread('canteen9.png')
                imgplot = plt.imshow(img)
                plt.show()
        elif search == 'Canteen 11':
                img = mpimg.imread('canteen11.png')
                imgplot = plt.imshow(img)
                plt.show()
        elif search == 'Canteen 13':
                img = mpimg.imread('canteen13.png')
                imgplot = plt.imshow(img)
                plt.show()
        elif search == 'Canteen 14':
                img = mpimg.imread('canteen14.png')
                imgplot = plt.imshow(img)
                plt.show()
        elif search == 'Canteen 16':
                img = mpimg.imread('canteen16.png')
                imgplot = plt.imshow(img)
                plt.show()
        elif search == 'North Hill Food Court':
                img = mpimg.imread('northhill.jpg')
                imgplot = plt.imshow(img)
                plt.show()
        elif search == 'Tamarind Food Court':
                img = mpimg.imread('tamarind.jpg')
                imgplot = plt.imshow(img)
                plt.show()
        elif search == 'Pioneer Food Court':
                img = mpimg.imread('pioneer.png')
                imgplot = plt.imshow(img)
                plt.show()
        elif search == 'Quad Cafe':
                img = mpimg.imread('quad.jpg')
                imgplot = plt.imshow(img)
                plt.show()
        elif search == 'North Spine Plaza':
                img = mpimg.imread('northspine.png')
                imgplot = plt.imshow(img)
                plt.show()
        elif search == 'Koufu':
                img = mpimg.imread('southspine.png')
                imgplot = plt.imshow(img)
                plt.show()
        print()
    return

#search canteens based on rating
def search_rank():
    rating_user = 0.0
    try:
        rating_user = (float)(input("Enter rating(to display canteens above that rating, max rating being 5): "))
        print()
        count = 0
        for canteen, review in rating.items():
            #display only those canteens whose rating is higher than the input rating
            if review > rating_user:
                print(canteen,": rating = ",review)
                count = 1
        if count == 0:
            print("No canteens above this rating!")
            print()
    except ValueError:
        print("Invalid data type!")
    print()
    return

#search canteens depending on the food-type available
def search_food():
    print("1. Vegetarian")
    print("2. Non-vegetarian: non-halal")
    print("3. Non-vegetarian: halal")
    print()
    try:
        opt = (int)(input("Enter option number of food you want: "))
        print()
        if opt == 1:
            print("You have the following options: ")
            for key in foodtype:
                    if 'vegetarian' in foodtype[key]:
                            print(key)
            print()
        elif opt == 2:
            print("You have the following options: ")
            for key in foodtype:
                    if 'non-vegetarian:non-halal' in foodtype[key]:
                            print(key)
            print()
        elif opt == 3:
            print("You have the following options")
            for key in foodtype:
                    if 'non-vegetarian:halal' in foodtype[key]:
                            print(key)
            print()
        else:
            print("Invalid option number! ")
    except ValueError:
        print("Invalid input!")

#search canteens hav9ing the chosen satll
def search_stall():
    try:
      while True:
        #display options
        print("1.  Waffles")
        print("2.  Canopy Coffee Club")
        print("3.  Indian")
        print("4.  Malaysian")
        print("5.  Japanese")
        print("6.  Yong Tau Foo")
        print("7.  Ayam Penyet")
        print("8.  Chinese")
        print("9.  Ramen Shop")
        print("10. Korean Cuisine")
        print("11. Economical Rice")
        print("12. Fruits and Juices")
        print("13. Jiu Li Xiang")
        print("14. Xia Long Bao")
        print("15. Noodle Bar")
        print("16. Western Food")
        print("17. Vegetarian Stall")
        print("18. Mini Wok")
        print("19. Chicken Rice")
        print("20. Pasta Express")
        print("21. Coffee Bean")
        print("22. Thai")
        print("23. Desserts")
        print("24. Back to menu")
        print()
        option = (int)(input("Enter option number of stall you want to search: "))
        print()
        #check in which canteens is input stall present and print those
        if option == 1:
                print("You have the following options: ")
                for key in stalls:
                        if 'Waffles' in stalls[key]:
                                print(key)
        elif option == 2:
                print("You have the following options: ")
                for key in stalls:
                        if 'Canopy Coffee Club' in stalls[key]:
                                print(key)
        elif option == 3:
                print("You have the following options: ")
                for key in stalls:
                        if 'Indian' in stalls[key]:
                                print(key)
        elif option == 4:
                print("You have the following options: ")
                for key in stalls:
                        if 'Malaysian' in stalls[key]:
                                print(key)
        elif option == 5:
                print("You have the following options: ")
                for key in stalls:
                        if 'Japanese' in stalls[key]:
                                print(key)
        elif option == 6:
                print("You have the following options: ")
                for key in stalls:
                        if 'Yong Tau Foo' in stalls[key]:
                                print(key)
        elif option == 7:
                print("You have the following options: ")
                for key in stalls:
                        if 'Ayam Penyet' in stalls[key]:
                                print(key)
        elif option == 8:
                print("You have the following options: ")
                for key in stalls:
                        if 'Chinese' in stalls[key]:
                                print(key)
        elif option == 9:
                print("You have the following options: ")
                for key in stalls:
                        if 'Ramen Shop' in stalls[key]:
                                print(key)
        elif option == 10:
                print("You have the following options: ")
                for key in stalls:
                        if 'Korean Cuisine' in stalls[key]:
                                print(key)
        elif option == 11:
                print("You have the following options: ")
                for key in stalls:
                        if 'Economical Rice' in stalls[key]:
                                print(key)
        elif option == 12:
                print("You have the following options: ")
                for key in stalls:
                        if 'Fruits and Juices' in stalls[key]:
                                print(key)
        elif option == 13:
                print("You have the following options: ")
                for key in stalls:
                        if 'Jiu Li Xiang' in stalls[key]:
                                print(key)
        elif option == 14:
                print("You have the following options: ")
                for key in stalls:
                        if 'Xia Long Bao' in stalls[key]:
                                print(key)
        elif option == 15:
                print("You have the following options: ")
                for key in stalls:
                        if 'Noodle Bar' in stalls[key]:
                                print(key)
        elif option == 16:
                print("You have the following options: ")
                for key in stalls:
                        if 'Western Food' in stalls[key]:
                                print(key)
        elif option == 17:
                print("You have the following options: ")
                for key in stalls:
                        if 'Vegetarian Stall' in stalls[key]:
                                print(key)
        elif option == 18:
                print("You have the following options: ")
                for key in stalls:
                        if 'Mini Wok' in stalls[key]:
                                print(key)
        elif option == 19:
                print("You have the following options: ")
                for key in stalls:
                        if 'Chicken Rice' in stalls[key]:
                                print(key)
        elif option == 20:
                print("You have the following options: ")
                for key in stalls:
                        if 'Pasta Express' in stalls[key]:
                                print(key)
        elif option == 21:
                print("You have the following options: ")
                for key in stalls:
                        if 'Coffee Bean' in stalls[key]:
                                print(key)
        elif option == 22:
                print("You have the following options: ")
                for key in stalls:
                        if 'Thai' in stalls[key]:
                                print(key)
        elif option == 23:
                print("You have the following options: ")
                for key in stalls:
                        if 'Desserts' in stalls[key]:
                                print(key)
        #back to menu
        elif option == 24:
                return
        else:
                print("Invalid option number!")
        print()
    except ValueError:
            print("Invalid input!")

#calculate distance from the canteens, the straight line distance
def cal_dist(x,y):
    distance = []
    keys = []
    for key in coordinates:
        a=coordinates[key][0]
        b=coordinates[key][1] 
        sq1= abs(a*a - x*x)
        sq2= abs(b*b - y*y)
        result = sq1 + sq2
        #using pythagoras' formula for straight distance 
        z= round(math.sqrt(result),2)
        distance.append(z)
        keys.append(key)
    return distance,keys
    print()

#sorting canteens according to rating
def sort_rating():
    sorted_rating = sorted(rating.items(), key = operator.itemgetter(1))
    for item in sorted_rating:
        print(item[0], ":", item[1])

#sorting canteens according to price
def sort_price():
    sorted_price = sorted(pricing.items(), key = operator.itemgetter(1))
    for item in sorted_price:
        print(item[0], ": $",end ="")
        print(item[1])

#sorting canteens based on distance from canteens
def sort_distance(x,y):
    dist,key = cal_dist(x,y)
    distances = {}
    i = 0
    for i in range(len(dist)):
        distances[key[i]] = dist[i]
    sorted_distance = sorted(distances.items(), key = operator.itemgetter(1))
    for item in sorted_distance:
        print(item[0], ":", item[1],"units")

#function to enable user to update price or rating based on his/her own opinion
def update():
    while True:
        print("1. Update price")
        print("2. Update rating")
        print("3. Back to menu")
        print()
        option = 0
        try:
            option = (int)(input("Enter option number: "))
            print()
        except ValueError:
            print("Invalid input!")
        if option == 1:
           for key in pricing:
               print(key)
           print()
           option_canteen = 0
           try:
               option_canteen = input("Enter canteen name(as mentioned above): ")
           except ValueError:
                print("Inavlid input!")
           print()
           for key in pricing:
               u_price = 0
               if (option_canteen == key):
                   try:
                       #update average price in canteen(just updating the value in the dictionary)
                       u_price = (float)(input("Enter updated price: "))
                       print()
                       pricing[key] = u_price
                       print("Your values have been successfully updated!")
                       print()
                   except ValueError:
                       print("Invalid input!")
        elif option == 2:
           for key in rating:
               print(key)
           print()
           option_canteen = 0
           try:
               option_canteen = input("Enter canteen name(as mentioned above): ")
               print()
           except ValueError:
                print("Inavlid input!")
           print()
           for key in rating:
               u_rate = 0
               if (option_canteen == key):
                   try:
                       #update rating(by just updating the value in the dictionary)
                       u_rate = (float)(input("Enter updated rating: "))
                       print()
                       rating[key] = u_rate
                       print("Your values have been successfully updated!")
                       print()
                   except ValueError:
                       print("Invalid input!")

        elif option == 3:
            break
        else:
            print("Invalid option!")
            continue

#function to recommend transport system to destination from nearest bus stop
def transit(x,y):
    #list of canteens to search from
    print("Canteen 1")
    print("Canteen 2")
    print("Canteen 9")
    print("Canteen 11")
    print("Canteen 13")
    print("Canteen 14")
    print("Canteen 16")
    print("North Hill Food Court")
    print("Tamarind Food Court")
    print("Pioneer Food Court")
    print("Quad Cafe")
    print("North Spine Plaza")
    print("Koufu")
    print()

    search = input("Enter the canteen you want to go to: ")
    print()

    if search not in coordinates:
        print("Canteen not found! Please enter data according to the specified format!")
    else:
     print("You may use the following data for easy commute:")
     print()
     #calculating nearest bus stop to current destination
     temp1={}
     for key in red_bus: 
                a=red_bus[key][0]
                b=red_bus[key][1]
                c=coordinates[search][0]
                d=coordinates[search][1]
                sq1= abs(a*a - c*c)
                sq2= abs(b*b - d*d)
                z= math.sqrt(sq1+sq2) 
                temp1.update({key:z})
     r=min(temp1, key= lambda k: temp1.get(k))
           
     temp2={}
     for key in blue_bus: 
                a=blue_bus[key][0]
                b=blue_bus[key][1]
                c=coordinates[search][0]
                d=coordinates[search][1]
                sq1= abs(a*a - c*c)
                sq2= abs(b*b - d*d)
                z= math.sqrt(sq1+sq2) 
                temp2.update({key:z})
     s=min(temp2, key= lambda k: temp2.get(k))
     
     curr1=r
     curr2=s
     print('Nearest Campus Red stop to destination: ',curr1)
     print('Nearest Campus Blue stop to destination: ',curr2)                   

     #calculating nearest bus stop to current location
     temp3={}
     for key in red_bus:
                a=red_bus[key][0]
                b=red_bus[key][1] 
                sq1= abs(a*a - x*x)
                sq2= abs(b*b - y*y)
                z= math.sqrt(sq1+sq2) 
                temp3.update({key:z})
     r=min(temp3, key= lambda k: temp3.get(k))
     print('Nearest Campus Red bus stop to your current location: ',r)           

     temp4={}
     for key in blue_bus:
                a=blue_bus[key][0]
                b=blue_bus[key][1] 
                sq1= abs(a*a - x*x)
                sq2= abs(b*b - y*y)
                z= math.sqrt(sq1+sq2) 
                temp4.update({key:z})
     s=min(temp4, key= lambda k: temp4.get(k))
     print('Nearest Campus Blue bus stop to your current location: ',s)

     #calculating number of bus stops between destination and location
     for i in range (0,len(red)):
        if curr1==red[i]:
            q=i
        elif r== red[i]:
            w=i
        else:
            continue
         
     try:
      if 0 <= w <= 12 and 0<q<w:
          v= abs(w-12-q)
      elif 0 <= w <= 12 and q>w:
          v= abs(w-q)-1
      print('Number of bus stops taken by Campus Red: ',v)
      for i in range (0,len(blue)):
          if curr2 == blue[i]:
              f=i
          elif s== blue[i]:
              d=i
          else:
              continue
      if 0 <= f <= 11 and 0<d<f:
          e=abs(f-d)-1
      elif 0 <= f <= 11 and d>f:
          e=abs(d-11-f)
      print('Number of bus stops taken by Campus Blue: ',e)
      print()
     except:
      print("Sorry! Transport could not be retrieved for your current location!")
    return

#helper function to add canteen to list of favourites
def add_favourites():
    try:
        no = (int)(input("Enter number of canteens you want to insert: "))
        print()
        for counter in range(no):
            favourite = input("Enter canteen name to add to favourites: ")
            favourites.append(favourite)
        print("Canteens added successfully!")
        print()
    except ValueError:
        print("Invalid input!")

#helper fucntion to delete canteen from list of favourites
def del_favourites():
    if not favourites:
            print("No favourites to delete!")
            print()
    else:
            print("These are canteens in your favourites: ")
            print()
            for i in range(len(favourites)):
                    print(i+1,end = "")
                    print(".", favourites[i])
            print()
            try:
                    option = (int)(input("Enter the number of the element you want to delete from the list above: "))
                    if 0 < option <= len(favourites):
                            #deleted the specified element from the given index
                            favourites.pop(option - 1)
                            print("Deletion carried out successfully!")
                            print()
                    else:
                            print("Option number does not exist!")
            except ValueError:
                    print("Invalid input! Option number should be an integer from 1 to",len(favourites))

#helper fucntion to print canteens in list of favourites             
def print_favourites():
    if not favourites :
        print("No favourites as of now!")
        print()
    else:
            print("Your favourites are: ")
            print()
            for i in range(len(favourites)):
                print(i+1,end = "")
                print(".", favourites[i])
            print()

#function that has the functionality of adding/deleting/printing list of favourite canteens
def favourite():
    try:
     while True:
        print("1. Add to list of favourites")
        print("2. Delete from list of favourites")
        print("3. Print list of favourites")
        print("4. Back to menu")
        print()
        option = (int)(input("Enter option number: "))
        print()
        if option == 1:
                add_favourites()
        elif option == 2:
                del_favourites()
        elif option == 3:
                print_favourites()
        elif option == 4:
                return
    except ValueError:
            print("Invalid input!")

#display map just for reference of the user, to see the canteens, gauge location etc.
def display_map_ref():
        map_img = pygame.image.load("NTUMap.jpg")
        screen1 = pygame.display.set_mode((700,700))
        map_img = pygame.transform.scale(map_img, (700,700))
        screen1.blit(map_img,(0,0))
        pygame.display.flip()
        pygame.init()
        #pressing on the map exits by using the event of mouse being pressed
        print("Press on the map to exit")
        while True:
                ev = pygame.event.get()
                for event in ev:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                pygame.quit()
                                return 0

#fucntion to suggest crowd in canteens in general
def crowd():
        #to extract current time and based in that, suggest crowd in canteens in general
        t1 = datetime.datetime.now()
        print("Current time is :", t1.hour,end = "")
        print("h :",t1.minute,end = "")
        print("m :",t1.second,end = "")
        print("s")
        if 9 <= t1.hour <= 13 or 6 <= t1.hour <= 8:
                print("Peak hours! Canteens will be generally crowded.")
        elif 0 <= t1.hour <= 6:
                print("Most of the canteens will be closed now!")
        else:
                print("Non-peak hours! Canteens will be generally less crowded.")
        print()

#main fucntion for implementing enitre functionality of the program        
def main():
    arg = 0
    pygame.init()
    display_map(arg,0,0)
    i = 0
    print()
    print("Click on the map to specify your location ")
    while True:
            #keep on tracking events and do the below only if mouse button pressed
            ev = pygame.event.get()
            for event in ev:
              if event.type == pygame.MOUSEBUTTONDOWN:
                #extract mouse location
                pos = pygame.mouse.get_pos()
                (x,y) = pos
                arg = 1
                display_map(arg,x,y)
                sleep(3)
                pygame.quit()
                #display various options available and call relevant functions
                while True:
                    print("_______________________________________________________________________________")
                    print("1.  Search by canteen (includes canteen images)")
                    print("2.  Search by rating")
                    print("3.  Search by food")
                    print("4.  Search by stall")
                    print("5.  Sort canteens by rating")
                    print("6.  Sort canteens by price")
                    print("7.  Sort canteens by distance")
                    print("8.  Update information about canteen")
                    print("9.  Update my location")
                    print("10. Transport options to canteens")
                    print("11. Add, delete or print list of favourite canteens")
                    print("12. Display map for reference")
                    print("13. Expected crowd in canteens in general")
                    print("14. Exit")
                    print()
                    option = 0
                    try:
                        option = (int)(input("Enter option number for the task you want to perform: "))
                        print()
                        if option == 1:
                            search_canteen(pos)
                        elif option == 2:
                            search_rank()
                        elif option == 3:
                            search_food()
                        elif option == 4:
                            search_stall()
                        elif option == 5:
                            sort_rating()
                        elif option == 6:
                            sort_price()
                        elif option == 7:
                            sort_distance(x,y)
                        elif option == 8:
                            update()
                        elif option == 9:
                            main()
                        elif option == 10:
                            transit(x,y)
                        elif option == 11:
                            favourite()
                        elif option == 12:
                            display_map_ref()
                        elif option == 13:
                            crowd()
                        elif option == 14:
                            print("Are you sure you want to exit? (Click on red box for 'Yes' and green box for 'No')")
                            screen = pygame.display.set_mode((400,300))
                            pygame.display.set_caption("Confirm exit (Red for yes, Green for no)")
                            screen.fill((255,255,255))
                            yes_button = pygame.draw.rect(screen,(255,0,0),(50,80,90,50))
                            no_button = pygame.draw.rect(screen,(0,255,0),(250,80,90,50))
                            pygame.display.flip()
                            
                            counter = 1
                            
                            while counter != 0:
                                    #to make a confirmation window, to exit or not, by making use of pygame buttons
                                    for event in pygame.event.get():
                                            if event.type == pygame.MOUSEBUTTONDOWN:
                                                    if pygame.mouse.get_pos()[0] >= 50 and pygame.mouse.get_pos()[1] >= 80:
                                                         if pygame.mouse.get_pos()[0] <= 140 and pygame.mouse.get_pos()[1] <= 130:
                                                                 #if mouse clicked on red, then exit
                                                                 pygame.quit()
                                                                 print("Thank you for giving us a chance to serve you!")
                                                                 sys.exit()
                                                    if pygame.mouse.get_pos()[0] >= 250 and pygame.mouse.get_pos()[1] >= 80:
                                                            if pygame.mouse.get_pos()[0] <= 340 and pygame.mouse.get_pos()[1] <= 130:
                                                                 #if mouse clicked on green then return to menu
                                                                 print("Redirecting back to menu")
                                                                 pygame.quit()
                                                                 counter = 0
                                                                 break
                            
                        else:
                            print("Invalid option!")
                            continue
                    except ValueError:
                        print("Invalid Input!")

#boilerplate to call main()
if __name__ == "__main__":
    main()
