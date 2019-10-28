/*
Java DO NOT HAVE multiple inheritance
No MRO characteristic
*/
import java.lang.System.*;

class Robot
{
    public void move_forward()
    {
        System.out.println("Physical Movement! Moving forward");
    }
    public void move_backward()
    {
        System.out.println("Physical Movement! Moving backward");
    }
};

class CleaningRobot extends Robot
{
    public void clean(int times)
    {
        for(int i=0; i<times; i++)
        {
            super.move_forward();
            super.move_backward();
        }
    }
};

class MockBot extends Robot
{
    public void move_forward()
    {
        System.out.println("forward");
    }
    public void move_backward()
    {
        System.out.println("backward");
    }
};

/*
class MockCleaningRobot extends CleaningRobot, MockBot
{
};
*/

public class MainClazz
{
    public static void main(String args[])
    {
        //MockCleaningRobot bot = new MockCleaningRobot();
        CleaningRobot bot = new CleaningRobot();
        bot.clean(10);
    }
}