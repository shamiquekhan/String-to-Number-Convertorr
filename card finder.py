# def locate_card(cards,query) :
#     position=0
#     print ("cards:",cards)
#     print("query:",query)
#     while position < len(cards) :
#         # print ("position:",position)
#         if cards[position]==query:
#             return position
#         position+=1 # elif position==len(cards): 
#     return -1

# # cards6=tests[6]["input"]["cards"]
# # query6=tests[6]["input"]["query"]
# # locate_card(cards6,query6)
def find_card_position(cards,target):
    sorted_cards=sorted(cards,reverse=True)
    try:
        postion=sorted_cards.index(target) + 1
        return postion
    except ValueError:
        return -1
if __name__ == "__main__":
    n=int(input("Enter the number of cards :"))
    cards=[]
    for _ in range(n):
        card=input("Enter the card : ")
        cards.append(card)
    print("Cards in desing order are :",cards)
    target=input("Enter the card to find : ")
    position=find_card_position(cards, target)
    if position != -1:
        print(f"the position of the card is :", position)
    else :
        print(f"The card {target} is not in the list")
