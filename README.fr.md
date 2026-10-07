# Smode New Scene

*[English version](README.md)*

> **Expérimental, pas un outil officiel Smode.** Construit par essais et erreurs sur l'API Oil (voir [smode-oil-reference](https://github.com/gyomh/smode-oil-reference)). Testé sur Smode Compose R15.

Un tout petit Script qui ajoute au projet une **Scene prête à l'emploi** : une *Main Timeline* (`TimelineCue`), trois
banks (Parameters / Animations / Links) et une Compo enfant, nommée automatiquement (*Scene 1*, *Scene 2*...).

Il est prévu pour être déclenché depuis une surface de contrôle (Chataigne, Stream Deck) via
[smode-server-http](https://github.com/gyomh/smode-server-http).

## Installation

1. Glissez `nouvelle_scene.py` dans votre projet Smode, **Launch Mode = Manual**.
2. Exécutez-le (ou mettez-le dans un slot du serveur HTTP et appelez-le depuis Chataigne / un Stream Deck).

## Licence

MIT — voir [LICENSE](LICENSE).
