from dronekit import connect, VehicleMode, LocationGlobalRelative, LocationGlobal, Command
import time
from pymavlink import mavutil

# Connect to the drone
import argparse



def arm_and_takeoff(tgt_altitude,Form):
    print("Arming drone")

    while not vehicle.is_armable:
        time.sleep(1)

    vehicle.mode = VehicleMode("GUIDED")
    vehicle.armed = True

    while not vehicle.armed: time.sleep(1)

    print("Takeoff")
    vehicle.simple_takeoff(tgt_altitude)

    while True:
        altitude = vehicle.location.global_relative_frame.alt
        print(altitude)
        Form.label_3.setText(" m")
        if altitude >= tgt_altitude - 1:
            print("Altitude reached")
            break

        time.sleep(1)


def new_mission():
    print("New Mission")

    cmd = vehicle.commands
    cmd.clear()

    # Takeoff command, ignored if already in air
    cmd.add(
        Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_TAKEOFF, 0, 0, 0, 0,
                0, 0, 0, 0, 10))

    # cmds.add(Command( 0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_WAYPOINT, 0, 0, 0, 0, 0, 0,20.4793259, 85.8995998, 11))
    # cmds.add(Command( 0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_WAYPOINT, 0, 0, 0, 0, 0, 0,20.4738582, 85.8956409, 12))
    # dummy waypoint "5" at point 4 (lets us know when have reached destination)
    # cmds.add(Command( 0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_WAYPOINT, 0, 0, 0, 0, 0, 0, 20.4738582, 85.8956409, 12))

    # cmds.add(Command( 0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_RETURN_TO_LAUNCH, 0, 0, 0, 0, 0, 0,0,0, 0))

    # Upload the commands
    cmd.upload()


def newWaypoint(lat, long, alt):
    print(type(lat))
    cmd = vehicle.commands

    cmd.add(
        Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_WAYPOINT, 0, 0, 0,
                0, 0, 0, lat, long, alt))

    print(lat + " " + long + " " + alt)


def returntolaunch():
    cmd = vehicle.commands
    cmd.add(
        Command(0, 0, 0, mavutil.mavlink.MAV_FRAME_GLOBAL_RELATIVE_ALT, mavutil.mavlink.MAV_CMD_NAV_RETURN_TO_LAUNCH, 0,
                0, 0, 0, 0, 0, 0.0, 0.0, 0.0))
    cmd.upload()


def start(Form):
    arm_and_takeoff(10,Form)
    vehicle.mode = VehicleMode("AUTO")
    print(vehicle.mode.name)


def close():
    vehicle.close()


vehicle = connect("tcp:127.0.0.1:5762", wait_ready=True)
print("Connected")
cmds = vehicle.commands
cmds.download()
cmds.wait_ready()

# Set mode to AUTO to start mission

