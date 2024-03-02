#5 ადამიანს შემოატანინეთ თავისი ასაკი, პირველი ორი შემოტანილი ასაკი გაამრავლეთ ერთმანეთზე, შემდგომ მესამე შემოტანილ ასაკზე გაყეთ,  ხოლო მეოთხისა და მეხუთს ასაკები დაამატეთ ერთმანეთზე და გადაამრავლეთ პირველისა და მეორის საბოლოო ჯამზე

nanuka = int(input("enter nanukas age : "))
jeko = int(input("enter jekos age :"))
leqso =int(input("enter leqsos age :"))
barbare =int(input("enter barbares age:"))
batoni_davit_janezashvili =int(input("enter batoni davit janezashvilis age :"))
multiplication = nanuka * jeko
print("multiplication answer is " + str(multiplication))
division = multiplication // leqso
print("division answer is " + str(division))
addition = barbare + batoni_davit_janezashvili
print("addition answer is " + str(addition))
final_answer = (multiplication + division ) * addition
print("final answer is " + str(final_answer))