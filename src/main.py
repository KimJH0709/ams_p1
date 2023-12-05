from three_operations import ThreerBasicOperations

from easter_egg import EasterEgg
import threading

# Create an instance of the EasterEgg class
easter_egg = EasterEgg()
# Function to detect the '5' key press
def detect_keys(stop_event):
    easter_egg.track_keys()
# Start the key detection in a separate thread2
stop_event = threading.Event()
key_detection_thread = threading.Thread(target=detect_keys, args = (stop_event,))
key_detection_thread.daemon = True
key_detection_thread.start()


while True:
    infix= ThreerBasicOperations.make_infix()
    ThreerBasicOperations.infix_check(infix)
    postfix = ThreerBasicOperations.make_postfix(infix)
    result = ThreerBasicOperations.calculate(postfix)

    user_input = input("계속 사용 하시겠습니까? (y/n)")
    if user_input.lower() != 'y':
        stop_event.set()
        break