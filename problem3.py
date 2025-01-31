#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
SLIDER = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
CLAW = Motor(Ports.PORT2, GearSetting.RATIO_18_1, False)


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

myVariable = 0

def when_started1():
# Variable initialization
    myVariable = 0
    SLIDER.set_velocity(55, RPM)

# Initialize the motor to a known home position (at the object)
def set_home_position():
    SLIDER.set_position(0, DEGREES)

def open_claw():
    CLAW.spin_for(FORWARD, 90, DEGREES)

def close_claw():
    CLAW.spin_for(REVERSE, 90, DEGREES)

def move_slider_backward():
    SLIDER.spin_for(REVERSE, 2160, DEGREES)
    wait(4, SECONDS)
    SLIDER.stop()

def set_main_position():
    SLIDER.set_position(1080, DEGREES)

def return_to_home():
    SLIDER.set_position(0, DEGREES)

def grab_and_deposit():
    open_claw()
    wait(1, SECONDS)
    close_claw()
    move_slider_backward()
    open_claw()

def main():
    set_home_position()
    grab_and_deposit()
    set_main_position()
    open_claw()
    return_to_home()
