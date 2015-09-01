
def f(A):
   if len(A) == 0:
      return 0
   else:
      first = A.pop(0)
      return 1 + f(A)

print(f([1,2,3,4,5]))
'''
Why?
(1) f returns 0 when input is an empty list.  This is correct.
(2) Suppose len(A) is k+1.  After line 6, len of A is k.  Assume f works correctly for input sizes less than k+1.  Then, line 7 returns 1 + k.  So, f is correct for input size n.


Math induction:
To prove S(n) correct all n's.
(1) Prove S(0) correct.
(2) Prove "If S(0), S(1), ..., S(k) all correct, then S(k+1) is correct."
same:
Assuming S(0), S(1), ..., S(k) all correct, prove S(k+1) is correct.

'''