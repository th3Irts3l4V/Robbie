
# Robbie: The Raspberry Pi 4 Freenove 3WD Car Kit Project

Welcome to Robbie, a highly engaging and interactive project designed to bring robotics into your hands using the Raspberry Pi 4 and the Freenove 3WD Car Kit. This repository is dedicated to all hobbyists, educators, and students who share a passion for robotics and coding. Dive into the world of robotics with Robbie, and experience the thrill of controlling a custom-built robot with your keyboard.

## Project Overview

Robbie is not just a robot; it's your companion into the world of technology and engineering. Built on the versatile Raspberry Pi 4 platform and leveraging the capabilities of the Freenove 3WD Car Kit, Robbie offers an accessible yet powerful platform for learning, experimentation, and fun. This project includes a client-server architecture that allows you to control Robbie using the WASD keys on your keyboard, similar to controlling a character in a video game.

### Key Features

- **Real-time Control**: Experience seamless and intuitive control over Robbie with real-time responsiveness.
- **Networked Interaction**: Control Robbie from anywhere on your network, thanks to the client-server setup.
- **Extensible Platform**: Built using Python, Robbie is easily extendable with additional sensors and modules for endless experimentation.
- **Educational Tool**: Learn fundamental concepts in robotics, programming, and networking in a hands-on manner.

## Getting Started

To get started with Robbie, you'll need a Raspberry Pi 4, the Freenove 3WD Car Kit, and a sense of adventure. Follow the instructions below to set up your environment and begin your journey into robotics.

### Prerequisites

- Raspberry Pi 4 with Raspbian OS installed
- Freenove 3WD Car Kit (assembled according to the manufacturer's instructions)
- Python 3.x installed on both your Raspberry Pi and client computer
- `smbus` library installed on your Raspberry Pi (`pip3 install smbus`)
- `keyboard` library installed on your client computer (`pip install keyboard`)

### Installation

1. **Clone the Repository**: Clone this repository to your Raspberry Pi and client computer.
    ```
    git clone https://github.com/th3Irts3l4V/Robbie.git
    ```
2. **Install Dependencies**: Make sure you have all the required libraries installed on both your Raspberry Pi and client computer.

3. **Configure the Network**: Ensure both your Raspberry Pi and client computer are connected to the same network. Note down the IP address of your Raspberry Pi.

### Running Robbie

1. **Start the Server on Raspberry Pi**: Navigate to the project directory and run the server script.
    ```
    cd Robbie
    sudo python3 server.py
    ```
2. **Control Robbie from Your Client Computer**: Open another terminal on your client computer, navigate to the project directory, and run the client script.
    ```
    cd Robbie
    python client.py
    ```

## Documentation

For a deeper dive into Robbie's architecture, setup instructions, and customization options, refer to the [Documentation](docs/).

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Your Name - @YourTwitter - email@example.com

Project Link: [https://github.com/th3Irts3l4V/Robbie](https://github.com/th3Irts3l4V/Robbie)

## Acknowledgments

- Freenove for their excellent 3WD Car Kit
- Raspberry Pi Foundation for creating a versatile computing platform
