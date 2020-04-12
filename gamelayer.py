import random

from cocos.director import director
from cocos.scenes.transitions import SplitColsTransition, FadeTransition
import cocos.layer
import cocos.scene
import cocos.text
import cocos.actions as ac
import cocos.collision_model as cm

import actors
import mainmenu
from scenario import get_scenario


def game_over():
    w, h = director.get_window_size()
    layer = cocos.layer.Layer()
    text = cocos.text.Label('Gane Over', position=(w*0.5, h*0.5),
                            font_name='Oswald', font_size=72,
                            anchor_x='center', anchor_y='center')
    layer.add(text)
    scene = cocos.scene.Scene(layer)
    new_scene = FadeTransition(mainmenu.new_menu())
    func = lambda: director.replace(new_scene)
    scene.do(ac.Delay(3) + ac.CallFunc(func))
    return scene