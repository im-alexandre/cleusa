

#include <ESP8266WiFi.h>
#include <PubSubClient.h>

// VARIÁVEIS WIFI

const char* ssid = "SSID";
const char* password = "SENHA";

//VARIÁVEIS MQTT
const char* mqtt_server = "MQTT_BROKER";
const char* mqtt_clientID = "sonoff";
const char* topico = "cleusa/iluminacao";

String LED_PIN = 14
String RELAY_PIN = 12

//Cria instâncias WIFI e MQTT
WiFiClient espClient;
PubSubClient client(espClient);
long lastMsg = 0;
String msg = "";
int value = 0;

void setup_wifi() {
  delay(10);
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}

void monitoraTopico (char* topico, byte* payload, unsigned int length){

  if ((char)payload[0] == '1'){
    digitalWrite(RELAY_PIN, LOW);
  }else if ((char)payload[0] == '0'){
    digitalWrite(RELAY_PIN, HIGH);
  }
}

void conectaMQTT() {
  while (!client.connected()) {
    client.connect(mqtt_clientID);
  }
  client.subscribe(topico);
  Serial.println("conectado ao broker");
}

void setup() {
  Serial.begin(115200);
  pinMode(RELAY_PIN, OUTPUT);
  digitalWrite(RELAY_PIN, HIGH);
  setup_wifi();
  client.setServer(mqtt_server, 1883);
  client.setCallback(monitoraTopico); //Chama a função monitora tópico no client.loop
}

void loop() {

  if (!client.connected()) {
    conectaMQTT();
    digitalWrite(RELAY_PIN, HIGH);
  }
  client.loop();

  }
