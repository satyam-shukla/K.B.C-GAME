print("\tWEL-COME TO K.B.C (KON BANEGA COROREPATI)")



question_list = [
    "1. How many continents are there?",              # pehla question
    "2. What is the capital of India?",            # doosra question
    "3. NG mei kaun se course padhaya jaata hai?",    # teesra question
    "4. 1. sampat pal devi ne bundelkhand me mahilao k khilaf hone wali hinsa ko rokane k liye kis dal ki sthapna ki thi?",
    "5. inme se kis bimari ko  dimagi bukhar k  name se jana jata he ?",
    "6. candy crus saga , tempal run or farut ninza kiske prkar he ? ",
    "7. film 'hiropanti' me bator nayak kadam rakhne wale tiger kis abhineta k bete he?",
    "8. india me konsa pad ek nirvachit pad he?",
    "9. inme se kon ramayan k mukhya patro me se ek he jo mahabharat me bhi nazar aate he?",
    "10. hamare sor mandal me sabse badi vastu kya he?",
    "flip question :  how many planet in our solar system?"
]
options_list = [
    #pehle question ke liye options
    ["Four", "Nine", "Seven", "Eight"],
    #second question ke liye options
    ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
    #third question ke liye options
    ["Software Engineering", "Counseling", "Tourism", "Agriculture"],
    ["lakshmi bai","nari mukti vahini","mahila morcha","gulabi gang"],
    ["japani insefalitis","tatnas"," dangu","rabiz"],
    ["chat masanger","anty virus", "games", "search enjan"],
    ["sunil shatty","sany deol","anil kapoor","jacy saraf"],
    ["bharat k mukhya nyayadhish","mukhya chunav aayukt","bharat ke rastrapti","rajyapal"],
    ["hanuman","vedvyas","dashrath","duryodhan"],
    ["titan","sun","alfa sentory","jupitar"],
    [2,5,6,8]
]

win_ammount = [10000,50000,100000,500000,1000000,2500000,5000000,10000000,50000000,70000000]
solution_list = [3, 4,1,4,1,3,4,3,1,4,4] 
solution_list2 = ["seven","Delhi","Software Engineering","gulabi gang","japani insefalitis","games","jacy sraf","bharat ke rastrapati","hanuman","jupitar","four"]

life=['11 for 5050','12 for flip the question.',"13 for expert advice.","14 for phone a friend"]
life1=[11,12,13,14]
q=0
while q<len(question_list)-1:
    print(question_list[q])
    c=1
    for i  in options_list[q]:
        print('  ',c,'. ',i)
        c+=1
    print()
    if len(life)==0:
        print("you dont have any life line")
    else:
        print('   5. for life line')
    print('   6. for quiting the game.')
    print()
    print('choose your answer --')

    user=int(input('enter your choose'))

    if  user > 0 and user < 5:
        if user==solution_list[q]:
            print('congratulation you give right asnswer and win ',win_ammount[q])
        else:
            print("you give wrong answer")
            if q==0:
                print('you win nothing')
            else:
                print('you win',win_ammount[q])
            break

    elif user==5:
        print(life)
        slife=int(input('enter your life line :  '))
        if slife in life1:
            z=life1.index(slife)
            life.pop(z)
            life1.remove(slife)
            if slife==11:
                print("1.",solution_list2[q],"or","2.",options_list[q][1])
                w=int(input("enter your correct option"))
                if w==1:
                    print("congrats you win",win_ammount[q])
                else:
                    if q==0:
                        print("you win nothing")
                        
                    else:
                        print("you loose the game","\n","and you win",win_ammount[q])
                    break
            elif slife==12:
                print(question_list[10])
                v=1
                for i  in options_list[10]:
                    print('  ',v,'. ',i)
                    v+=1
                w=int(input("enter your correct option"))
                if w==4:
                    print("congrats you win",win_ammount[q])
                else:
                    if q==0:
                        print("you win nothing")
                        
                    else:
                        print("you loose the game","\n","and you win",win_ammount[q])
                    break
            elif slife==13:
                print('option ',solution_list[q],'is advice by expert')
                w=int(input("enter your correct option"))
                if w==solution_list[q]:
                    print("congrats you win",win_ammount[q])
                else:
                    if q==0:
                        print("you win nothing")
                        
                    else:
                        print("you loose the game","\n","and you win",win_ammount[q])
                    break
            elif slife==14:
                print('option ',solution_list[q],'is advice by friend')
                print('option ',solution_list[q+1],'is advice by friend')

                w=int(input("enter your correct option"))
                if w==solution_list[q]:
                    print("congrats you win",win_ammount[q])
                else:
                    if q==0:
                        print("you win nothing")
        else:
            print('you have no life liffe line')

          
    elif user==6:
        print("thankuu riyaz for playing")
        if q==0:
            print("you win nothing")
            
        else:
            print("you loose the game","\n","and you win",win_ammount[q])
        break
                
        
    q+=1