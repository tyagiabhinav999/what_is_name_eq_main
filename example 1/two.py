import one

print('top-level in two')

one.f()

if __name__ == '__main__':
    print('file two is running directly.')
else:
    print('file two is imported into another module')