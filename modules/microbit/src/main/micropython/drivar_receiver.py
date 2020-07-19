from microbit import *
import radio
import neopixel


ROBOT_BITBOT_XL = "bitbotxl"
ROBOT_BITBOT = "bitbot"
ROBOT_BUGGY_MK3 = "buggymk3"


pin_direction_left = None
pin_direction_right = None
pin_speed_left = None
pin_speed_right = None

# Very simple and probably buggy line protocol parser
# Do not reuse !

def _pop_head_or_none(arr, peek_only = False):
    if arr and len(arr)>0:
        if peek_only:
          return arr[0]
        else:
          return arr.pop(0)
    else:
        return None


def parse_lineprotocol_message(msg):
    measurement = None
    tags = {}
    values = {}
    value = None

    fragments = msg.split(" ")
    fragment = _pop_head_or_none(fragments)
    if fragment is not None:
        measurementFragments = fragment.split(",")
        if len(measurementFragments) > 0:
            measurement = measurementFragments[0]
        if  len(measurementFragments) > 1:
            for tagFragment in measurementFragments[1:]:
                tagKV = tagFragment.split("=")
                tags[tagKV[0]] = float(tagKV[1])
        
    fragment = _pop_head_or_none(fragments,True)
    if fragment is not None:
        if("=" in fragment):
            fragment = _pop_head_or_none(fragments)
            valuesFragment = fragment.split(",")
            for valueFragment in map(lambda v: v.split("="),valuesFragment):
                if len(valueFragment) > 1:
                  values[valueFragment[0]] = valueFragment[1]

    fragment = _pop_head_or_none(fragments)
    if fragment is not None:
        value = float(fragment)
        
    return (measurement, tags, values, value)

def configure_pin_mapping(model):
    if(model == ROBOT_BITBOT_XL):
        pin_direction_left = pin8
        pin_direction_right = pin12
        pin_speed_left = pin16
        pin_speed_right = pin14
    else if (model == ROBOT_BITBOT or model == ROBOT_BUGGY_MK3):
        pin_direction_left = pin8
        pin_direction_right = pin12
        pin_speed_left = pin0
        pin_speed_right = pin1


def move(speed, steer):
    # Sensible defaults that mean "stop".
    forward = 0
    left = 0
    right = 0
    if speed > 0:
        display.show(Image.ARROW_S)
        # Moving forward.
        forward = 1
        left = 1000 - speed
        right = 1000 - speed
    elif speed < 0:
        display.show(Image.ARROW_N)
        # In reverse.
        left = 1000 + (-1000 - speed)
        right = 1000 + (-1000 - speed)
    if steer < 0:
        # To the right.
        right = min(1000, right + abs(steer))
        left = max(0, left - abs(steer))
    elif steer > 0:
        # To the left.
        left = min(1000, left + steer)
        right = max(0, right - steer)
    # Write to the robot motors.
    pin_direction_left.write_digital(forward)
    pin_direction_right.write_digital(forward)
    pin_speed_left.write_analog(left)
    pin_speed_right.write_analog(right)


while True:
    try:
        msg = radio.receive()
        if button_a.is_pressed():
          msg = "move steer=0,speed=500"
        if button_b.is_pressed():
          msg = "move steer=0,speed=-500"
    except:
        msg = None  # Networks are not safe!
    if msg is not None:
        command,tags,values,value = parse_lineprotocol_message(msg)
        if command == "move":
            steer = values["steer"] if values["steer"] is not None else 0
            speed = values["speed"] if values["speed"] is not None else 0
            move(int(speed),int(steer))
        if command == "stop":
            move(0,0)
        
    else:
        # No message? Do nothing!
        move(0, 0)
        display.show(Image.SKULL) 
    sleep(20)



cfg_radio_channel = 42
cfg_robot_model = ROBOT_BITBOT_XL
try:
  with open("drivar_cfg.txt") as config_file:
      cfg_line=config_file.read_line()
      if len(cfg_line) >0:
          category,tags,values,value = parse_lineprotocol_message(cfg_line)
          if(category == "drivar"):
              cfg_radio_channel = int(tags["channel"]) if tags["channel"] is not None else cfg_radio_channel
              cfg_robot_model = tags["model"] if tags["model"] is not None else ROBOT_BITBOT_XL
  configure_pin_mapping(cfg_robot_model)
  radio.config(channel=cfg_radio_channel)
  radio.on()
  display.show(Image.YES) 
except: 
  display.show(Image.NO)

