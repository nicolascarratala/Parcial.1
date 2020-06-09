import unittest
from parameterized import parameterized
from member import Member
from memberService import MemberService
from repository import Repository


class TestMember(unittest.TestCase):

    # *************************
    # ****** Member ***********
    # *************************
    def test_constructor_vacio(self):
        member = Member()
        self.assertDictEqual(member.__dict__, {'_name': '',
                                               '_surname': '',
                                               '_age': '',
                                               '_phone': ''})

    def test_uso_property(self):
        member = Member()
        member.name = 'SANTIAGO'
        member.surname = 'FERNANDEZ'
        member.age = 24
        member.phone = 2615956565
        self.assertDictEqual(member.__dict__, {'_name': 'SANTIAGO',
                                               '_surname': 'FERNANDEZ',
                                               '_age': 24,
                                               '_phone': 2615956565})

    def test_constructor_con_valores_iniciales(self):
        member = Member("PEDRO", "PICO", 30, 2615956565)
        self.assertDictEqual(member.__dict__, {'_name': 'PEDRO',
                                               '_surname': 'PICO',
                                               '_age': 30,
                                               '_phone': 2615956565})

    # *************************
    # *****ServicesMember *****
    # *************************
    @parameterized.expand([
        ("Claudio", "Pico", 30, 2615956565),
        ("Juanx", "Bautista", 15, 2615656545),
    ])
    # Agregar un member
    def test_add_member(self, name, surname, age, phone):
        member = Member(name, surname, age, phone)
        memberKey = MemberService().add_member(member)
        self.assertDictEqual(Repository.membersList[memberKey], member.__dict__)



if __name__ == '__main__':
    unittest.main()