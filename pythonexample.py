# Returns an array of names in format "Firstname Lastname"
def get_names_array():
    names = []
    with open("names.txt", "r") as f:
        for line in f:
            names.append(line)
    return names


# Write a program that prints the 5 most popular firstnames and the 5 most popular last names from the names array
# hint: the str.split function allows for easy string splitting
# hint: to sort a dict largest value first, try sorted_list = sorted(first_names.items(), key=lambda x: x[1], reverse=True)
def main():
    names = get_names_array()
    firstnames = {}
    lastnames = {}
    
    for name in names:
        name_arr = name.split()

        if name_arr[0] not in firstnames:
            firstnames[name_arr[0]] = 0

        firstnames[name_arr[0]] += 1

        if name_arr[1] not in lastnames:
            lastnames[name_arr[1]] = 0

        lastnames[name_arr[1]] += 1

    firstnames_sorted_list = sorted(firstnames.items(), key=lambda x: x[1], reverse=True)
    print("Firstnames:")
    for i in range(5):
        print(firstnames_sorted_list[i][0] + ", count = " + str(firstnames_sorted_list[i][1]))
        
    print()

    lastnames_sorted_list = sorted(lastnames.items(), key=lambda x: x[1], reverse=True)
    print("Lastnames:")
    for i in range(5):
        print(lastnames_sorted_list[i][0] + ", count = " + str(lastnames_sorted_list[i][1]))

if __name__ == "__main__":
    main()