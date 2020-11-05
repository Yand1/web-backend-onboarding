# Returns an array of names in format "Firstname Lastname"
def get_names_array():
    names = []
    with open("names.txt", "r") as f:
        for line in f:
            names.append(line)
    return names


# Write a program that prints the 5 most popular firstnames and the 5 most popular last names from the names array
# hint: the str.split() function allows for easy string splitting
# hint: use dictionaries to count names
# hint: to sort a dict largest value first, try sorted_list = sorted(first_names.items(), key=lambda x: x[1], reverse=True)
def main():
    names = get_names_array()

if __name__ == "__main__":
    main()