import pickle


class User:
    def __init__(self, _id, name, surname, mail, photo):
        self.id = _id
        self.name = name
        self.surname = surname
        self.mail = mail
        self.photo = photo
        self.form = Form(_id)

    def __repr__(self):
        return f"User(id: {self.id}, name: {self.name, self.surname}, " \
               f"mail: {self.mail}, photo: {self.photo}, form: {self.form})"


class Answer:
    def __init__(self, mail=None):
        self.mail = mail
        self.force = None
        self.agility = None
        self.speed = None
        self.beauty = None
        self.physique = None
        self.intelligence = None
        self.wisdom = None
        self.stress_tolerance = None
        self.creativity = None
        self.charisma = None
        self.sociability = None
        self.reliability = None
        self.leadership_skills = None
        self.special_skills = None

    def average(self):
        arr = [self.force, self.agility, self.speed, self.beauty, self.physique, self.intelligence,
               self.wisdom, self.special_skills, self.creativity, self.charisma, self.sociability,
               self.reliability, self.leadership_skills, self.special_skills]
        if None not in arr:
            return round(sum(arr) / len(arr), 1)
        return None

    def __repr__(self):
        return f"Answer (mail: {self.mail})"


class Form:
    def __init__(self, _id):
        self.id = _id
        self.answers = []

    def stats(self) -> Answer:
        average = Answer()
        if len(self.answers) > 0:
            average.force = round(sum([answer.force for answer in self.answers]) / len(self.answers), 1)
            average.agility = round(sum([answer.agility for answer in self.answers]) / len(self.answers), 1)
            average.speed = round(sum([answer.speed for answer in self.answers]) / len(self.answers), 1)
            average.beauty = round(sum([answer.beauty for answer in self.answers]) / len(self.answers), 1)
            average.physique = round(sum([answer.physique for answer in self.answers]) / len(self.answers), 1)
            average.intelligence = round(sum([answer.intelligence for answer in self.answers]) / len(self.answers), 1)
            average.wisdom = round(sum([answer.wisdom for answer in self.answers]) / len(self.answers), 1)
            average.stress_tolerance = round(sum([answer.stress_tolerance for answer in self.answers])
                                              / len(self.answers), 1)
            average.creativity = round(sum([answer.creativity for answer in self.answers]) / len(self.answers), 1)
            average.charisma = round(sum([answer.charisma for answer in self.answers]) / len(self.answers), 1)
            average.sociability = round(sum([answer.sociability for answer in self.answers]) / len(self.answers), 1)
            average.reliability = round(sum([answer.reliability for answer in self.answers]) / len(self.answers), 1)
            average.leadership_skills = round(sum([answer.leadership_skills for answer in self.answers])
                                               / len(self.answers), 1)
            average.special_skills = round(sum([answer.special_skills for answer in self.answers])
                                            / len(self.answers), 1)
        return average

    def __repr__(self):
        return f"Form (id: {self.id}, answers = {self.answers})"


class DataBase:
    file_name = "db.dat"

    @staticmethod
    def load():
        try:
            return pickle.load(open(DataBase.file_name, "rb"))
        except FileNotFoundError:
            return {"users": {}}

    @staticmethod
    def save(db):
        pickle.dump(db, open(DataBase.file_name, "wb"))

    @staticmethod
    def get_user_by_mail(mail):
        try:
            return DataBase.load()["users"][mail]
        except KeyError:
            return None

    @staticmethod
    def add_user(user):
        db = DataBase.load()
        db["users"][user.mail] = user
        DataBase.save(db)

    @staticmethod
    def get_user_by_id(_id):
        for user in DataBase.load()["users"].keys():
            if DataBase.load()["users"][user].id == _id:
                return DataBase.load()["users"][user]
        return None

    @staticmethod
    def add_answer(new_answer, form_id):
        flag = True
        answers = DataBase.get_user_by_id(form_id).form.answers
        for index, answer in enumerate(answers):
            if answer.mail == new_answer.mail:
                answers[index] = new_answer
                flag = False
        if flag:
            answers.append(new_answer)
        edited_user = DataBase.get_user_by_id(form_id)
        edited_user.form.answers = answers
        db = DataBase.load()
        db["users"][edited_user.mail] = edited_user
        DataBase.save(db)

