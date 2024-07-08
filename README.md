# Building a Real-Time Chat Application with Python and Flet
## Project Overview

This repository houses a real-time chat application built using Python and the Flet framework. This chat application is a simple yet functional, that allows users to connect and communicate in real-time. The application features a user-friendly interface built with Flet, a framework that enables the creation of web-based UIs using Python without the need for extensive JavaScript or HTML knowledge.

## Application Features

- **Start Chat:** An initial button that launches the chat experience.
- **Welcome Popup:** A popup dialog greets the user and prompts them to enter a username.
- **Chat Room:** Upon entering the chat, users are presented with a dedicated space to view messages and send new ones.
- **Real-Time Messaging:** The application leverages Flet's PubSub functionality to enable instant message delivery to all connected users.

## Technology Stack

- ``Python``: The core programming language for the application logic and UI design.
- ``Flet``: A Python framework for building interactive web UIs.

## Key Functionality Breakdown

1. **UI Initialization:**
The ``main()`` function sets up the initial UI elements:
    - "*Hashzap*" title
    - "*Start Chat*" button
2. **Start Chat Action:**
    - Clicking "*Start Chat*" opens a popup dialog. This popup contains:
        - "*Welcome to Hashzap*" title
        - A text field for entering a username
        - An "Enter Chat" button
3. **Enter Chat Action:**
    - Clicking "*Enter Chat*":
        - Removes the initial title and "*Start Chat*" button.
        - Closes the popup.
        - Loads the chat interface, which includes:
            - A chat history area (initially empty)
            - A text field for typing messages
            - A "*Send*" button
        - Broadcasts a message to all users announcing the new user's arrival.
4. **Sending Messages:**
    - The "*Send*" button triggers the ``send_message()`` function:
    - Retrieves the user's message and username.
    - Sends the message to all users via the PubSub channel.
    - Clears the message input field.
5. Real-Time Updates:
    - The ``send_message_tunnel()`` function:
    - Subscribes to the PubSub channel to receive incoming messages.
    - Displays each new message in the chat history area.
    - Updates the UI in real-time to reflect new messages.

## Running the Application

1. **Install Flet:**
```
pip install flet
```

2. **Run the Python Script:**
```
python main.py
```

This will launch the application in your default web browser.

## Conclusion

This project demonstrates how Python and Flet can be used to create interactive, real-time applications with ease. Hashzap provides a basic foundation for building more complex chat functionalities, offering a starting point for exploring the potential of web development with Python.
