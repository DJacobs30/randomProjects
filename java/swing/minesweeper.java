import java.lang.Math.*;
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class minesweeper extends JFrame implements ActionListener {
    
    // Set Params for Game
    int size = 10;
    int mines = 30;

    // Instance Variables for Field Settings
    int[][] field;
    JButton[][] fieldButtons;

    // Construct the field and place the mines
    public minesweeper() {
        super(" Minesweeper ");

        // Make the field array
        field = new int[size][size];

        // Set up the field of blank squares
        for (int i = 0; i < field.length; i++) {
            for (int n = 0; n < field[i].length; n++) { field[i][n] = 0; }
        }

        // Randomly place mines and update adjacent squares
        setMines();
        makeField();

        // Initialize the display
        startDisplay();

    }

    public void setMines() {

        // Randomly select spots on the field to turn into mines
        for (int n = 0; n < mines; n++) {

            int x = (int) (Math.random()*(field[0].length));
            int y = (int) (Math.random()*(field.length));

            if (field[y][x] == 9) {n -= 1;}
            field[y][x] = 9;
            
        }

    }

    public void makeField() {

        // Scan for mines
        for (int i = 0; i < field.length; i++) {
            
            for (int n = 0; n < field[i].length; n++) {

                // Increase the nearby mine count (NMC) of squares near mines
                int spot = field[i][n];
                if (spot == 9) {

                    for (int m = -1; m  <= 1; m++) {
                        
                        for (int k = -1; k <= 1; k++) {

                            // Move to the adjacent values in the array and increas NMC
                            try {
                                if ((m == 0 && k == 0) || (field[i+m][n+k] == 9)) {field[i][n] += 0;}
                                else {field[i+m][n+k] += 1;}
                            } catch (ArrayIndexOutOfBoundsException e) {}

                        }

                    }

                }

            }

        }

    }

    public void startDisplay() {

        // Make array of buttons mathing the screen
        fieldButtons = new JButton[size][size];

        // Fill array with different buttons labeled for getting the action command
        for (int n = 0; n < size; n++) {

            for (int i = 0; i < size; i++) {

                int buttonNum = (i+(n*size)) + 1000;
                fieldButtons[n][i] = new JButton(String.valueOf(buttonNum));

            }

        }

        // Place the buttons in a grid with dimensions specified in size
        setLayout(new GridLayout(size, size));

        // Add a listener to each button
        for (JButton[] row : fieldButtons) {

            for (JButton space : row) {

                add(space);
                space.addActionListener(this);

            }
        }

        // Set size of display window
        setSize(size*45, size*45);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setVisible(true);

    }

    public void actionPerformed(ActionEvent evt) {

        // Get the coord of the button from the number assigned to it
        String boxString = evt.getActionCommand();
        int spaceNum = Integer.valueOf(boxString) - 1000;
        int[] coords = new int[]{spaceNum % size, spaceNum / size};
        JButton currentButton = fieldButtons[coords[1]][coords[0]];
 
        // Find the similar position in the mine array
        int mineCount = field[coords[0]][coords[1]];
        String numMines = String.valueOf(mineCount);
        
        // Replace the square with the number
        // A period is added to prevent the player from pressing the button again
        currentButton.setText(numMines);

        // Change the color of the box to help differentiate from unpressed buttons
        // Mines are colored black
        if (mineCount == 9) {
            
            currentButton.setBackground(Color.BLACK);
            currentButton.setText("");
                            
        } else {currentButton.setBackground(Color.WHITE);}

        // Remove action listener from button
        currentButton.removeActionListener(this);

    }
    
    public static void main(String[] args) {

        // Run Constructor
        new minesweeper();

    }

}