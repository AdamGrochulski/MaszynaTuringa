from func_library import *
fS=Sigma()

def main():
    print("\n>>>>>>>>>>>>>>>>>>>> Maszyna Turinga <<<<<<<<<<<<<<<<<<<<")
    print("M = (Q,\u03a3, \u0393, \u03B4, q0, B, F), gdzie:")
    print("Q = { q0, q1, q2, q3, q4, q5, q6 } -> zbiór stanów")
    print("\u03a3 = { 0, 1 } -> zbiór symboli wejściowych")
    print("\u0393 = { 0, 1, B } -> zbiór symboli taśmowych")
    print("\u03B4 -> funkcja następnego ruchu")
    print("q0 -> symbol początkowy")
    print("B -> symbol pusty")
    print("F = 0 -> zbiór stanów końcowych\n")
    print("Maszyna oblicza różnicę właściwą dla")
    print("liczb całkowitych na podstawie wzoru:")
    print("m - n dla m >= n")
    print("0 dla m < n\n")
    print("Proszę podać liczby:")
    m=input_checker("m")
    n=input_checker("n")

    belt=first_belt_maker(m,n)

    print("")
    print("Taśma:" + stringify(belt))
    print("Opisy chwilowe MT:")
    print(len(belt))
    state="q0"
    i = 0
    j= 1
    p=0
    first_ever=temporary_belt_maker(belt,state,i, j,p)
    while state!="end":
        symbol = belt[i]
        first=temporary_belt_maker(belt,state,i, j,p)
        command=fS.commands[(state,symbol)]

        if command == "end":
            last_ever = temporary_belt_maker(belt, state, i, j,p)
            state="end"
        else:
            state=command[0]
            belt[i]=command[1]
            j=i
            if belt[-1]=="B":
                belt.pop(-1)
                p+=1
            if command[2]=="P":
                    i = i+1
                    if i > len(belt)-1:
                        i=0
            if command[2] == "L":
                    i= i-1
                    if i < 0:
                        i=len(belt)-1
            second = temporary_belt_maker(belt, state, i, j, p)
            print(first + " |- " + second)

    difference=belt.count("0")
    print("Jeśli "+first_ever + " |-* " + last_ever)
    print("to różnica właściwa dla "+str(m)+" i "+str(n)+" jest równa "+str(difference))

    return difference

if __name__ == "__main__":
    main()





