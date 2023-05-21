import simpy
import random

def car(env:simpy.Environment,name):
    while True:
        print(f'仿真时间:{env.now},{name}停车')
        yield env.timeout(random.randint(10,20))

        print(f'仿真时间:{env.now},{name}启动')
        yield env.timeout(random.randint(10, 20))

if __name__ == '__main__':
    env=simpy.Environment()
    cars=[]
    for i in range(10):
        env.process(car(env, f'苏{i+1}'))
    env.run(until=200)