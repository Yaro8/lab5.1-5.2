if __name__ == '__main__':
    import random


    def generate_password(m):
        list_for_generate = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'p', 'q',
                             'r', 's',
                             't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J',
                             'K', 'L',
                             'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '2',
                             '3', '4',
                             '5', '6', '7', '8', '9', ]
        list_password = random.sample(list_for_generate, m)
        password = ''
        for i in list_password:
            password += i
        return password


    def main(m, n):
        while n != 0:
            print(generate_password(m))
            n -= 1


    count_of_passwords = int(input())
    count_of_symbols = int(input())
    print(main(count_of_passwords, count_of_symbols))
