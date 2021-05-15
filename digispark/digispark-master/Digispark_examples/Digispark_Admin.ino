#include <DigiKeyboard.h>
#define KEY_Tab    43

void setup() {
// Parfois nécessaire pour initialiser le clavier
  DigiKeyboard.sendKeyStroke(0);

// On attend deux petites secondes (pour permettre au driver de se charger)
  DigiKeyboard.delay(2000);

// On envoie les identifiants
  DigiKeyboard.print("domaine\\Administrateur");
  DigiKeyboard.sendKeyStroke(KEY_Tab);

  DigiKeyboard.print("Password1");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
}

void loop() {
  DigiKeyboard.delay(10000);
}












