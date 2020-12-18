class Student:
    def __init__(self, fio, dr, pol, number, post, university, fackulty, spec,  grade, group = 'adey'):
        self.fio = fio
        self.dr = dr
        self.pol = pol
        self.number = number
        self.post = post
        self.university = university
        self.fackulty = fackulty
        self.spec = spec
        self.grade = grade
        self.group = group


    def __del__(self):
        print("отчислен студент {} {}".format(self.fio, d[self.grade]))

    def display(self):
        return self.fio, self.dr, self.pol, self.number, self.post, self.university, self.fackulty, self.spec, d[self.grade], self.group




d = {2: 'Двоешник', 4: 'хорошист', 5: 'отличнык'}
s1 = Student('Иванов Иван Иванович', "21.08.2000", 'm', '913', 'h@gmail', 'МГПУ', 'инженерии', '3.09', 5)
print(s1.display())
s2 = Student('Петрова Алина Петровна', "21.09.2000", 'ж', '903', 'д@gmail', 'МГПУ', 'инженерии', '3.09', 2)
print(s2.display())
s3 = Student('Сидорова анастасия владимировна', "26.08.2000", 'ж', '813', '0@gmail', 'МГПУ', 'инженерии', '3.09', 4)
print(s3.display())
del s2
input()

