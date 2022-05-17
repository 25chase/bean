from djitellopy import tello
from time import sleep

Bee = tello. Tello()
Bee.connect()
print(Bee.get_battery())

Bee.takeoff()

# Takeoff Point
Bee.move_up(95)
Bee.move_foward(325)
sleep(.5)
Bee.move_forward(325)
sleep(1)

# Moving in to the must fly zone
Bee.rotate_counter_cloclwise(98)
Bee.move_foward(325)
sleep(1)

# Going to the start I think
Bee.rotate_counter_clockwise(90)
Bee.move_foward(325)
sleep(.5)
Bee.move_forward(325)
sleep(1)

# Landing zone
Bee.rotate_counter_clockwise(90)
Bee.move_forward(325)
sleep(1)

Bee.land()
