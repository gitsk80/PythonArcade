import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sokoban Grundgerüst"

# Größe eines Gitterfelds in Pixeln
GRID_SIZE = 64

# Spielergeschwindigkeit (ein Feld pro Bewegung)
MOVEMENT_SPEED = GRID_SIZE


class SokobanGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        arcade.set_background_color(arcade.color.LIGHT_GRAY)

        # Spieler-Attribute
        self.player_sprite = None
        self.player_list = None

        # Bewegungsrichtung speichern
        self.movement_x = 0
        self.movement_y = 0

    def setup(self):
        """ Spiel initialisieren """
        # Sprite-Liste erstellen
        self.player_list = arcade.SpriteList()

        # Spieler erstellen (vorläufig als blaues Quadrat)
        self.player_sprite = arcade.SpriteSolidColor(GRID_SIZE, GRID_SIZE, arcade.color.BLUE)

        # Startposition des Spielers (Mitte des Bildschirms)
        self.player_sprite.center_x = 0 + GRID_SIZE / 2
        self.player_sprite.center_y = 0 + GRID_SIZE / 2

        # Spieler zur Sprite-Liste hinzufügen
        self.player_list.append(self.player_sprite)

    def on_draw(self):
        """ Bildschirm zeichnen """
        self.clear()

        # Gitterlinien zeichnen
        for x in range(0, SCREEN_WIDTH, GRID_SIZE):
            arcade.draw_line(x, 0, x, SCREEN_HEIGHT, arcade.color.BLACK)
        for y in range(0, SCREEN_HEIGHT, GRID_SIZE):
            arcade.draw_line(0, y, SCREEN_WIDTH, y, arcade.color.BLACK)

        # Spieler zeichnen
        self.player_list.draw()

    def on_key_press(self, key, modifiers):
        """ Tastatureingaben verarbeiten """
        if key == arcade.key.UP:
            # Bewege ein Feld nach oben
            self.player_sprite.center_y += MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            # Bewege ein Feld nach unten
            self.player_sprite.center_y -= MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            # Bewege ein Feld nach links
            self.player_sprite.center_x -= MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            # Bewege ein Feld nach rechts
            self.player_sprite.center_x += MOVEMENT_SPEED


def main():
    window = SokobanGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()