package org.djacobs.adcTest;

import com.pi4j.io.gpio.GpioController;
import com.pi4j.io.gpio.GpioFactory;
import com.pi4j.io.gpio.GpioPinDigitalInput;
import com.pi4j.io.gpio.PinPullResistance;
import com.pi4j.io.gpio.RaspiPin;

public class Ex27_JoyStickPS2 extends ADC_Base {    
   
    private GpioPinDigitalInput joyStick_Z;
    
    public Ex27_JoyStickPS2(GpioController gpio){
        super(gpio);
    }
    
    public static void main(String[] args) throws InterruptedException {
		
		long start = System.currentTimeMillis();
        Thread.sleep(0, 2);
        long end = System.currentTimeMillis();
        System.out.println(end - start);
		
        Ex27_JoyStickPS2 sketch = new Ex27_JoyStickPS2(GpioFactory.getInstance());
        sketch.run(args);
    }
    
    @Override
    protected void setup(String[] args) {
        super.setup(args);
        joyStick_Z = gpio.provisionDigitalInputPin(RaspiPin.GPIO_03);
        joyStick_Z.setPullResistance(PinPullResistance.PULL_UP);
        System.out.println("Joystick ready!");        
    }

    @Override
    protected void loop(String[] args) {
        int tmp = 0;
        int channelX=0, channelY=1;
        short xVal=0, yVal=0, zVal=0;
        double illuminance;
        
        System.out.println("Entering Loop");
        
        do{
            xVal = get_ADC_Result(channelX);
            yVal = get_ADC_Result(channelY);
            //zVal = (short) joyStick_Z.getState().getValue();
            
            //System.out.println(xVal + ", " + yVal + ", " + (zVal == 0 ? "Pressed" : "Not Pressed"));
            illuminance = 255.84 * Math.pow(yVal, -10d/9d);
            System.out.println(illuminance);
            delayMilliseconds(50);
            
            /*
            tmp++;
            if (tmp % 100 == 0) {
				System.out.println("here" + System.currentTimeMillis());
			}
            
            if(xVal == 0){
                tmp = 1; //up	
            }
            if(xVal == 255){
                tmp = 2; //down
            }

            
            if(yVal == 0){
                tmp = 3; //right
            }
            if(yVal == 255){
                tmp = 4; //left
            }

            
            if(zVal == 0){
                //System.out.println("Button is pressed!");
            }
            */
            
			
			/*				   
            switch(tmp){
				case 0: System.out.println("neutral"); break;
                case 1: System.out.println("up"); break;
                case 2: System.out.println("down"); break;
                case 3: System.out.println("right"); break;
                case 4: System.out.println("left"); break;
                default: break;
            }
            */
            
        }while(isNotInterrupted);
    }
}
