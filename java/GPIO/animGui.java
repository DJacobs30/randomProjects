// GUI Imports
import javax.swing.*;
import javax.imageio.ImageIO;
import java.io.File;
import java.io.IOException;
import java.awt.*;
import java.awt.event.*;
import java.awt.image.BufferedImage;

// Audio Imports
import java.util.Scanner; 
import javax.sound.sampled.AudioInputStream; 
import javax.sound.sampled.AudioSystem; 
import javax.sound.sampled.Clip; 
import javax.sound.sampled.LineUnavailableException; 
import javax.sound.sampled.UnsupportedAudioFileException; 

// GPIO Imports
import com.pi4j.io.gpio.GpioController;
import com.pi4j.io.gpio.GpioFactory;
import com.pi4j.io.gpio.GpioPinDigitalOutput;
import com.pi4j.io.gpio.GpioPinDigitalInput;
import com.pi4j.io.gpio.PinState;
import com.pi4j.io.gpio.RaspiPin;
import com.pi4j.io.gpio.event.GpioPinDigitalStateChangeEvent;
import com.pi4j.io.gpio.event.GpioPinListenerDigital;
import com.pi4j.io.gpio.PinPullResistance;
import java.util.HashMap;

public class GUI extends JFrame implements ActionListener, ItemListener, GpioPinListenerDigital {
	
	// Create Instance variables for the GUI
	private JLabel Title;
	private JButton MainSequence;
	private JButton MoveRover;
	private JButton TurnHead;
	private JButton BlinkLED;
	private JLabel img1;
	private JLabel img2;
	private JLabel img3;
	private JButton whitespace;
	private JComboBox SoundList;
	
	// Create Instance Variables for the Audio
	private Clip clip;
	private AudioInputStream audioInputStream;
	
	// Create Instance Variables for GPIO
	private GpioPinDigitalOutput[] step1;
	private GpioPinDigitalOutput[] step2;
	private GpioPinDigitalOutput[] leds;
	private GpioPinDigitalInput ir;
	private GpioController gpio;
	private HashMap driveLogic;
	private Boolean go = false;
	
	
	// CONSTRUCT CLASS
	
	
	public GUI() {
		// Set the window title
		super(" Animatronics Graphical User Interface");
		
		GpioController gpioc = GpioFactory.getInstance();
		gpio = gpioc;
		
		initGUI();
		initGPIO();
		
	}
	
	private void initGUI() {
		
		// Create the buttons and labels
		initComponents();
		
		// Set the bounds of the GUI
		setSize(1000, 800);
		setExtendedState(JFrame.MAXIMIZED_BOTH);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setVisible(true);
		
		// Set the shutdown actions
		addWindowListener(new WindowAdapter() {
			public void windowClosing(WindowEvent e) {
				
                System.out.println("Closed");
                gpio.shutdown();
                
        }});
		
	}
	
