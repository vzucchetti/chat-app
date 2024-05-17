import flet as ft


# create the main function of the program with all functionalities
def main(page):
    # create elements of text
    # title
    main_title = ft.Text("Hashzap")

    # popup
    # title of popup
    title_popup = ft.Text("Welcome to Hashzap")

    # function to give the enter chat button an action
    def enter_chat(evento):
        # removing the main title
        page.remove(main_title)
        # removing the start chat button
        page.remove(start_button)
        # closing popup
        popup.open = False
        page.add(chat)
        page.add(line_message)
        message = f"{user_name_box.value} joined the chat! Say hello."
        page.pubsub.send_all(message)
        page.update()

    # ask for user enter username
    user_name_box = ft.TextField(label="Write your username", on_submit=enter_chat)

    # load the chat
    chat = ft.Column()

    def send_message_tunnel(message):
        chat_text = ft.Text(message)
        chat.controls.append(chat_text)
        page.update()

    # create a communication tunnel to communicate different users
    page.pubsub.subscribe(send_message_tunnel)

    # function to give the send message button an action
    def send_message(event):
        message_text = message_box.value
        user_name = user_name_box.value
        message = f"{user_name}: {message_text}"
        page.pubsub.send_all(message)
        message_box.value = ""
        page.update()

    # create a box to enter a message on chat
    message_box = ft.TextField(label="Type your message", on_submit=send_message)

    # create button to send message
    send_message_button = ft.ElevatedButton("Send", on_click=send_message)

    # adapt the message box and send button to be side by side
    line_message = ft.Row([message_box, send_message_button])

    # button to enter the chat
    enter_button = ft.ElevatedButton("Enter Chat", on_click=enter_chat)
    popup = ft.AlertDialog(
        title=title_popup, content=user_name_box, actions=[enter_button]
    )

    # start button
    # function to give the start chat button an action
    def start_chat(event):
        page.dialog = popup
        popup.open = True
        page.update()

    start_button = ft.ElevatedButton("Start Chat", on_click=start_chat)

    # add the elements to the page
    page.add(main_title)
    page.add(start_button)


# execute the program
ft.app(main, view=ft.WEB_BROWSER)
