string = input("enter a string you want:")
reference = str.maketrans("kajipotefuKAJIPOTEFU", "akijopetufAKIJOPETUF")
text = string.translate(reference)
print(text)