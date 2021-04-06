import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

/*
 * Written by GraphicsUnderTheInfluence
 * April 5, 2021
 * Enjoy :)
 * 
 * Steps:
 *  - Edit the names for the teams
 *  - Press the Bid Button for the team that wins the bid
 *  - Enter their bid into the text field then press enter
 *  - Type the amount of points the other team makes in the other box
 *  - Repeat each hand
 */

public class RookGUI extends JFrame implements ActionListener {

    // Create Instance Variables for the 16 widgets on the GUI
    private JLabel teamOneA;
    private JLabel teamOneB;
    private JLabel teamTwoA;
    private JLabel teamTwoB;
    private JTextField bidOne;
    private JTextField bidTwo;
    private JButton bbOne;
    private JButton bbTwo;
    private JTextField pointsOne;
    private JTextField pointsTwo;
    private JLabel sbOne;
    private JLabel sbTwo;
    private JLabel scoreOne;
    private JLabel scoreTwo;
    private int teamOneScore = 0;
    private int teamTwoScore = 0;
    private JLabel scoreLabelOne;
    private JLabel scoreLabelTwo;

    // Create Instance Variables to know which event was from which text field
    private Boolean team;
    private Boolean afterButton = false;
    private Boolean afterBid = false;

    // Create Instance Variables to hold key values
    private int teamOneBid;
    private int teamTwoBid;
    private int teamOnePoints;
    private int teamTwoPoints;

    // Make it easy to change names of teams
    private String oneA = "Joey";
    private String oneB = "Billy";
    private String twoA = "Jason";
    private String twoB = "Bob";

    // Construct the GUI
    public RookGUI() {
        super(" Rook Score Keeper ");

        // Initialize the widgets
        InitGui();

        setSize(500, 350);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setVisible(true);

    }

    private void InitGui() {

        // Display Team Names
        teamOneA = new JLabel(oneA, SwingConstants.RIGHT);
        teamOneB = new JLabel(oneB, SwingConstants.LEFT);
        teamTwoA = new JLabel(twoA, SwingConstants.RIGHT);
        teamTwoB = new JLabel(twoB, SwingConstants.LEFT);

        // Text Fields to enter the bids
        bidOne = new JTextField();
        bidTwo = new JTextField();

        // Button to select who won the bid
        bbOne = new JButton("Bid One");
        bbTwo = new JButton("Bid Two");

        // Text Fields to enter points scored to set
        pointsOne = new JTextField();
        pointsTwo = new JTextField();

        // Show which row is score
        sbOne = new JLabel("Points", SwingConstants.CENTER);
        sbTwo = new JLabel("Points", SwingConstants.CENTER);

        // Display the teams score
        scoreOne = new JLabel(String.valueOf(teamOneScore), SwingConstants.RIGHT);
        scoreTwo = new JLabel(String.valueOf(teamOneScore), SwingConstants.LEFT);

        scoreLabelOne = new JLabel("Score", SwingConstants.CENTER);
        scoreLabelTwo = new JLabel("Score", SwingConstants.CENTER);

        // Layout in a grid of four collumns and four rows
        setLayout(new GridLayout(4, 4, 30, 30));

        // Add the widgets to the grid
        add(teamOneA);
        add(teamOneB);
        add(teamTwoA);
        add(teamTwoB);
        add(bidOne);
        add(bbOne);
        add(bbTwo);
        add(bidTwo);
        add(pointsOne);
        add(sbOne);
        add(sbTwo);
        add(pointsTwo);
        add(scoreOne);
        add(scoreLabelOne);
        add(scoreLabelTwo);
        add(scoreTwo);

        // Create listeners for each field and button
        bidOne.addActionListener(this);
        bidTwo.addActionListener(this);
        pointsOne.addActionListener(this);
        pointsTwo.addActionListener(this);
        bbOne.addActionListener(this);
        bbTwo.addActionListener(this);

    }

    private void calculateScore() {

        // Determine which team took the bid
        if (team == true) {

            // Determine if the bid was met or not
            if (teamOneBid + teamTwoPoints > 180) {

                System.out.println("Team One Set");
                teamOneScore -= teamOneBid;
                teamTwoScore += teamTwoPoints;

            } else {

                System.out.println("Team One Bid Made");
                teamOneScore += 180 - teamTwoPoints;
                teamTwoScore += teamTwoPoints;

            }

        } else {

            // Determine if the bid was met or not
            if (teamTwoBid + teamOnePoints > 180) {

                System.out.println("Team Two Set");
                teamTwoScore -= teamTwoBid;
                teamOneScore += teamOnePoints;

            } else {

                System.out.println("Team Two Bid Made");
                teamTwoScore += 180 - teamOnePoints;
                teamOneScore += teamOnePoints;

            }

        }

        updateScore();

    }

    private void updateScore() {

        // Reset the widgets for the next hand
        bidOne.setText("");
        bidTwo.setText("");
        pointsOne.setText("");
        pointsTwo.setText("");
        bbOne.setText("Bid One");
        bbTwo.setText("Bid Two");
        
        scoreOne.setText(String.valueOf(teamOneScore));
        scoreTwo.setText(String.valueOf(teamTwoScore));

    }

    public void actionPerformed(ActionEvent evt) {

        String buttonPressed = evt.getActionCommand();

        // Determine what stage of the hand you are in
        if (afterButton == true) {

            // Determine which team bid then save their bid to the instance variable
            if (team == true) {

                System.out.println("Team One Bid");
                teamOneBid = Integer.parseInt(evt.getActionCommand());
                bidTwo.setText(String.valueOf(185 - teamOneBid));
                bbTwo.setText("Min to Set");
                afterButton = false;
                afterBid = true;

            } else {

                System.out.println("Team Two Bid");
                teamTwoBid = Integer.parseInt(evt.getActionCommand());
                bidOne.setText(String.valueOf(185 - teamTwoBid));
                bbOne.setText("Min to Set");
                afterButton = false;
                afterBid = true;

            }

        } else if (afterBid == true) {

            // Determine which team won the bid then take the other teams points and calculate the scores
            if (team != true) {

                System.out.println("Team One Points");
                teamOnePoints = Integer.parseInt(evt.getActionCommand());
                calculateScore();
                afterBid = false;

            } else {

                System.out.println("Team Two Points");
                teamTwoPoints = Integer.parseInt(evt.getActionCommand());
                calculateScore();
                afterBid = false;

            }

        } else {

            // Check for which button got pressed to see who won the bid
            if (buttonPressed == "Bid One") {

                System.out.println("Team One Bidding");
                team = true;
                afterButton = true;

            } else if (buttonPressed == "Bid Two") {

                System.out.println("Team Two Bidding");
                team = false;
                afterButton = true;

            }

        }


    }
    
    public static void main(String[] args){

        // Construct and Run
        new RookGUI();

    }

}
