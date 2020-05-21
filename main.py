from pathlib import Path
import matplotlib.pyplot as plt
from datetime import datetime
import fb.fb_data
import fb.messages.conversation
import numpy as np
from pprint import pprint

def main(fb_data_directory: Path):
    data = fb.fb_data.fb_data(fb_data_directory)

    msgs = data.get_messages()

    msgs_sorted = sorted(msgs, key=lambda x: x.getTotalMessages(), reverse=True)

    for i in range(40):
        print(f"Thread: {msgs_sorted[i].getTitle()} has {msgs_sorted[i].getTotalMessages()} messages")
        pprint(msgs_sorted[i].get_messages_per_participants())
        pprint(msgs_sorted[i].get_characters_per_participant())


if __name__ == '__main__':
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--fb_json_path", help="Path to top level of JSON dumped from FB", required=True)

    args = ap.parse_args()

    fb_path = Path(args.fb_json_path)
    if not fb_path.exists():
        print("Ruh roh scoobs")

    main(fb_path)

