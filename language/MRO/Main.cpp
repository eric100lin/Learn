/*
C++ do not have MRO characteristic
*/
#include <stdio.h>
#include <stdlib.h>

class Robot
{
    public:
        virtual void move_forward()
        {
            printf("Physical Movement! Moving forward\n");
        }
        virtual void move_backward()
        {
            printf("Physical Movement! Moving backward\n");
        }
};

class CleaningRobot : public Robot
{
    public:
        void clean(int times)
        {
            for(int i=0; i<times; i++)
            {
                this->move_forward();
                this->move_backward();
            }
        }
};

class MockBot : public Robot
{
    public:
        void move_forward()
        {
            printf("forward\n");
        }
        void move_backward()
        {
            printf("backward\n");
        }
};

class MockCleaningRobot : public CleaningRobot, MockBot
{
};

int main(int argc, char **argv)
{
    MockCleaningRobot mockedBot;
    mockedBot.clean(10);
    return 0;
}