import time
from timeit import default_timer as timer

def run_task(name,second):
    print(f'{name} started at : {timer()}')
    time.sleep()
    print(f'{name} completed at: {timer()}')
    

start=timer()
run_task('Task 1',1)
run_task('Task 2',2)
run_task('Task 3',3)

print(f'Total time taken: {timer()-start:.2f}')
