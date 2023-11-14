from three_operations import ThreerBasicOperations

from easter_egg import EasterEgg
import threading

# Create an instance of the EasterEgg class
easter_egg = EasterEgg()
# Function to detect the '5' key press
def detect_keys():
    easter_egg.track_keys()
# Start the key detection in a separate thread
key_detection_thread = threading.Thread(target=detect_keys)
key_detection_thread.start()

ThreerBasicOperations.show_operators()

while True:
    infix= ThreerBasicOperations.make_infix()
    ThreerBasicOperations.infix_check(infix)
    postfix = ThreerBasicOperations.make_postfix(infix)
    result = ThreerBasicOperations.calculate(postfix)

    user_input = input("계속 사용 하기겠습니까? (y/n)")
    if user_input.lower() != 'y':
        break;