
if __name__ == '__main__':
    n = int(raw_input().strip())
    if n%2==0 and (n in range(2,6) or n > 20):
        print('Not Weird')
    else:
        print('Weird')
