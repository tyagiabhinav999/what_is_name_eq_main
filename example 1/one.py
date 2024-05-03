# Understanding if __name__ == __main__:

def f():
    print('Inside one.')

print('top-level in one')

if __name__ == "__main__":
    print("file one is running directly")
else:
    print("file one is imported into another module")
