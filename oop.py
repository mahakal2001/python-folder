# class and student:=
'''
class student:
    name = ""
    age = ""
    sex = ""

bhim = student()
bhim.name = "bhim charan bhakta"
bhim.age = 19
bhim.sex = "male"
print("\n.....student- 1 ......")
print(f"Full name : {bhim.name}\nage : {bhim.age}\nsex : {bhim.sex}" )

subal = student()
subal.name = "Subal Bhakta"
subal.age = 48
subal.sex = "male"
print("\n.....student- 2 ......")
print(f"Full name : {subal.name}\nage : {subal.age}\nsex : {subal.sex}" )

anima = student()
anima.name = "Anima Bhakta"
anima.age = 40
anima.sex = "female"
print("\n.....student- 3 ......")
print(f"Full name : {anima.name}\nage : {anima.age}\nsex : {anima.sex}" )
'''

# me

class student:
    name = ""
    age = ""
    sex = ""

    def dispay(self):
        print(f"Full name : {self.name}\nAge :{self.age}\nSex : {self.sex}")

bhim = student()
bhim.name = "bhim charan bhakta"
bhim.age = 19
bhim.sex = "male"
print("\n.....student- 1 ......")
bhim.dispay()

subal = student()
subal.name = "Subal Bhakta"
subal.age = 48
subal.sex = "male"
print("\n.....student- 2 ......")
subal.dispay()

anima = student()
anima.name = "Anima Bhakta"
anima.age = 40
anima.sex = "female"
print("\n.....student- 3 ......")
anima.dispay()

# Exercise:=

