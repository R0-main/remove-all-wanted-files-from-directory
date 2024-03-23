from cleaner import Cleaner

if __name__ == '__init__' :

    path : str = input("Enter the path of your directory :")

    cleaner = Cleaner(path, ('.js', '.d.ts'))
