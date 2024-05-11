#include <WiFi.h>
#include <WiFiClient.h>

const char *ssid = "motorola edge 30_7688";     // Nombre de la red Wi-Fi
const char *password = "castellanos";           // Contraseña de la red Wi-Fi
const char *server = "192.168.131.41";          // Dirección IP del servidor
const int port = 12345;                         // Puerto del servidor

void setup() {
  Serial.begin(115200);
  delay(1000);

  Serial.println("Conectando a la red Wi-Fi...");
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Conectando...");
  }

  Serial.println("Conexión Wi-Fi establecida");
}

void loop() {
  Serial.println("Enviando mensaje al servidor...");

  // Obtener la dirección IP local del ESP32
  IPAddress localIP = WiFi.localIP();
  String ip = localIP.toString();

  // Mensaje a enviar al servidor (incluye la dirección IP)
  String message = "Mensaje desde ESP32. Ubicación: " + ip;

  // Iniciar la conexión con el servidor
  WiFiClient client;
  if (!client.connect(server, port)) {
    Serial.println("Error al conectar con el servidor");
    delay(5000);
    return;
  }

  // Enviar el mensaje al servidor
  client.println(message);

  // Esperar la respuesta del servidor
  while (client.connected() && !client.available()) {
    delay(100);
  }
  // Leer la respuesta del servidor (si la hay)
  String response = client.readString();
  Serial.println("Respuesta del servidor: " + response);

  // Cerrar la conexión con el servidor
  client.stop();

  // Esperar un tiempo antes de enviar el siguiente mensaje
  delay(5000);
}
