class Sigma:
    def __init__(self):
        self.commands = {
            ("q0","0"): ("q1","B","P"),
            ("q0", "1"): ("q5","B","P"),
            ("q0", "B"): "end",
            ("q1", "0"): ("q1","0","P"),
            ("q1", "1"): ("q2","1","P"),
            ("q1", "B"): "end",
            ("q2", "0"): ("q3","1","L"),
            ("q2", "1"): ("q2","1","P"),
            ("q2", "B"): ("q4","B","L"),
            ("q3", "0"): ("q3","0","L"),
            ("q3", "1"): ("q3","1","L"),
            ("q3", "B"): ("q0","B","P"),
            ("q4", "0"): ("q4","0","L"),
            ("q4", "1"): ("q4","B","L"),
            ("q4", "B"): ("q6","0","P"),
            ("q5", "0"): ("q5","B","P"),
            ("q5", "1"): ("q5","B","P"),
            ("q5", "B"): ("q6","B","P"),
            ("q6", "0"): "end",
            ("q6", "1"): "end",
            ("q6", "B"): "end",
        }
def input_checker(mode):
    """Przyjmuje string n lub string m, jako zmienną mode"""
    if mode == "m":
        answer=input("m = ")
        try:
            answer=int(answer)
            return answer
        except:
            print("Proszę, podać liczbę całkowitą")
            return input_checker(mode)
    if mode == "n":
        answer=input("n = ")
        try:
            answer=int(answer)
            return answer
        except:
            print("Proszę, podać liczbę całkowitą")
            return input_checker(mode)

def stringify(belt):
    string=""
    for j in belt:
        string+=j
    return string

def first_belt_maker(m,n):
    """Tworzy pierwszą postać taśmy"""
    belt=[]
    for i in range(m):
        belt.append("0")
    belt.append("1")
    for j in range(n):
        belt.append("0")
    return belt

def temporary_belt_maker(belt, state, i, j, p):
    string=stringify(belt)
    if state=="q6" and j==0:
        return string+"<"+state+">"
    if i==0 and j==1:
        return "<"+state+">"+string
    if i==0 and j==len(belt)+p-1:
        return string+"<"+state+">"
    return string[0:i]+"<"+state+">"+string[i:]
