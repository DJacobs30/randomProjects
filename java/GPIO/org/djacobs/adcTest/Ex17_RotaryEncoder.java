package org.djacobs.adcTest;

import com.pi4j.io.gpio.GpioController;
import com.pi4j.io.gpio.GpioFactory;
import com.pi4j.io.gpio.GpioPinDigitalInput;
import com.pi4j.io.gpio.PinPullResistance;
import com.pi4j.io.gpio.PinState;
import com.pi4j.io.gpio.RaspiPin;
import com.pi4j.io.gpio.event.GpioPinDigitalStateChangeEvent;
import com.pi4j.io.gpio.event.GpioPinListenerDigital;

/**
 *
 * @author marcandreuf
 */
public class Ex17_RotaryEncoder extends BaseSketch {    
   
    private GpioPinDigitalInput swPin;
    private GpioPinDigitalInput roAPin;
    private GpioPinDigitalInput roBPin;
    private int globalCounter = 0;
    private boolean flag = false;
    private PinState lastRoBStatus;
    private PinState currentRoBStatus=PinState.LOW;
    
    
    /**
     * @param gpio controller 
     */
    public Ex17_RotaryEncoder(GpioController gpio){
        super(gpio);
    }
    
    public static void main(String[] args) throws InterruptedException {
        Ex17_RotaryEncoder sketch = new Ex17_RotaryEncoder(GpioFactory.getInstance());
        sketch.run(args);
    }
    
    @Override
    protected void setup(String[] args) {
        swPin = gpio.provisionDigitalInputPin(RaspiPin.GPIO_00, PinPullResistance.PULL_UP);
        roAPin = gpio.provisionDigitalInputPin(RaspiPin.GPIO_01);
        roBPin = gpio.provisionDigitalInputPin(RaspiPin.GPIO_02);
        swPin.addListener(new GpioPinListenerDigital() {
            @Override
            public void handleGpioPinDigitalStateChangeEvent(GpioPinDigitalStateChangeEvent gpdsce) {
                globalCounter = 0;
            }
        });
        System.out.println("Rotary encoder ready!");        
    }

    @Override
    protected void loop(String[] args) {
        do{
            rotaryDeal();
            System.out.println("counter :"+globalCounter);
        }while(isNotInterrupted);
    }

    private void rotaryDeal() {
       lastRoBStatus = roBPin.getState();
            
        while(roAPin.isLow()){
            currentRoBStatus = roBPin.getState();
            flag=true;
        }
            
        if(flag){
            flag = false;
            if(lastRoBStatus==PinState.LOW && currentRoBStatus==PinState.HIGH){
                globalCounter ++;
            }
            if(lastRoBStatus==PinState.HIGH && currentRoBStatus==PinState.LOW){
                globalCounter --;
            }
        }
    }
}