	private void initGPIO() {
		
		// INITIALIZE THE GPIO
		System.out.println(" Setting Up GPIO Pins ");
		
		// Stepper 1
		GpioPinDigitalOutput stepA = gpio.provisionDigitalOutputPin(RaspiPin.GPIO_22, "Step Pin A", PinState.LOW);
		GpioPinDigitalOutput stepB = gpio.provisionDigitalOutputPin(RaspiPin.GPIO_23, "Step Pin B", PinState.LOW);
		GpioPinDigitalOutput stepC = gpio.provisionDigitalOutputPin(RaspiPin.GPIO_24, "Step Pin C", PinState.LOW);
		GpioPinDigitalOutput stepD = gpio.provisionDigitalOutputPin(RaspiPin.GPIO_25, "Step Pin D", PinState.LOW);
		
		// Stepper 2
		GpioPinDigitalOutput stepE = gpio.provisionDigitalOutputPin(RaspiPin.GPIO_26, "Step Pin E", PinState.LOW);
		GpioPinDigitalOutput stepF = gpio.provisionDigitalOutputPin(RaspiPin.GPIO_27, "Step Pin F", PinState.LOW);
		GpioPinDigitalOutput stepG = gpio.provisionDigitalOutputPin(RaspiPin.GPIO_28, "Step Pin G", PinState.LOW);
		GpioPinDigitalOutput stepH = gpio.provisionDigitalOutputPin(RaspiPin.GPIO_29, "Step Pin H", PinState.LOW);
		
		// LEDS
		GpioPinDigitalOutput rPin = gpio.provisionDigitalOutputPin(RaspiPin.GPIO_04, "Red LED", PinState.LOW);
		GpioPinDigitalOutput gPin = gpio.provisionDigitalOutputPin(RaspiPin.GPIO_05, "Green LED", PinState.LOW);
		
		// IR Stuffs
		GpioPinDigitalOutput irE = gpio.provisionDigitalOutputPin(RaspiPin.GPIO_10, "IR Emmitor", PinState.LOW);
		GpioPinDigitalInput irR = gpio.provisionDigitalInputPin(RaspiPin.GPIO_21);
		irR.setDebounce(50);
		irR.addListener(this);
		
		// Turn on the Infared LED
		irE.high();
		
		// Set Shutdown Options
		stepA.setShutdownOptions(true, PinState.LOW, PinPullResistance.PULL_DOWN);
		stepB.setShutdownOptions(true, PinState.LOW, PinPullResistance.PULL_DOWN);
		stepC.setShutdownOptions(true, PinState.LOW, PinPullResistance.PULL_DOWN);
		stepD.setShutdownOptions(true, PinState.LOW, PinPullResistance.PULL_DOWN);
		stepE.setShutdownOptions(true, PinState.LOW, PinPullResistance.PULL_DOWN);
		stepF.setShutdownOptions(true, PinState.LOW, PinPullResistance.PULL_DOWN);
		stepG.setShutdownOptions(true, PinState.LOW, PinPullResistance.PULL_DOWN);
		stepH.setShutdownOptions(true, PinState.LOW, PinPullResistance.PULL_DOWN);
		rPin.setShutdownOptions(true, PinState.LOW, PinPullResistance.PULL_DOWN);
		gPin.setShutdownOptions(true, PinState.LOW, PinPullResistance.PULL_DOWN);
		irE.setShutdownOptions(true, PinState.LOW, PinPullResistance.PULL_DOWN);
		irR.setShutdownOptions(true, PinState.LOW);
		
		// Organize the Pins into Lists
		step1 = new GpioPinDigitalOutput[]{stepA, stepB, stepC, stepD};
		step2 = new GpioPinDigitalOutput[]{stepE, stepF, stepG, stepH};
		leds = new GpioPinDigitalOutput[]{rPin, gPin, irE};
		
		initDriveLogic();
		
	}
	
	
	// GUI BUILDING
	
	
	private ImageIcon bufferImage(int i) {
		
		ImageIcon icon = null;
		
		try {
			
			BufferedImage img = ImageIO.read(new File(
					"/home/pi/animCode2021/GUI/images/image" + i + ".jpg"));
			icon = new ImageIcon(img);
		
		} catch (Exception e) { System.out.println("Image Error"); }
		
		return icon;
		
	}
	
