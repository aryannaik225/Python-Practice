def count_substring(string, sub_string):
    main_str = []
    sub_str = []
    for i in range(len(string)):
        main_str.append(string[i])
    for i in range(len(sub_string)):
        sub_str.append(sub_string[i])
    
    final_count = 0

    for i in range(len(main_str)):
        count = 0
        for j in range(len(sub_str)):
            if i+j < len(main_str):
                if main_str[i+j] == sub_str[j]:
                    count+=1
                if count == len(sub_string):
                    final_count+=1

    return final_count
    
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)