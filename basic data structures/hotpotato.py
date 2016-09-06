from pythonds.basic.queue import Queue

def hotPotato(players, num):
    simQueue = Queue()

    for name in players:
        simQueue.enqueue(name)

    while simQueue.size() > 1:
        for i in range(num):
            simQueue.enqueue(simQueue.dequeue())

        simQueue.dequeue()

    return simQueue.dequeue()

print hotPotato(["Jorge", "Ana"], 7)
