def get_bees_between_flowers(s, start_indexes, end_indexes):
    result = []
    
    for start, end in zip(start_indexes, end_indexes):
        segment = s[start - 1:end] 
        
        first_flower_position = segment.find("|")
        last_flower_position = segment.rfind("|")
        
        if first_flower_position != -1 and last_flower_position != -1:
            bees_count = segment[first_flower_position + 1:last_flower_position].count('*')
            result.append(bees_count)
        else:
            result.append(0)
    
    return result

def main():
    line_segment = input("Enter your string: ")
    
    start_count = int(input("Enter number of start indices: "))
    start_indices = [int(input()) for _ in range(start_count)]
    
    end_count = int(input("Enter number of end indices: "))
    end_indices = [int(input()) for _ in range(end_count)]
    
    result = get_bees_between_flowers(line_segment, start_indices, end_indices)
    
    print(result)

if __name__ == "__main__":
    main()
