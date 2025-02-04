#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
SLIDER = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
CLAW = Motor(Ports.PORT2, GearSetting.RATIO_18_1, False)
bumper_h = Bumper(brain.three_wire_port.h)


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
    wait(2,SECONDS)

def close_claw():
    CLAW.spin_for(REVERSE, 170, DEGREES)

def move_slider_backward():
    SLIDER.spin_for(REVERSE, 1850, DEGREES)
    wait(3, SECONDS)
    SLIDER.stop()

def set_main_position():
    SLIDER.spin_for(FORWARD,1850, DEGREES)
    wait(4, SECONDS)
    SLIDER.stop()

def return_to_home():
    SLIDER.set_position(0, DEGREES)

def grab_and_deposit():
    open_claw()
    wait(1, SECONDS)
    close_claw()
    move_slider_backward()
    open_claw()
    set_main_position()

def main():
    
    while True:
        if bumper_h.pressing(): 
            grab_and_deposit() 
            wait(2, SECONDS)  
main()
