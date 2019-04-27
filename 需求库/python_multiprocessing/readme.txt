from multiprocessing import Process
p = Process(target=func, args=(params,))  -> create subprocess
p.start()
p.join()

from multiprocess import Pool
p = Pool(4)
p.apply_async(func, args=(params,))
p.close()  -> must be call before p.join(), it mean you can't add other new process in this main line
p.join()

import subprocess
this is a way for user to control the input&output in subprocess, ignore temporary

from multiprocess import Queue, Process
q = Queue()
worker = Process(target=func, args=(params,))
manager = Process(target=func, args=(params,))
worker.start()
manager.start()
worker.join()
manager.join()

multiprocessing.cpu_count()  -> in this way, you will get the statistic num of you cup