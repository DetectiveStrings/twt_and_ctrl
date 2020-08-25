#include<WiFi.h>

char ssid[] = "WIFI_NAME";
char pass[] = "WIFI_password"  ; 


  int fric = 5000 ; 
  int cha1 = 0 ; 
  int cha2 = 1 ; 
  int reslution = 8 ; 
  int x = 0 , y = 0 ;

void set_led() ; 
void test1() ; 
void test2() ; 
  

WiFiServer server(1337);

void setup() {
  set_led();
  Serial.begin(115200) ; 
  WiFi.disconnect();
  WiFi.disconnect();
  delay(5000);
  Serial.println("") ; 
  Serial.println("connectin to ") ; 
  WiFi.begin(ssid,pass);
  while(WiFi.status() != WL_CONNECTED){
    Serial.print(".");
    delay(300);
  }
  Serial.println("connected ");
  Serial.println("IP Address : ");
  Serial.println(WiFi.localIP()) ; 
  server.begin();
}

void loop() {
  WiFiClient client = server.available();
  if(!client){return ; }
  while(!client.available()){delay(1);}
  char string[256];
  String xxx = (client.readString());
  if(xxx[1] == 's' ) {
    test1() ; 
  }
  else if (xxx[1] == 'y'){

    test2() ; 
  }
  Serial.println(xxx[1]);
  client.stop();
}

void test1(){
if(x){
  ledcWrite(cha1 , 0 ) ;
  x = 0 ; 
  }
  else{
ledcWrite(cha1 , 255 ) ;
    x = 1 ; 
  }
  }

void test2(){
if(y){
  ledcWrite(cha2 , 0 ) ;
  y= 0 ; 
  }
  else{
ledcWrite(cha2 , 255 ) ;
    y = 1 ; 
  }
  }

  void set_led(){
 
 ledcSetup(cha1 , fric , reslution);
 ledcAttachPin(2 , cha1); 
 ledcSetup(cha2 , fric , reslution);
 ledcAttachPin(27 , cha2);  
 

  }
