# Eculidean Algo
# GCD(A,B). where (A>=B)
# keep doing GCD(A <-B, B <- A%B) untill B==0
# GCD(x=any number, 0)=x as x*0 = 0. 
# GCD(24,9)-> GCD(9,6) -> GCD(6,3) -> GCD(3,6/3 = 0)=3 

def gcd_iter(A,B):
    while B!=0:
        print(f'A={A} B={B}')
        r = A%B
        A = B
        B = r 
        print(f'B={B}')
    # when we have reached B=0 then return A
    return A

def gcd_recur(A,B):
    if B==0:
        return A
    return gcd_recur(B, A%B)

if __name__=='__main__':
    A=24
    B=9
    print(f'gcd_iter({A},{B})= {gcd_iter(A,B)}')
    print(f'gcd_recur({A},{B})= {gcd_recur(A,B)}')

