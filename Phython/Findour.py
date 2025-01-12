
# the point is to tyry and vreak down the basic components and to user as many as possible to make somethinh that makes sence at the end
#pyhton has loose decclarations 
#the functiopns are clear thou so make sure you know how to use them 
#********************************************************

# first will be playing with [arrays] its called a list and like most lista thee are plexile 
# will it alet me declear an epmty array and the fill it ? yes

Number=[]
letters= []


# *append* adds to the arrey *insert* adds it a certain index point
#Number.append(input("Input a number:"), input("Another num:")) *this dosent work * 

#//Number.append(input("Input a number:"))
#//Number.append(input("Input a number:"))


# use loop cause waw
# while is used to perform action under confition like this 
#//while  len(Number) < 10 :
   #// Number.append(input("Input a number:"))

#use for to incrimental functions like this 
# becuse of the incrimental natrure of the for loop its maily used to increment output rather then input 
#//for x in Number:
   #// print(x)


#sortin list
while  len(letters) < 10 :
    letters.append(input("Input a Letter:"))

letters.sort()
#revLetters = str(letters.sort(reverse=True))*dosent work*
#revLetters = letters.sort(reverse=True)*dosent work*
#print(x.sort(reversed))*dosent work*


#//for x in letters:
   #//print(x)


#following in a function that isnt working 
#why ?? 
#//def Reverser():
   #// revLetters =[]
    #//for i in letters:
       #// revLetters.append(input(i))
    #//print(revLetters)

#also not working as its not reversing the order 
#why? 
revLetters =[]
def Reverser():
    for i in letters:
       revLetters.append(input(i))
    revLetters.sort(reverse=True)   
    for y in revLetters:
            print(y) 
        
    
Reverser()

#usingf a method to hold functions 


# Tupple wors more like arrays 
#//example= (1,2,3,4)
 
    



