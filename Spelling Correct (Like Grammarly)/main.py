from textblob import TextBlob

file1 = open("1.txt", "r+")
a= file1.read()

print("The wrong spelling you wrote: ", str(a))

b = TextBlob(a)

print("The correct spelling of that text was: "+str(b.correct()))
file1.close()


if a == "" or a == " ":
    print("R u making me fool, you just wrote nothing !!!!!!!!!!!!!!!!. 😡😡👿")


d = open("1.txt", "w")
d.write(str(b.correct()))
d.close()

