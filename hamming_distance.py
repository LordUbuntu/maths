# Jacobus Burger (Created 2018, Last Edited 2024-08-08)
# Prologue:
#   This was sourced from discrete.py which was originally written in
#   2018/2022 to better understand and learn discrete math. That was
#   done for fun and practice, and inspired by the great influence of
#   my discrete math Professors Richard J Sutcliffe.
#
#   Thank you to Professor Richard J. Sutcliffe for being such an awesome
#   teacher and inspiration in both my discrete math courses.
#   I had a lot of fun taking those courses (though it was hard) and
#   I hope to carry the knowledge into my future, and continue to learn
#   and improve because of it. I will grow and transform.
# Desc:
#   Hamming Distance calculates the distance / amount of difference
#   between two strings of information (usually binary numbers, but
#   can be for any sequential pieces of data, aka: strings).
# Info:

# find the hamming distance of any two strings
# this should work with lists, strings, and other sequential data types
def hamming_distance(a, b):
    return sum(map(op.ne, a, b))
