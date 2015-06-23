def getClass(mark):
    if mark >= 80:
        return "First class with distinction."
    elif mark >= 60:
        return "First class."
    elif mark >=50:
        return "Second class."
    elif mark >= 35:
        return "Passed."
    else:
        return "Failed."

m = int(input("Enter the mark:"))
print(getClass(m));