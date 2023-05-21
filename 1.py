import simpy
import random

def runner(name, env):
    distance = 0
    while True:
        speed = random.randint(5, 15)
        distance += speed
        print("{} ran {} meters".format(name, distance))
        if distance>=100:
            break


env = simpy.Environment()
runner1 = env.process(runner("Bob", env))
runner2 = env.process(runner("Alice", env))
env.run(until=100)