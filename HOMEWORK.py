# Индивидуальное задание к практической номер 4
# Николаева София
# группа: АДЭУ-201
# вариант 10
# Квитанция, накладная, документ, счет

class Document:
    def __init__(self, name, number, date, addressee):
        self.name = name
        self.number = number
        self.date = date
        self.addressee = addressee

    def requisites(self):
        print(f'НАЗВАНИЕ: {self.name}; НОМЕР: {self.number}; ДАТА: {self.date}; АДРЕСАНТ: {self.addressee}')


class Invoice(Document):
    def __init__(self, number, date, addressee, name = 'НАКЛАДНАЯ',):
        self.name = name
        self.number = number
        self.date = date
        self.addressee = addressee

    def signature(self):
        d = input('Введите дату подписания: ')
        sign_who_passed = input("Подпись того, кто сдал: : ")
        decryption_who_passed = input("Расшифрвка подписи, кто сдал: ")
        sign_who_accepted = input("Подпись того, кто принял: : ")
        decryption_who_accepted = input("Расшифрвка подписи, кто принял: ")
        print(f"ДАТА: {d} СДАЛ: {sign_who_passed} {decryption_who_passed} ПРИНЯЛ: {sign_who_accepted} {decryption_who_accepted}")


class Bill(Invoice):
    def __init__(self, number, date, addressee, name = 'СЧЕТ НА ОПЛАТУ'):
        self.name = name
        self.number = number
        self.date = date
        self.addressee = addressee

    def info_about_service(self):
        number_of_service = input('введите номер услуги/работы: ')
        name_of_service = input('введите название услуги/работы: ')
        cost_of_service = int(input('введите цену услуги/работы: '))
        print(f'НОМЕР: {number_of_service}; НАЗВАНИЕ: {name_of_service}; ЦЕНА: {cost_of_service}')


class Receipt(Bill):
    def __init__(self, number, date, addressee, name = 'КВИТАНЦИЯ',):
        self.name = name
        self.number = number
        self.date = date
        self.addressee = addressee

    def approved(self):
        organization = input('введите наименование органа в творительном падеже: ')
        date_of_approval = input('введите дату утверждения документа: ')
        print(f'{self.name} {self.number} от {self.date} '
              f'УТВЕРЖДЕНО {organization} {date_of_approval}')


doc1 = Document('Приказ', "123", '20.04.2013', 'Иванов')
print(doc1.requisites())
doc2 = Invoice("123", '20.04.2013', 'Иванов')
print(doc2.requisites())
print(doc2.signature())
doc3 = Receipt('123', '12.09.2012', 'Иванов')
print(doc3.requisites())
print(doc3.info_about_service())
print(doc3.signature())
print(doc3.approved())
doc4 = Bill("123", '20.04.2013', 'Иванов')
print(doc4.requisites())
print(doc4.info_about_service())
print(doc4.signature())