	private void initComponents() {
		
		// Add info to the buttons and labels
		Title = new JLabel("Martian Rover");
		MainSequence = new JButton("Main Sequence");
		MoveRover = new JButton("Move Rover");
		TurnHead = new JButton("Turn Head");
		BlinkLED = new JButton("Blink LED");
		whitespace = new JButton("");
		
		// Buffer the images
		img1 = new JLabel(bufferImage(1));
		img2 = new JLabel(bufferImage(2));
		img3 = new JLabel(bufferImage(3));
		
		// Make the Combo Box
		String[] sounds = 
			{"Command Recieved", "Error!", "Movement", "Friendly Greeting", "Goodbye"};
		SoundList = new JComboBox(sounds);
		
		// Extra Layout Specifications
		Title.setHorizontalAlignment(JLabel.CENTER);
		img1.setVerticalAlignment(JLabel.BOTTOM);
		img3.setVerticalAlignment(JLabel.TOP);
		
		// Format the buttons
		setLayout(new GridLayout(5, 2));
		
		// Add the widgets to the GUI
		add(Title);
		add(MainSequence);
		add(img1);
		add(MoveRover);
		add(img2);
		add(TurnHead);
		add(img3);
		add(BlinkLED);
		add(whitespace);
		add(SoundList);
		
		// Create the listeners for each button
		MainSequence.addActionListener(this);
		MoveRover.addActionListener(this);
		TurnHead.addActionListener(this);
		BlinkLED.addActionListener(this);
		SoundList.addItemListener(this);
		
	}
	
	
	// LISTENERS
	
	
	public void actionPerformed(ActionEvent e) {
		
		String button = e.getActionCommand();
		System.out.println(button);
		
		try {
		
		if (button == "Main Sequence") {
			
			setupSound("/home/pi/animCode2021/GUI/sounds/sound5.wav");
			clip.start();
			
			changeLED(1, 0, false, false);
			turnHead();
			move(2048, true);
			LEDOff();
			changeLED(0, 3, true, true);
			turnHead();
			changeLED(1, 0, false, false);
			move(2048, false);
			turnHead();
			LEDOff();
			
		} else if (button == "Move Rover") {
			
			setupSound("/home/pi/animCode2021/GUI/sounds/sound5.wav");
			clip.start();
			
			move(2048, true);
			move(2048, false);
			
		} else if (button == "Turn Head") {
			
			turnHead();
			
		} else if (button == "Blink LED") {
			
			setupSound("/home/pi/animCode2021/GUI/sounds/sound5.wav");
			clip.start();
			
			changeLED(1, 2000, false, true);
			
			changeLED(0, 3, true, false);
			
		}
		
		} catch (Exception exe) { System.out.println(exe); }
		
	}
	
	public void itemStateChanged(ItemEvent e) {
		
		if (e.getStateChange() == ItemEvent.SELECTED) {
		
			Object item = e.getItem();
			System.out.println(item);
			
			if (item == "Command Recieved") {
				
				setupSound("/home/pi/animCode2021/GUI/sounds/sound5.wav");
				clip.start();
				
			} else if (item == "Error!") {
				
				try {
				setupSound("/home/pi/animCode2021/GUI/sounds/sound2.wav");
				clip.start();
				Thread.sleep(1000);
				clip.setFramePosition(0);
				clip.start();
				Thread.sleep(1000);
				clip.setFramePosition(0);
				clip.start();
				} catch (Exception ex) { System.out.println("How did we get here?"); }
				
			} else if (item == "Movement") {
				
				setupSound("/home/pi/animCode2021/GUI/sounds/sound3.wav");
				clip.start();
				
			} else if (item == "Friendly Greeting") {
				
				setupSound("/home/pi/animCode2021/GUI/sounds/sound4.wav");
				clip.start();
				
			} else if (item == "Goodbye") {
				
				setupSound("/home/pi/animCode2021/GUI/sounds/sound1.wav");
				clip.start();
				
			}
		
		}
	
	}
	
	public void handleGpioPinDigitalStateChangeEvent(GpioPinDigitalStateChangeEvent event) {

		if(event.getState().isLow()) {

			System.out.println(" INPUT RECIEVED ");
			go = true;

		}

	}
	
	
	// SOUND PLAYING
	

	public void setupSound(String path) {

		try {
		
			// Create Audio Input Object
			audioInputStream = AudioSystem.getAudioInputStream(new File(path));
			
			// Create Clip Reference
			clip = AudioSystem.getClip();
			
			// Open AudioInputStream to the clip
			clip.open(audioInputStream);
			
		} catch (Exception e) { System.out.println("Audio Player Error"); }
			
	}


