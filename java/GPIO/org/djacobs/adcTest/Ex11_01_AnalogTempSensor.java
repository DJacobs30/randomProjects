package org.djacobs.adcTest;

import com.pi4j.io.gpio.GpioController;
import com.pi4j.io.gpio.GpioFactory;

/**
 * This code has been tunner with the NTC thermistor datasheet from Murata.
 * http://www.murata.com/~/media/webrenewal/support/library/catalog/products/thermistor/ntc/r44e.ashx
 * 
 * The sample code has been adjusted from these forums:
 * http://electronics.stackexchange.com/questions/8754/how-to-measure-temperature-using-a-ntc-thermistor
 * 
 * Because we are using an ADC0832 which is a 8 bit IC,
 * the code has been adjusted to a value of 256 instead of 1024.
 * 
 * The sensor its been power at 3.3V and the GND and VCC has been switched, because the label on the
 * board looks like is wrong. Based on this forum http://forum.arduino.cc/index.php/topic,209133.0.html
 * "Temperature sensor module KY-013
 * These modules are the same, they're all on boards labelled "S1". THE PINS ARE MARKED BACKWARDS ON THESE.
 * Has pin 1 (marked S) (GND), pin 2 (5v power) and pin 3 (marked -) (analog signal.)"
 * 
 * @author marcandreuf
 */
public class Ex11_01_AnalogTempSensor extends ADC_Base {
    /**
     * @param gpio controller
     */
    public Ex11_01_AnalogTempSensor(GpioController gpio) {
        super(gpio);
    }

    public static void main(String[] args) throws InterruptedException {
        Ex11_01_AnalogTempSensor sketch = new Ex11_01_AnalogTempSensor(GpioFactory.getInstance());
        sketch.run(args);
    }

    @Override
    protected void setup(String[] args) {
        super.setup(args);
        System.out.println("Analog temp sensor ready!");
    }

    @Override
    protected void loop(String[] args) {        
        do {
            double temp = getTempfromThermister(get_ADC_Result());
            System.out.println("Current temperature: "+temp);
            delayMilliseconds(1000);
        } while (isNotInterrupted);
    }
    
    
    private double getTempfromThermister(double rawADC) {
        double KY_013Resistor = 10000; // For a 10k resistance thermistor.
        // The b_constant value its been extracted from the datasheet for a 
        // 10K thermistor NXRT15XH103FA5B, which is closer sensor I found.
        double b_constant = 3380.0; 
        double t0 = 298; // 273 + 25, constant of the S.Hart equation.
        double celciusAdjustment = 273.15;
        double adc8BitPrecision = 256;
        
        double resisADC = ((adc8BitPrecision / rawADC)-1) * KY_013Resistor;       
        double farenh = b_constant / Math.log(resisADC/(KY_013Resistor*Math.exp(-b_constant/t0)));
        return rawADC;
        //return farenh - celciusAdjustment;
    }
}
