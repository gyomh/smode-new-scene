# Smode New Scene

*[Version française](README.fr.md)*

> **Experimental, not an official Smode tool.** Built by trial and error against the Oil API (see [smode-oil-reference](https://github.com/gyomh/smode-oil-reference)). Tested on Smode Compose R15.

A tiny Script that adds a **ready-to-use Scene** to the project: a *Main Timeline* (`TimelineCue`), three banks
(Parameters / Animations / Links) and a child Compo, named automatically (*Scene 1*, *Scene 2*...).

It is meant to be triggered from a control surface (Chataigne, Stream Deck) through
[smode-server-http](https://github.com/gyomh/smode-server-http).

## Install

1. Drag `nouvelle_scene.py` into your Smode project, **Launch Mode = Manual**.
2. Execute it (or put it in a slot of the HTTP server and call it from Chataigne / a Stream Deck).

## License

MIT — see [LICENSE](LICENSE).
