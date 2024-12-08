def find_strongest_trainees(data):
    r1, r2, r3 = data
    t1 = (r1[0] + r2[0] + r3[0]) // 3
    t2 = (r1[1] + r2[1] + r3[1]) // 3
    t3 = (r1[2] + r2[2] + r3[2]) // 3
    t4 = (r1[3] + r2[3] + r3[3]) // 3

    avgs = [t1, t2, t3, t4]
    max_strength = max(avgs)

    if max_strength < 100:
        return ["All trainees are unfit"]

    strongest_trainees = []
    for i in range(len(avgs)):
        if avgs[i] == max_strength:
            strongest_trainees.append(f"Trainee Number: {i + 1}")
    
    return strongest_trainees

def main():
    data = []
    for i in range(3): 
        each_round = []
        for j in range(4): 
            read = int(input(f"Enter strength lifted by Trainee {j+1} in Round {i+1}: "))
            if read < 1 or read > 200:
                print("INVALID INPUT")
                exit()
            each_round.append(read)
        data.append(each_round)

    result = find_strongest_trainees(data)
    for res in result:
        print(res)

if __name__ == "__main__":
    main()
