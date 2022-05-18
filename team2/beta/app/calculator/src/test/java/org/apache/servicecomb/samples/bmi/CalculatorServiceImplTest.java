package org.apache.servicecomb.samples.bmi;
import org.junit.Test;
import static org.junit.Assert.assertEquals;

// the unit test cannot be recognized by "mvn clean package"
public class CalculatorServiceImplTest {
    private final CalculatorService calculatorService = new CalculatorServiceImpl();
    @Test
    public void testCalculator() {
        double bmi = calculatorService.calculate(165.0d, 50.0d);
        System.out.println(bmi);
        assertEquals("Calculate Wrongly", bmi, 18.4d, 0);
    }
}
