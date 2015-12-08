import socket

from conf import ADDRESS

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect(ADDRESS)

large_message = '''Lorem ipsum dolor sit amet,\nconsectetur adipiscing elit. Proin lacus neque,\nluctus non commodo nec,\ndapibus at ex. Vestibulum blandit at mi sed venenatis.\nSed bibendum orci a mi lacinia, egestas ullamcorper ligula sagittis.\nNunc vulputate ante id eros mattis convallis.\nEtiam vel lectus varius, accumsan erat nec,\nimperdiet dolor.\nProin sagittis mollis velit viverra lacinia. Morbi quis orci bibendum,\ntincidunt dui dictum, vehicula augue.\nDonec eu pulvinar erat, vel mollis tellus.\nIn fringilla enim enim, egestas vulputate nibh suscipit eget.\nNam eu tincidunt leo, ut rutrum orci.\nCras et ligula diam. Nulla commodo cursus sem vel molestie.\n\nDonec sed tincidunt nunc.\nFusce urna felis, posuere condimentum viverra feugiat, euismod ut sapien.\nMaecenas auctor porttitor tincidunt.\nNam sit amet tortor at ipsum aliquam tristique ut non risus.\nVivamus ultricies, ante a laoreet suscipit, augue mi dignissim eros, nec porttitor dolor arcu non odio.\nNulla at laoreet justo. Nullam sapien nisl, scelerisque lobortis metus.\n'''

menu = '''
    menu:
    1) send large message
    2) custom messages
    3) close
'''
user_message = ""


def sending(message):
    print 'sending message...'
    server.sendall(message)

    message_recivied_length = 0
    complete_message = ''
    goal = len(message)

    while message_recivied_length < goal:
        data = server.recv(16)
        message_recivied_length += len(data)
        complete_message += data
    return complete_message


def send_large_message():
    complete_message = sending(large_message)
    print 'message recived:\n%s' % complete_message
    return True


def send_user_message():
    user_message = raw_input("\nType your message or Q to quit:\n")
    while user_message != "Q":
        if user_message != "Q":
            response = sending(user_message)
            print 'message recived:\n"%s"' % str(response)
        user_message = raw_input("\nType your message or Q to quit:\n")
    return True


def close():
    server.close()
    print "bye!"
    return False


menu_function_dict = {
    "1": send_large_message,
    "2": send_user_message,
    "3": close
}


def main():
    play = True
    while play:
        print menu
        option = raw_input("select an option:\n")

        if option not in ['1', '2', '3']:
            print "You choose an avaible option.\nPlease, choose another."
            option = raw_input("select an option:\n")

        play = menu_function_dict[option]()

if __name__ == "__main__":
    main()
