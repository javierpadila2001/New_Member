#calls the funcion MotorController.c over an infite time, so that information can always be updated. I learned we do this every 100ms


while(true)
{
  #update
  MotorController.c(CANID());
  MotosController.c(CANMESSAGE);
}
