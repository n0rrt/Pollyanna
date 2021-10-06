import random

class Person:
    def __init__(self, name, sibs, match = None):
        self.name = name
        self.sibs = sibs
        self.match = match

sean = Person("Sean", ["Sean", "Mary", "Neve"])
mary = Person("Mary", ["Sean", "Mary", "Neve"])
neve = Person("Neve", ["Sean", "Mary", "Neve"])
brendan = Person("Brendan", ["Brendan", "Kieran", "Bridget", "Aidan"])
kieran = Person("Kieran", ["Brendan", "Kieran", "Bridget", "Aidan"])
bridget = Person("Bridget", ["Brendan", "Kieran", "Bridget", "Aidan"])
aidan = Person("Aidan", ["Brendan", "Kieran", "Bridget", "Aidan"])
tim = Person("Tim", ["Tim", "Claire", "Molly"])
claire = Person("Claire", ["Tim", "Claire", "Molly"])
molly = Person("Molly", ["Tim", "Claire", "Molly"])
kate = Person("Kate", ["Kate", "Nora"])
nora = Person("Nora", ["Kate", "Nora"])

brian = Person("Brian", ["Brian"])
lori = Person("Lori", ["Lori", "Leo"])
leo = Person("Leo", ["Lori", "Leo"])
mike = Person("Mike", ["Mike", "Linda"])
linda = Person("Linda", ["Mike", "Linda"])
tom = Person("Tom", ["Tom", "Karen"])
karen = Person("Karen", ["Tom", "Karen"])

kids = [sean, mary, neve, brendan, kieran, bridget, aidan, tim, claire, molly, kate, nora]
adults = [brian, lori, leo, mike, linda, tom, karen]

def gen_matches(arr):
    match_arr = []
    for person in arr:
        found = False
        while found == False:
            match_num = random.randrange(len(arr))
            if match_num not in match_arr and arr[match_num].name not in person.sibs:
                match_arr.append(match_num)
                person.match = arr[match_num].name
                found = True
        print(person.name + " : " + person.match)
    
gen_matches(kids)
gen_matches(adults)