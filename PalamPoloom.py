import random 

k = 5

while True : 
    
        print("\nā ==== R")
        print("š¤ ==== P")


        user = input("\nEnter a Choice : 1-R 2-P\n ")
        rand = ["P","R"]

        computer1 = random.choice(rand)
        computer2 = random.choice(rand)

        if computer1 == computer2 == "P" :
            if user == "P" :
                print("\nThey are Same")
            else :
                print("\nUser Win")   
                
        elif  computer1 == computer2 == "R" :
            if user == "R" :
                    print("\nThey are Same")
            else :
                print("\nUser Win")    
                
        elif computer1 == user == "P" :
            if computer2 == "P" :
                    print("\nThey are Same")
            else :
                print("\nComputer2 Win")    
                    
        elif computer1 == user == "R" :
            if computer2 == "R" :
                    print("\nThey are Same")
            else :
                print("\nComputer2 Win")                

        elif computer2 == user == "P" :
            if computer1 == "P" :
                    print("\nThey are Same")
            else :
                print("\nComputer1 Win") 

        elif computer2 == user == "R" :
            if computer1 == "R" :
                    print("\nThey are Same")
            else :
                print("\nComputer1 Win")       
        k -=1
        
        if k == 0 :
            print("\nEnd Of The Game")
            break                                


# while True :
     
#         print("\nā ==== R")
#         print("š¤ ==== P")


#         user = input("\nEnter a Choice : 1-R 2-P\n ")
#         rand = ["š¤","ā"]

#         computer1 = random.choice(rand)
#         computer2 = random.choice(rand)

#         if computer1 == computer2 == "š¤" :
#             if user == "š¤" :
#                 print("\nThey are Same")
#             else :
#                 print("\nUser Win")   
                
#         elif  computer1 == computer2 == "ā" :
#             if user == "ā" :
#                     print("\nThey are Same")
#             else :
#                 print("\nUser Win")    
                
#         elif computer1 == user == "š¤" :
#             if computer2 == "š¤" :
#                     print("\nThey are Same")
#             else :
#                 print("\nComputer2 Win")    
                    
#         elif computer1 == user == "ā" :
#             if computer2 == "ā" :
#                     print("\nThey are Same")
#             else :
#                 print("\nComputer2 Win")                

#         elif computer2 == user == "š¤" :
#             if computer1 == "š¤" :
#                     print("\nThey are Same")
#             else :
#                 print("\nComputer1 Win") 

#         elif computer2 == user == "ā" :
#             if computer1 == "ā" :
#                     print("\nThey are Same")
#             else :
#                 print("\nComputer1 Win")       
#         k -=1
        
#         if k == 0 :
#             print("\nEnd Of The Game")
#             break                                
    
    
    
    
 