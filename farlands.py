import argparse
import shutil
import logging
from nbtlib import load, File
from nbtlib.tag import Double, List

logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def update_player_position(nbt_path, new_x, new_y, new_z, update_velocity=False):
    logging.info(f"Loading NBT file: {nbt_path}")
    nbt_file: File = load(nbt_path)

    try:
        player_data = nbt_file['Data']['Player']
    except KeyError:
        logging.error("Player data not found in NBT structure.")
        return

    backup_path = nbt_path + '.bak'
    shutil.copy(nbt_path, backup_path)
    logging.info(f"Backup created at: {backup_path}")

    player_data['Pos'] = List([Double(new_x), Double(new_y), Double(new_z)])
    logging.info(f"Updated position to: ({new_x}, {new_y}, {new_z})")

    if update_velocity:
        player_data['Motion'] = List([Double(0.0), Double(0.0), Double(0.0)])
        logging.info("Velocity reset to zero.")

    new_path = 'level_new.dat'
    nbt_file.save(new_path)
    logging.info(f"Saved updated NBT file to: {new_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Update player position in level.dat")
    parser.add_argument('--x', type=float, required=True, help="New X coordinate")
    parser.add_argument('--y', type=float, required=True, help="New Y coordinate")
    parser.add_argument('--z', type=float, required=True, help="New Z coordinate")
    parser.add_argument('--file', type=str, default='level.dat', help="Path to level.dat")
    parser.add_argument('--velocity', action='store_true', help="Reset player velocity to zero")

    args = parser.parse_args()
    update_player_position(args.file, args.x, args.y, args.z, args.velocity)
