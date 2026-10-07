#    #########      ###         ###      #########      #########         ###############
# ###               ######   ######   ###         ###   ###      ###      ###
# ###               ###   ###   ###   ###         ###   ###         ###   ###
#    #########      ###   ###   ###   ###         ###   ###         ###   ############
#             ###   ###         ###   ###         ###   ###         ###   ###
#             ###   ###         ###   ###         ###   ###      ###      ###
# ############      ###         ###      #########      #########         ###############
#
# -------------------- "Guillaume Henrion aka [GYOMH]" "09/07/2026" --------------------

# __________________________________________ ___________________________________________
# |                                       | |                                         |
# |    NOUVELLE SCENE                     | | Cree une Scene prete a l'emploi :       |
# |       V1.0                            | | - Main Timeline (TimelineCue)           |
# |                                       | | - 3 banks (Parameters/Animations/Links) |
# |_______________________________________| | - 1 Compo enfant                        |
# |    Instructions :                     | | - Nom auto : Scene 1, Scene 2, ...      |
# | 1- Launch Mode = Manual               | |                                         |
# | 2- Execute (ou glisser dans un slot   | | Declenchable depuis le Script "bridge"  |
# |    du bridge, puis Chataigne)         | | (slot) via Chataigne / Stream Deck.     |
# |_______________________________________| |_________________________________________|
#
# HISTORIQUE
# V1.0 - 30/09/2026 - Version initiale : extrait de smode_bridge.py
#                      (create_scene_scaffold), verifie sur Smode Compose R15.
#

existing = [str(l.label) for l in script.project.masterScene.layers if l.getOilClassName() == "Scene"]
n = 1
while f"Scene {n}" in existing:
    n += 1
label = f"Scene {n}"

new_scene = Oil.createObject("Scene")
new_scene.label = label

new_scene.mainAnimation = Oil.createObject("TimelineCue")

new_scene.tools.append(Oil.createObject("ParameterBank"))
new_scene.tools.append(Oil.createObject("AnimationBank"))
new_scene.tools.append(Oil.createObject("LinkBank"))

compo = Oil.createObject("Compo")
compoLayer = Oil.createObject("TextureLayer")
compoLayer.generator = compo
compoLayer.label = "Compo"
new_scene.layers.append(compoLayer)

script.project.masterScene.layers.append(new_scene)
print(f"[nouvelle_scene] {label} creee")
