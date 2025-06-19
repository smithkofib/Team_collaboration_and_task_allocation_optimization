#1. Find the middle element of the list
#2. if it matches queried number, rrturn the middle position as the answer
#3. If it less than queried number, then search the first half of the list
#5. If it greater than the queried number, then search the second half of hte list
#6 If no more elements remain, return -1


def locate_number(card, query):
    lo, hi = 0, len(card) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        mid_number = card[mid]
        print(f"lo: {lo}, hi: {hi}, mid: {mid}, mid_number: {mid_number}")
        if(mid_number == query):
            return mid
        elif(mid_number > query):
            hi = mid - 1
        elif(mid_number < query):
            lo = mid + 1
        
    return -1

#locate_number([1,2,5,6,7,8,9,11,13,14,18,19,20], 7)
age: int 

def demo_eval():
    
    expression = input("Put your expression")
    result = eval(expression)
    print(result)

demo_eval()