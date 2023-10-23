def main():
    file = open("Congrats.txt")

    congrats = []
    for line in file:
        line = line.replace("â€™", "'")
        stripped_line = line.strip()
        line_list = stripped_line.split()
        congrats.append(stripped_line)

    file.close()

    print(congrats)

if __name__ == '__main__':
    main()
