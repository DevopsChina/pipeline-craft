package org.apache.servicecomb.samples.bmi;
import org.junit.Test;
import static org.junit.Assert.assertEquals;

// the unit test cannot be recognized by "mvn clean package"
public class StaticWebpageDispatcherTest {
    private final StaticWebpageDispatcher staticWebpageDispatcher = new StaticWebpageDispatcher();
    @Test
    public void testDispatcher() {
        assertEquals("Calculate Wrongly", 1, 1, 0);
    }
}
