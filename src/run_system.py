import time
import traceback

from example_system import ExampleSystem

aituber_system = ExampleSystem()
while True:
    try:
        aituber_system.talk_with_comment()
        time.sleep(5)
    except Exception as e:
        print('An error has occurred')
        print(traceback.format_exc())
        print(e)
        exit(200)
