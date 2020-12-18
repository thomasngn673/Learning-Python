import time, sys

#
# indent = 0
# while True:
#     try:
#         for indent in range(0, 20, 1):
#             print(' ' * indent, end='')
#             print('********')
#             time.sleep(.1)
#         for indent in range(20, 0, -1):
#             print(' ' * indent, end='')
#             print('********')
#             time.sleep(.1)
#     except KeyboardInterrupt:
#         sys.exit()

indent = 0
indentIncreasing = True
try:
    while True:
        if indentIncreasing:
            indent = indent + 1
            if indent == 20:
                indentIncreasing = False
        else:
            indent = indent - 1
            if indent == 0:
                indentIncreasing = True

        print(' ' * indent, end='')
        print('********')
        time.sleep(.1)
except KeyboardInterrupt:
    sys.exit()