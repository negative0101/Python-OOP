from MultiLevel.person import Person
from MultiLevel.employee import Employee


class Teacher(Person, Employee):
    def teach(self):
        Person.__init__(self)
        Employee.__init__(self)
        return 'teaching...'
