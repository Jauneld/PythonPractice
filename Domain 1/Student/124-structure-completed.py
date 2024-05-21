#dictionary example
#STORE DATA IN KEY VALUE PAIRS
coins = { #INSIDE CURLY BRACKETS
    "gold":100, #key:value
    "silver":50,
    "bronze":25
}
print(coins)

#set example
#A TYPE OF COLLECTION THAT STORES UNIQUE VALUES OF DATA
#No value is repeated
regions = {"north","south","east"}
regions.add("east")#east is not in the list twice because each value is unique
regions.add("west")#west is added because it is a unique value compared to everything
print(regions)

#tuple example
#A LIST WITH IMMUTABLE VALUES MEANS THAT THE VALUES ARE UNCHANGEABLE UNLESS YOU REDECLARE THE VARIABLE
char1_name=("Humphrey",'Cat')
char1_name[1]="Dog"#It will not work
