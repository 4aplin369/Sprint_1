class Tester:

    def __init__(self, name, deadline):
        self.name = name
        self.deadline = deadline

    def work_hard(self, deadline=True):
        if self.deadline:
            print(self.name, 'Что ж, ещё часок поработаю!')
        else:
            print(self.name, 'Можно отдыхать')

tester_1 = Tester('tester_1', False)
tester_1.work_hard(deadline=False)  # 'tester_1 Можно отдыхать'
tester_2 = Tester('tester_2', True)
tester_2.work_hard(deadline=True)   # 'tester_2 Что ж, ещё часок поработаю!' 