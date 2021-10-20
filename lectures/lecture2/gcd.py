
def GCD(m,n):
    print("m={} n={}".format(m,n))
    if m < n:
        return GCD(n,m)
    if m % n == 0:
        return n
    return GCD(n, m % n)

def main():
    gcd = GCD(24, 21)
    print(gcd)

if __name__ == "__main__":
    main()