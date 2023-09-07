#BOUNCEGUI

import g2d
from MOON_PATROL_GAME import MPgame


class MPGui:
    def __init__(self):
        self._game = MPgame()
        g2d.init_canvas(self._game.arena().size())
        self._im = g2d.load_image("moon-patrol.png")
        self._imbg = g2d.load_image("moon-patrol-bg.png")
        self._go = g2d.load_image("game_over.png")
        self._yw = g2d.load_image("you_win.png")
        g2d.main_loop(self.tick)
        
    def handle_keyboard(self):
        hero = self._game.hero()
        if g2d.key_pressed("ArrowUp"):
            hero.jump()
        elif g2d.key_pressed("ArrowRight"):
            hero.go_right()
        elif g2d.key_pressed("ArrowDown"):
            hero.go_down()
        elif g2d.key_pressed("ArrowLeft"):
            hero.go_left()
        elif (g2d.key_released("ArrowUp") or
              g2d.key_released("ArrowRight") or
              g2d.key_released("ArrowDown") or
              g2d.key_released("ArrowLeft")):
            hero.stay()
        elif g2d.key_pressed("Spacebar"):
            hero.shoot()
    
    def tick(self):
        self.handle_keyboard()
        arena = self._game.arena()
        
        arena.move_all()  # Game logic
        arena.move_bg()
        
        g2d.clear_canvas()
        
        for b in arena.backgrounds():
            g2d.draw_image_clip(self._imbg, b.symbol(), b.position())
            
        for a in arena.actors():
            if a.symbol() != (0, 0, 0, 0):
                g2d.draw_image_clip(self._im, a.symbol(), a.position())
            else:
                g2d.fill_rect(a.position())
        lives = "Lives: " + str(self._game.hero().lives())
        toplay = "Time: " + str(self._game.remaining_time())
        g2d.draw_text(lives + " " + toplay, (0, 0), 24)

        if self._game.game_over():
            g2d.draw_image_clip(self._go,(0,0,640,360), (0,0,516,256))
            g2d.draw_text("(PRESS SPACEBAR TO CLOSE OR ENTER TO RESTART)", (120,220), 10)
            if g2d.key_pressed("Spacebar"):
                g2d.close_canvas()
            elif g2d.key_pressed("Enter"):
                gui = MPGui()
            
        elif self._game.game_won():
            g2d.draw_image_clip(self._yw,(0,0,608,342), (0,0,516,256))
            g2d.draw_text("(PRESS SPACEBAR TO CLOSE OR ENTER TO RESTART)", (120,220), 10)
            if g2d.key_pressed("Spacebar"):
                g2d.close_canvas()
            elif g2d.key_pressed("Enter"):
                gui = MPGui()
gui = MPGui()
