package org.djacobs.adcTest;

import com.pi4j.io.gpio.GpioController;
import com.pi4j.io.gpio.GpioFactory;
import com.pi4j.io.gpio.PinMode;

/**
 *
 * In this example we use type 'short'. In JAVA the type 'byte' is signed and
 * the values go from -128 to 127. There is no unsigned 'byte' type in JAVA. The
 * next numeric type is 'short', which is a 16-bit integer. 
 * Documentation about the Hall effect and the ADC0832CCN
 * 
 * Hall effect sensing and application by Honeywell
 * http://sensing.honeywell.com/index.php?ci_id=47847
 * 
 * Hall effect sensor 44E datasheet
 * http://www.allegromicro.com/~/media/Files/Datasheets/A3141-2-3-4-Datasheet.ashx
 * 
 * ADC0832 datasheet
 * http://pdf1.alldatasheet.com/datasheet-pdf/view/158145/NSC/ADC0832CCN.html
 *
 * @author marcandreuf
 */
public class Ex02_03_LinearHall extends ADC_Base {
    private short intensity;

    /**
     * @param gpio controller
     */
    public Ex02_03_LinearHall(GpioController gpio) {
        super(gpio);
    }

    public static void main(String[] args) throws InterruptedException {
        Ex02_03_LinearHall sketch = new Ex02_03_LinearHall(GpioFactory.getInstance());
        sketch.run(args);
    }

    @Override
    protected void setup(String[] args) {
        super.setup(args);
        System.out.println("Linear Hall sensor ready!");
    }

    @Override
    protected void loop(String[] args) {
        short analogVal;
        do {
            analogVal = get_ADC_Result();
            intensity = (short) (210 - analogVal);
            System.out.println("Current intensity of magnetic field: " + Integer.valueOf(intensity));
            delayMilliseconds(500);
        } while (isNotInterrupted);
    }
    
    public short getIntensity() {
        return intensity;
    }
}
