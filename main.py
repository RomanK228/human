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
        self.health = 100

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
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                manage = "fuel"
            else:
                self.to_repair()
                return
        if manage == "fuel":
            print("I bought fuel")
            self.money -= 100
            self.car.fuel += 50
        elif manage == "food":
            print("I bought food")
            self.money -= 50
            self.home.food += 30
        elif manage == "Chocolate":
            print("I`m happy")
            self.money -= 10
            self.gladness += 10
            self.satiety += 5

    def chill(self):
        print("Time to chill")
        self.gladness += 10
        self.home.mess += 10

    def clean_home(self):
        print("Time to clean")
        self.gladness -= 10
        self.home.mess = 0

    def to_repair(self):
        self.car.strength += 100
        self.money -= 50
        self.gladness += 10

    def days_indexes(self, day):
        d = f"Today the {day} of {self.name}'s life"
        print(f"{d:=^50}\n")
        print(f"Money {self.money}")
        print(f"Gladness {self.gladness}")
        print(f"Food {self.home.food}")
        print(f"Mess {self.home.mess}")
        print(f"Fuel {self.car.fuel}")
        print(f"Strength {self.car.strength}")
        print(f"Satiety {self.satiety}")
        print(f"Health {self.health}")

    def is_alive(self):
        if self.gladness <= 0:
            print("Depression...")
            return False
        if self.satiety < 0:
            print("Dead")
            return False
        if self.money <= -100:
            print("Bankrupt...")
            return False

        # if self.health <= 0:
        #     print("Died")
        # else:
        #     print("Alive")

    def live(self):
        if not self.is_alive():
            return False
        if self.home is None:
            print("Settled in the house")
            self.get_home()
        if self.job is None:
            self.get_job()
            print(f"I`m a job {self.job.job},salary {self.job.salary}")
        if self.car is None:
            self.get_car()
            print(f"I bougth a car {self.car.brand}")
        self.days_indexes(day)
        dice = random.randint(1, 4)
        if self.satiety < 20:
            print("Time to eat")
            self.eat()
        elif self.gladness < 20:
            if self.home.mess > 20:
                print(f"I want to chill, but there is so much mess\nSo I will clean house")
                self.clean_home()
            else:
                print("Time to chill")
                self.chill()
        elif self.money < 0:
            print("Time to work")
            self.work()
        elif self.car.strength < 10:
            print("Need to repair car")
            self.to_repair()
        elif dice == 1:
            print("Time to chill")
            self.chill()
        elif dice == 2:
            print("Time to work")
            self.work()
        elif dice == 3:
            print(f"Time to clean house")
            self.clean_home()
        elif dice == 4:
            print("Need to shopping")
            self.shopping(manage="delicacies")


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

hum = Human(name="Evfrat")
for day in range(1, 365):
    if hum.live(day) == False:
        break
