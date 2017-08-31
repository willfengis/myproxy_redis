from proxypool.api import app
from proxypool.schedule import Schedule
from multiprocessing import Pool

def main():
    s = Schedule()
    s.run()
    app.run()

if __name__ == '__main__':
    main()
    # loop = Pool(50)
    # loop.map(main())
    # loop.close()
    # loop.join()


