def main():
    N = 2

    if N == 1:
        print('*')
    elif N == 2:
        print('**')
        print('**')
    else:
        for _ in range(N):
            if N > 2:
                print('*' + ' ' * (N - 2) + '*')


if __name__ == '__main__':
    main()
