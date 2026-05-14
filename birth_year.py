# 7.1 Create years_list 
birth_year = 2005
years_list = list(range(birth_year, birth_year + 6))
print("7.1 years_list:", years_list)

# 7.2 Third birthday year (0 = first year, so index 3)
third_birthday = years_list[3]
print("7.2 Third birthday year:", third_birthday)

# 7.3 Oldest year in list (last year)
oldest_year = years_list[-1]
print("7.3 Oldest year:", oldest_year)


# 7.4 Create list
things = ["mozzarella", "cinderella", "salmonella"]
print("\n7.4 things:", things)


# 7.5 Capitalize person (cinderella)
things[1] = things[1].capitalize()
print("7.5 After capitalizing person:", things)

# Yes — it permanently changes the list


# 7.6 Uppercase cheesy element
things[0] = things[0].upper()
print("7.6 After uppercasing cheese:", things)


# 7.7 Remove disease
things.remove("salmonella")
print("7.7 After removing disease:", things)


# 7.8 surprise list
surprise = ["Groucho", "Chico", "Harpo"]
print("\n7.8 surprise:", surprise)


# 7.9 lowercase last, reverse, then capitalize
surprise[-1] = surprise[-1].lower()[::-1].capitalize()
print("7.9 modified surprise:", surprise)


# 7.10 even numbers using list comprehension
even = [x for x in range(10) if x % 2 == 0]
print("\n7.10 even numbers:", even)


# 7.11 Jump rope rhyme maker
start1 = ["fee", "fie", "foe"]
rhymes = [
    ("flop", "get a mop"),
    ("fope", "turn the rope"),
    ("fa", "get your ma"),
    ("fudge", "call the judge"),
    ("fat", "pet the cat"),
    ("fog", "walk the dog"),
    ("fun", "say we're done"),
]
start2 = "Someone better"

print("\n7.11 Rhymes:\n")

for first, second in rhymes:
    # first line
    print(" ".join(word.capitalize() + "!" for word in start1), end=" ")
    print(first.capitalize() + "!")

    # second line
    print(start2 + " " + second + ".\n")
    2005
    