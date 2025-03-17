import random

class Human:
    def __init__(self, name="Human", job=None, home=None, car=None):
        self.name = name
        self.job = job
        self.home = home
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.car = car

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = Job(job_list)

    def eat(self):
        if self.home.food <= 0:
            self.shopping("food")
        else:
            if self.satiety > 100:
                self.satiety = 100
            return
        self.satiety += 5
        self.home.food -= 5

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping("fuel")
                return
            else:
                self.to_repair()
                return
        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4

    def shopping(self, manage):
        pass

    def chill(self):
        pass

    def clean_home(self):
        pass

    def to_repair(self):
        pass

    def days_indexes(self):
        pass

    def is_alive(self):
        pass

    def live(self):
        pass


class Job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]['salary']
        self.gladness_less = job_list[self.job]['gladness_less']
class House:
    def __init__(self):
        self.mess = 0
        self.food = 0
class Auto:
    def __init__(self, brands_of_car):
        self.brand = random.choice(list(brands_of_car))
        self.fuel = brands_of_car[self.brand]['fuel']
        self.strength = brands_of_car[self.brand]['strength']
        self.consumption = brands_of_car[self.brand]['consumption']




brands_of_car = {"Opel": {"fuel": 20, 'strength': 80, "consumption": 8},
                 "BMW": {"fuel": 40, 'strength': 60, "consumption": 18},
                 "Ford": {"fuel": 30, 'strength': 100, "consumption": 10}}
job_list = {"Java developer": {"salary": 50, "gladness_less": 10},
            "C++ developer": {"salary": 80, "gladness_less": 2},
            "Python developer": {"salary": 40, "gladness_less": 12}}