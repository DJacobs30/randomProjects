import com.pi4j.io.gpio.GpioController;
import com.pi4j.io.gpio.GpioFactory;
import com.pi4j.io.gpio.GpioPinDigitalOutput;
import com.pi4j.io.gpio.GpioPinDigitalMultipurpose;
import com.pi4j.io.gpio.GpioPinDigitalInput;
import com.pi4j.io.gpio.PinMode;
import com.pi4j.io.gpio.PinState;
import com.pi4j.io.gpio.RaspiPin;
import com.pi4j.io.gpio.event.GpioPinDigitalStateChangeEvent;
import com.pi4j.io.gpio.event.GpioPinListenerDigital;
import com.pi4j.io.gpio.PinPullResistance;
import java.util.HashMap;

public class findLight {

    // Instance Variables
    private GpioController gpio;
    private GpioPinDigitalOutput[] step1;
    private GpioPinDigitalOutput[] step2;
	private HashMap driveLogic;
	private Boolean go = false;

	private GpioPinDigitalOutput adcCS;
	private GpioPinDigitalOutput adcCLK;
	private GpioPinDigitalMultipurpose adcDIO;
    
    // Constructer
    public findLight() {

        gpio = GpioFactory.getInstance();
        initGpio();
		initSearch();

    }

    // Initialize GPIO pinouts and drive logic
    private void initGpio() {

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

		// ADC Pins
		adcCS = gpio.provisionDigitalOutputPin(RaspiPin.GPIO_00, "Chip Select");
		adcCLK = gpio.provisionDigitalOutputPin(RaspiPin.GPIO_01, "Clock");
		adcDIO = gpio.provisionDigitalMultipurposePin(RaspiPin.GPIO_02, "Input/Output", PinMode.DIGITAL_OUTPUT);

		// Set Shutdown Options
		stepA.setShutdownOptions(true, PinState.LOW, PinPullResistance.PULL_DOWN);
		stepB.setShutdownOptions(true, PinState.LOW, PinPullResistance.PULL_DOWN);
		stepC.setShutdownOptions(true, PinState.LOW, PinPullResistance.PULL_DOWN);
		stepD.setShutdownOptions(true, PinState.LOW, PinPullResistance.PULL_DOWN);

		stepE.setShutdownOptions(true, PinState.LOW, PinPullResistance.PULL_DOWN);
		stepF.setShutdownOptions(true, PinState.LOW, PinPullResistance.PULL_DOWN);
		stepG.setShutdownOptions(true, PinState.LOW, PinPullResistance.PULL_DOWN);
		stepH.setShutdownOptions(true, PinState.LOW, PinPullResistance.PULL_DOWN);
		
		// Organize the Pins into Lists
		step1 = new GpioPinDigitalOutput[]{stepA, stepB, stepC, stepD};
		step2 = new GpioPinDigitalOutput[]{stepE, stepF, stepG, stepH};
		
		initDriveLogic();
		
	}

    private void initDriveLogic() {
		
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

    private void turnStep(GpioPinDigitalOutput[] stepper, int revolutions, Boolean reverse) throws InterruptedException {
		
		// Method to turn a stepper motor

		for (int n = 1; n < revolutions; n++) {

			if (reverse) {
				
				for (int i = driveLogic.size() - 1; i > 0; i--) {

					String grayCode = (String) driveLogic.get(i);
					setPin(stepper[0], grayCode.charAt(0));
					setPin(stepper[1], grayCode.charAt(1));
					setPin(stepper[2], grayCode.charAt(2));
					setPin(stepper[3], grayCode.charAt(3));

					Thread.sleep(1);

				}

			} else {

				for (int i = 1; i < driveLogic.size(); i++) {

					String grayCode = (String) driveLogic.get(i);
					setPin(stepper[0], grayCode.charAt(0));
					setPin(stepper[1], grayCode.charAt(1));
					setPin(stepper[2], grayCode.charAt(2));
					setPin(stepper[3], grayCode.charAt(3));

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

	private short getADCResult(int channel) {

		short dat1 = 0, dat2 = 0;
        long delay = 2;

        // Prepare ACD_DIO for MUX addess configuration 
        adcDIO.setMode(PinMode.DIGITAL_OUTPUT);
        
        // Start converstaion        
        adcCS.low();

        // MUX Start bit to setup MUX address (Multiplexer configuration)
        adcCLK.low();
        adcDIO.high();
        adcCLK.high();

        // MUX SGL/-DIF git to setup Sigle-Ended channel type
        adcCLK.low();
        adcDIO.high();
        adcCLK.high();

        // MUX ODD/SIGN bit to setup
        adcCLK.low();
        if(channel==0){
            adcDIO.low();  // analog input in Channel #0
        }else{
            adcDIO.high();  // analog input in Channel #1
        }
        adcCLK.high();

        // Keep the clock going to settle the MUX address
        adcCLK.low();

        // Read MSB byte
        adcDIO.setMode(PinMode.DIGITAL_INPUT);
        for (byte i = 0; i < 8; i++) {
            adcCLK.high();
            adcCLK.low();
            dat1 = (short) ((dat1 << 1) | adcDIO.getState().getValue());
        }
        // Read LSB byte
        for (byte i = 0; i < 8; i++) {
            dat2 = (short) (dat2 | (adcDIO.getState().getValue() << i));
            adcCLK.high();
            adcCLK.low();
        }
        // End of conversation.
        adcCS.high();

        //If valid reading MSF == LSF
        return dat1 == dat2 ? dat1 : 0;

	}

	public static int findIndex(double arr[], double t)
 {

     // if array is Null
     if (arr == null) {
         return -1;
     }

     // find length of array
     int len = arr.length;
     int i = 0;

     // traverse in the array
     while (i < len) {

         // if the i-th element is t
         // then return the index
         if (arr[i] == t) {
             return i;
         }
         else {
             i = i + 1;
         }
     }
     return -1;
 }
 
 public static double[] addX(int n, double arr[], double x)
    {
        int i;
  
        // create a new array of size n+1
        double newarr[] = new double[n + 1];
  
        // insert the elements from
        // the old array into the new array
        // insert all elements till n
        // then insert x at n+1
        for (i = 0; i < n; i++)
            newarr[i] = arr[i];
  
        newarr[n] = x;
  
        return newarr;
    }

	private void initSearch() {

		try{

		double[] lightValues = new double[]{};
		double illuminance;
		double maxLight = 0;

		for (int i = 0; i < 10; i++) {

			illuminance = 255.84 * Math.pow(getADCResult(1), -10d/9d);
			if (i == 0) { maxLight = illuminance; }
			if (illuminance > maxLight) { maxLight = illuminance; }
			lightValues = addX(lightValues.length, lightValues, illuminance);
			turnStep(step1, 8, false);
			Thread.sleep(500);

		}

		int maxPos = findIndex(lightValues, maxLight);

		int stepBack = 80 - (maxPos * 8);
		turnStep(step1, maxPos, true);
		
		for (double lightValue : lightValues) {
			//System.out.println(lightValue);
		}
		
		System.out.println(maxLight);
		
		} catch (Exception e) {System.out.println(e); }

	}

    public static void main(String[] args) throws InterruptedException{

        findLight active = new findLight();

        active.turnStep(active.step1, 64, false);
        active.turnStep(active.step1, 64, true);
        active.turnStep(active.step2, 64, false);
        active.turnStep(active.step2, 64, true);

        active.gpio.shutdown();

    }

}