#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
optical_1 = Optical(Ports.PORT1)
motor_2 = Motor(Ports.PORT2, GearSetting.RATIO_18_1, False)


# wait for rotation sensor to fully initialize
wait(30, MSEC)


# Make random actually random
def initializeRandomSeed():
    wait(100, MSEC)
    random = brain.battery.voltage(MV) + brain.battery.current(CurrentUnits.AMP) * 100 + brain.timer.system_high_res()
    urandom.seed(int(random))
      
# Set random seed 
initializeRandomSeed()


def play_vexcode_sound(sound_name):
    # Helper to make playing sounds from the V5 in VEXcode easier and
    # keeps the code cleaner by making it clear what is happening.
    print("VEXPlaySound:" + sound_name)
    wait(5, MSEC)

# add a small delay to make sure we don't print in the middle of the REPL header
wait(200, MSEC)
# clear the console to make sure we don't have the REPL in the console
print("\033[2J")

#endregion VEXcode Generated Robot Configuration

def when_started1():
    while True:
        optical_1.set_light(50, PERCENT)
        # Get the color detected by the optical sensor
        value = optical_1.color()
        color = optical_1.hue()
        
        # Map hue (0-360) to motor speed (0-100)
        motor_speed = int(color / 360 * 100)

        # Set the motor speed based on the color's hue
        motor_2.spin(FORWARD, motor_speed, PERCENT)
        
        # Display the hue value on the screen for debugging
        brain.screen.print("Color Hue: {}".format(color))
        brain.screen.next_row()
        
        # Delay to prevent the motor from running too quickly
        wait(50, MSEC)

when_started1()
