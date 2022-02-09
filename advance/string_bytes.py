# strings and bytes are not directly interchangeable
# strings contain unicode , bytes are raw 8-bit values

def main():
    #define some strings starting values
    b = bytes([0x41,0x42,0x43,0x44])
    print(b)

    s = 'This is a String'

    #bytes and strings cannot be combined normally but using decode we can work them together
    s2= b.decode('utf-8') 
    print(s2)
    res = s+s2
    print(res)

    #encode for bytes

    g = "gunalan"
    g2 = g.encode('utf-8')
    print(g2+b)

if __name__ == '__main__':
    main()