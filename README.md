# Smart Chessboard

![Model](docs/smart-chessboard.png)

## Software flow
The system operates in a continuous loop, alternating between user and bot turns, with validation and feedback mechanisms at each step.

Here is the software execution flow:
1. **Start** - Initialize the system and check all sensors
2. **Scan 8x8 hall sensor array** - Continuously monitor the chess board for piece movements
3. **Check if user moved a piece**
   - If **No**: Return to step 2 (Keep monitoring the chessboard)
   - If **Yes**: Proceed to step 4
4. **Validate if the move is legal**
   - If **No**: Sound the buzzer and return to step 2
   - If **Yes**: Proceed to step 5
5. **Check for end game condition after user move**
   - If **Yes**: Sound the buzzer and stop the game
   - If **No**: Proceed to step 6
6. **Light up LEDs to indicate the user move** - Provide visual feedback
7. **Pass the move to the chess engine** - Calculate the bot's response
8. **Light up LEDs to indicate the bot move** - Show the user the bot's calculated move
9. **Check for end game condition after bot move**
   - If **Yes**: Sound the buzzer and stop the game
   - If **No**: Proceed to step 10
10. **Check if user played the bot move correctly**
    - If **No**: Return to step 10 (Wait for correct execution)
    - If **Yes**: Return to step 2 (Start next turn cycle)
11. **Stop** - End the game when end game condition is met


## Hardware block diagram
![Hardware block diagram](docs/block-diagram.png)

## Repository layout
|Directory|Description of contents|
|--|--|
|board|PCB design files|
|code|Raspberry Pi Zero firmware|
|docs|Design related documents|
|enclosure|Enclosure design files|
|gui|GUI application built using Python 3|

## Ideas for further development
- Connect the chessboard via the internet to another computer
- A 2 axis linear guide setup using stepper motors to move chess pieces using an electromagnet
- RFID based chess piece identification. Scan achieved using an array of 8 RFID readers mounted on a linear guide

### Made with lots of ⏱️, 📚 and ☕ by InputBlackBoxOutput