	// GPIO METHODS
	
	
	public void initDriveLogic() {
		
		// Setting Up Drive Logic
		
		driveLogic = new HashMap();

		driveLogic.put(0, "1001");
		driveLogic.put(1, "0001");
		driveLogic.put(2, "0011");
		driveLogic.put(3, "0010");
		driveLogic.put(4, "0110");
		driveLogic.put(5, "0100");
		driveLogic.put(6, "1100");
		driveLogic.put(7, "1000");
		
	}
			
	public void turnStep(GpioPinDigitalOutput[][] steppers, int revolutions, Boolean reverse) throws InterruptedException {
		
		// Method to turn a stepper motor

		for (int n = 1; n < revolutions; n++) {

			if (reverse) {
				
				for (int i = driveLogic.size() - 1; i > 0; i--) {

					for (GpioPinDigitalOutput[] stepper : steppers) {
	
						String grayCode = (String) driveLogic.get(i);
						setPin(stepper[0], grayCode.charAt(0));
						setPin(stepper[1], grayCode.charAt(1));
						setPin(stepper[2], grayCode.charAt(2));
						setPin(stepper[3], grayCode.charAt(3));
	
					}

					Thread.sleep(1);

				}

			} else {

				for (int i = 1; i < driveLogic.size(); i++) {

					for (GpioPinDigitalOutput[] stepper : steppers) {
	
						String grayCode = (String) driveLogic.get(i);
						setPin(stepper[0], grayCode.charAt(0));
						setPin(stepper[1], grayCode.charAt(1));
						setPin(stepper[2], grayCode.charAt(2));
						setPin(stepper[3], grayCode.charAt(3));

					}

					Thread.sleep(1);

				}

			}

		}
		
	}
	
	private void setPin(GpioPinDigitalOutput pin, char value) {

		if (value == '0') {

			pin.low();

		} else {

			pin.high();

		}

	}
	
	
	// SEQUENCE METHODS
	
	
	private void turnHead() throws InterruptedException {

		/*
		 * Turn Head:
		 *  - Move Stepper motor to turn cam
		 *      (might need a wormgear)
		 */

		System.out.println(" Turn Head ");

		// Bring in the Stepper One pins
		GpioPinDigitalOutput[][] steppers = new GpioPinDigitalOutput[][]{step2};

		setupSound("/home/pi/animCode2021/GUI/sounds/sound3.wav");
		clip.start();
		turnStep(steppers, 64, false);
		
		setupSound("/home/pi/animCode2021/GUI/sounds/sound3.wav");
		clip.start();
		turnStep(steppers, 128, true);
		
		setupSound("/home/pi/animCode2021/GUI/sounds/sound3.wav");
		clip.start();
		turnStep(steppers, 64, false);

	}

	private void move(int duration, Boolean reverse) throws InterruptedException {

		/*
		 * Move Forward:
		 *  - Turn both stepper motors in one direction for an arbitrary amount of time
		 *  - Turn both in other direction for same arbitrary time
		 */

		System.out.println(" Move Forward ");

		// Bring in the stepper two and three pins
		GpioPinDigitalOutput[][] stepper = new GpioPinDigitalOutput[][]{step1};
		
		System.out.println(" AFTER STEPPER ");

		turnStep(stepper, duration, reverse);
		
		System.out.println("AFTER TURN STEP");

	}

	private void changeLED(int color, int duration, Boolean blink, Boolean off) throws InterruptedException {

		/*
		 * Change LED:
		 *  - Change the LEDs from green to red flashing to signal warning
		 *  - Blinking green to represent being happy
		 */
	
		System.out.println(" Change LED ");
		
		// Red = 0   Green = 1
		GpioPinDigitalOutput LED = leds[color];

		if (blink == true) {

			for (int i = 0; i < duration; i++) {

				LED.high();
				Thread.sleep(500);
				LED.low();
				Thread.sleep(500);

			}

		} else {

			LED.high();

			if (off == true) {

				Thread.sleep(duration);
				LED.low();

			}

		}

	}

	private void LEDOff() {

		// Turn off both the LEDs
		leds[0].low();
		leds[1].low();

	}



	public static void main(String[] args) {
		
		new GUI();
		
	}

}
