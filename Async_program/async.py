import  asyncio
import time
from timeit import default_timer as timer

async  def run_task(name,second):
        print(f'{name} started at : {timer()}')
        await asyncio.sleep(second)
        print(f'{name} completed at: {timer()}')
    
    
async def main():
    start=timer()
    await asyncio.gather(
        run_task('Task 1',1),
        run_task('Task 2',2),
        run_task('Task 3',3)

    )

print(f'Total time taken: {timer()-start:.2f}')
