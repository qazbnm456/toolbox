# Toolbox - A Tsaotun's addon that provides useful aliases for you

## **Table of contents**

* [Introduction](#intro)
* [Screenshot](#screenshot)
* [Installation](#install)
* [Contribute](#contribute)
* [LICENSE](#license)

---------------------------------------

<a name="intro"></a>
## Introduction

This repo contains an addon called `toolbox` that provides useful aliases for docker. Besides, this repo also serves as a sample addon extending the power of [Tsaotun](https://github.com/qazbnm456/tsaotun).

You may want to follow the code and write one on your own.

<a name="screenshot"></a>
## Screenshot

- `tsaotun version --client`:

    <img src="http://i.imgur.com/bndEkbo.png" width="540">

- `tsaotun container rm --clear`:

    <img src="http://i.imgur.com/lzBeefr.png" width="540">

- `tsaotun toolbox`:

    <img src="http://i.imgur.com/P3TuZpt.png" width="540">

<a name="install"></a>
## Installation

1. Install `tsaotun` first: `pip install tsaotun`.
2. Install `toolbox` addon: `tsaotun addon install https://github.com/qazbnm456/toolbox.git`.
3. Enable the addon: `tsaotun addon enable toolbox`.
4. Check if installation is successful: `tsaotun addon ls`.

If installation is okay, you should see somthing like:

```bash
$ tsaotun addon ls
ADDON NAME              ENABLED
toolbox                 True
```

<a name="contribute"></a>
## Contribute

If you have any good ideas and you wanna share with one another, just send me the PR immediately.

I can't wait to see your fabulous ideas. :smile:

<a name="license"></a>
## LICENSE

This project use [Apache License, Version 2.0](LICENSE).
