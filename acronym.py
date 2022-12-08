def main():
    acronym = ''
    word = (input("Enter: ")).split()
    for i in word:
        acronym += i[0].upper()
    print(acronym)

main()
print('commit & push')