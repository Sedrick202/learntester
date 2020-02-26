def get_summ(one,two,delimiter="&"):
    one = str(one).upper()
    two = str(two).upper()
    return one + delimiter + two

a = get_summ("learn","python",delimiter="&")
print(a)







