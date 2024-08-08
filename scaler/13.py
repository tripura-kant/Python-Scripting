def main():
    # Read input
    N = 4

    # Generate and print the pattern
    for i in range(1, N + 1):
        # Create the line with numbers from 1 to i
        line = ' '.join(str(x) for x in range(1, i + 1))
        # Print the line
        print(line)


if __name__ == '__main__':
    main()
