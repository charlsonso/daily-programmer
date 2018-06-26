# Given a rectangular input i.e. (10, 6) find the combination of pentominos 
# to be able to pack into a rectangle.

# List of pentominos
# FF I L
#FF  I L      N pp TTT
# F  I L   N N  pp  T
#    I LL N N   p   T
#    I
#
#    V   V w w w y y zz
#U U  V V   w w   y   z
#UUU   V         y    zz
#               y

# square reprensentations               v   w  x    y y
# I  FF FF   L L         N N  TTT U U   v  ww xxx  yy yy  zz zz
# I FF   FF  L L  pp pp  N N   T  UUU vvv ww   x    y y   z   z
# I  F   F   L L  pp pp NN NN  T                    y y  zz   zz
# I         LL LL  p p  N   N  T                    
# I
#
# How to procede
# 1. Brute Force
#    i. Test by randomly combining pentominos until match appears
# 2. Mathmatical
# 3. Graphing (arrays)

# Questions
# How to deal with rotations?

# sample input - 10 6

# output 
# IPPYYYYVVV
# IPPXYLLLLV
# IPXXXFZZLV
# ITWXFFFZUU
# ITWWNNFZZU
# TTTWWNNNUU
