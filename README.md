# Smart chessboard
Designs for an electronic chessboard with Stockfish chess engine

## Hardware block diagram
![](docs/block-diagram.png)

## Repository layout
<table>
    <thead>
        <tr>
            <th>Directory</th>
            <th>Description of contents</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>board</td>
            <td>PCB design files for the chessboard</td>
        </tr>
        <tr>
            <td>code</td>
            <td>Raspberry Pi Zero firmware</td>
        </tr>
        <tr>
            <td>docs</td>
            <td>Design related documents</td>
        </tr>
        <tr>
            <td>gui</td>
            <td>GUI application built using python</td>
        </tr>
    </tbody>
</table>

## Ideas for further development
- Connect the application with the chessboard using a wireless network. Interaction will be based on the pub-sub model (See socketio module)
- A 2 axis linear guide setup using stepper motors to move chess pieces using an electromagnet
- RFID based chess piece identification (Scanning using an array of 8 RFID readers mounted on a linear guide)


### Made with lots of ⏱️, 📚 and ☕ by [InputBlackBoxOutput](https://github.com/InputBlackBoxOutput)
