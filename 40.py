try:
    print(5/0)
    # break

except (ValueError,ZeroDivisionError):
    print("too bad")
