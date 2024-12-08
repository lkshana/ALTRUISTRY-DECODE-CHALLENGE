def first_odd_flavour(n, flavours):
    diff_flavours = []
    for each in flavours:
        if each not in diff_flavours and flavours.count(each) % 2 != 0:
            diff_flavours.append(each)
    if diff_flavours:
        return diff_flavours[0]
    else:
        return "All are Even"

def main():
    n = int(input("Enter the number of flavours: "))
    flavours = [input("Enter flavour: ") for _ in range(n)]
    result = first_odd_flavour(n, flavours)
    print(result)

if __name__ == "__main__":
    main()
