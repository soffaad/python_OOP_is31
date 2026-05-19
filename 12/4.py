def read_number(s):
    try:
        num = int(s)
        return num
    except ValueError:
        return "Error"
    finally:
        print("Done")

print(read_number("10"))
print(read_number("abc"))