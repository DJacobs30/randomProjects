package org.djacobs.adcTest;

import com.pi4j.io.gpio.GpioController;
import com.pi4j.io.gpio.GpioPinDigitalMultipurpose;
import com.pi4j.io.gpio.GpioPinDigitalOutput;
import com.pi4j.io.gpio.PinMode;
import com.pi4j.io.gpio.RaspiPin;
import static org.djacobs.adcTest.BaseSketch.wiringPiSetup;

/**
 *
 * @author marcandreuf
 */
public abstract class ADC_Base extends BaseSketch {

    protected GpioPinDigitalOutput ADC_CS;
    protected GpioPinDigitalOutput ADC_CLK;
    protected GpioPinDigitalMultipurpose ADC_DIO;

    public ADC_Base(GpioController gpio) {
        super(gpio);
    }

    @Override
    protected void setup(String[] args) {
        wiringPiSetup();
        ADC_CS = gpio.provisionDigitalOutputPin(RaspiPin.GPIO_00);
        ADC_CLK = gpio.provisionDigitalOutputPin(RaspiPin.GPIO_01);
        ADC_DIO = gpio.provisionDigitalMultipurposePin(RaspiPin.GPIO_02, PinMode.DIGITAL_OUTPUT);
    }

    protected short get_ADC_Result() {
        return get_ADC_Result(0);
    }
    
    protected synchronized short get_ADC_Result(int channel) {
        short dat1 = 0, dat2 = 0;
        long delay = 2;

        // Prepare ACD_DIO for MUX addess configuration 
        ADC_DIO.setMode(PinMode.DIGITAL_OUTPUT);
        
        // Start converstaion        
        ADC_CS.low();

        // MUX Start bit to setup MUX address (Multiplexer configuration)
        ADC_CLK.low();
        ADC_DIO.high();
        //long start = System.currentTimeMillis();
        //delayMicrosendos(delay);  // Start bit
        //long end = System.currentTimeMillis();
        //System.out.println(end - start);
        ADC_CLK.high();
        //delayMicrosendos(delay);

        // MUX SGL/-DIF git to setup Sigle-Ended channel type
        ADC_CLK.low();
        ADC_DIO.high();
        //delayMicrosendos(delay);
        ADC_CLK.high();
        //delayMicrosendos(delay);

        // MUX ODD/SIGN bit to setup
        ADC_CLK.low();
        if(channel==0){
            ADC_DIO.low();  // analog input in Channel #0
        }else{
            ADC_DIO.high();  // analog input in Channel #1
        }
        //delayMicrosendos(delay);
        ADC_CLK.high();

        // Keep the clock going to settle the MUX address
        //delayMicrosendos(delay);
        ADC_CLK.low();
        //delayMicrosendos(delay);

        // Read MSB byte
        ADC_DIO.setMode(PinMode.DIGITAL_INPUT);
        for (byte i = 0; i < 8; i++) {
            ADC_CLK.high();
            //delayMicrosendos(delay);
            ADC_CLK.low();
            //delayMicrosendos(delay);
            dat1 = (short) ((dat1 << 1) | ADC_DIO.getState().getValue());
        }
        // Read LSB byte
        for (byte i = 0; i < 8; i++) {
            dat2 = (short) (dat2 | (ADC_DIO.getState().getValue() << i));
            ADC_CLK.high();
            //delayMicrosendos(delay);
            ADC_CLK.low();
            //delayMicrosendos(delay);
        }
        // End of conversation.
        ADC_CS.high();

        //If valid reading MSF == LSF
        return dat1 == dat2 ? dat1 : 0;
    }

}
