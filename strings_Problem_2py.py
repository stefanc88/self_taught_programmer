

# two user inputs combined into one string


a = input("Enter one of the following nouns: book, poem or e-mail:")
b = input("Enter the person you sent the work to:")

r = """Yesterday I wrote a {}. I sent it to {}""".format(a,b)

print(r)
