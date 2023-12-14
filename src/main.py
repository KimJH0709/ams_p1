from three_operations import ThreerBasicOperations

# from easter_egg import EasterEgg
import threading
import sys
# # Create an instance of the EasterEgg class
# easter_egg = EasterEgg()
# # Function to detect the '5' key press
# def detect_keys(stop_event):
#     easter_egg.track_keys()
# # Start the key detection in a separate thread2
stop_event = threading.Event()
# key_detection_thread = threading.Thread(target=detect_keys, args = (stop_event,))
# key_detection_thread.daemon = True
# key_detection_thread.start()


while True:
    infix= ThreerBasicOperations.make_infix()
    mode = ThreerBasicOperations.infix_check(infix) # 0 +,-,* 계산 / 1 factorial 계산
    if mode == 1:
        print(ThreerBasicOperations.calculateFactorial(infix))
    elif mode == 2:
        postfix = ThreerBasicOperations.make_postfix(infix)
        result = ThreerBasicOperations.calculate(postfix)
        print(result)
    else:
        sys.exit(0)

    user_input = input("계속 사용 하시겠습니까? (y/n)")
    if user_input.lower() != 'y':
        stop_event.set()
        break